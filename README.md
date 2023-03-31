 Flake8
--------

### config ``.flake8``


```ini
[flake8]
exclude=*/migrations/*
max-line-length=120
```

Flake8 runs all the tools by launching the single `flake8` command.

It displays the warnings in a per-file, merged output.

It also adds a few features:
- lines that contain a ``# noqa`` comment at the end will not issue warnings.
- you can ignore specific errors on a line with ``# noqa: <error>``, e.g.,
  ``# noqa: E234``. Multiple codes can be given, separated by comma. The ``noqa`` token is case insensitive, the colon before the list of codes is required otherwise the part after ``noqa`` is ignored
- Git hooks

[Flake8 Documentation](https://flake8.pycqa.org/en/latest/)

Poetry
-------

In this project, I used `poetry` for the first time instead of the standard `pip` installer.

Pre-commit
-----------


Django Rest Framework
----------------------

- `ModelViewsets` - it`s much more convenient than I thought.
- `serializers.Serializer` - must be used when there is no need to store data in the database, but need data validation (reports as example)
- Renderer classes - broadening of one's outlook
