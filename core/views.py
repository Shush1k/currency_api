from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_yaml.renderers import YAMLRenderer

from core.models import Currency, Category, Transaction
from core.reports import transactions_report
from core.serializers import CurrencySerializer, CategorySerializer, WriteTransactionSerializer, \
    ReadTransactionSerializer, ReportEntrySerializer, ReportParamsSerializer


class CurrencyListAPIView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    renderer_classes = [JSONRenderer, YAMLRenderer]


class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class TransactionModelViewSet(ModelViewSet):
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("category__name",)
    ordering_fields = ("amount", "date")
    filterset_fields = ("currency__code", "category__name",)

    def get_queryset(self):
        return Transaction.objects.select_related("currency", "category")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionReportAPIView(APIView):
    def get(self, request): # noqa
        params_serializer = ReportParamsSerializer(data=request.GET, context={"request": request})
        params_serializer.is_valid(raise_exception=True)
        params = params_serializer.save()
        data = transactions_report(params)
        serializer = ReportEntrySerializer(data, many=True)
        return Response(serializer.data)
