This package setup the django framework to take advantage of the ORM features and some other django features.

You need to specify the DJANGO_SETTINGS_MODULE environment variable, if not, 'settings' is used by default.

Inject the dependency into the nameko service with the DjangoModels dependency.

Supposing you injected the DjangoModels dependency into the `models` variable, you can use from your procedures like `self.models.MyModel.objects.all()`.
