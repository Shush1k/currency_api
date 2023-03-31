from rest_framework import serializers

from core.models import Currency, Category, Transaction
from core.reports import ReportParams


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            "name",
            "code"
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class WriteTransactionSerializer(serializers.ModelSerializer):

    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())

    class Meta:
        model = Transaction
        fields = (
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )


class ReadTransactionSerializer(serializers.ModelSerializer):

    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )
        read_only_fields = fields


class ReportEntrySerializer(serializers.Serializer): # noqa
    category__name = serializers.CharField()
    total = serializers.DecimalField(max_digits=15, decimal_places=2)
    count = serializers.IntegerField()
    avg = serializers.DecimalField(max_digits=15, decimal_places=2)


class ReportParamsSerializer(serializers.Serializer): # noqa
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        # Usually ModelSerializer validation by default
        # In this case, we write a class with type annotation
        return ReportParams(**validated_data)
