# DJANGO NAMEKO STANDALONE
## Use django into your nameko services

## Requirements
Developed for Python3.6.

Have dependecies of:

* Django==2.1.4
* nameko==2.11.0

## Installation
`pip install django-nameko-standalone`

## Usage
This package setup the django framework to take advantage of the ORM features and some other django features.

You need to specify the DJANGO_SETTINGS_MODULE environment variable, if not, 'settings' is used by default.

Inject the dependency into the nameko service with the DjangoModels dependency.

Supposing you injected the DjangoModels dependency into the `models` variable, you can use from your procedures like `self.models.MyModel.objects.all()`.


## Configuration
### Django nameko standalone configuration
django-nameko-standalone need the next setting variable to work:
```python
DJANGO_NAMEKO_STANDALONE_APPS = ("<my_django_app>",)  # apps to load models from
```
This variable control the applications where to load models.


### Django configuration
To configure the django ORM, just configure it as normally for Django.

The `INSTALLED_APPS` and `SECRET_KEY` settings needs to be defined to make Django work.

```python
# Minimum configuration required
DJANGO_NAMEKO_STANDALONE_APPS = ("<my_django_app>",)
INSTALLED_APPS = ("<mi_django_app>",)
SECRET_KEY = '<your_secret_key>'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database>',
        'USER': '<user>',
        'HOST': '<host>',
        'PORT': 5432,
    }
}
```

## Example

```python
from django_nameko_standalone import DjangoModels
from nameko.rpc import rpc


class NamekoService:
    name = "nameko_service"
    models = DjangoModels()  # Inject the django model dependency

    @rpc
    def get_items(self, host):
        items = self.models.Item.objects.all()
        ...

```