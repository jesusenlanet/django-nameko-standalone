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

You need to specify the DJANGO_SETTINGS_MODULE environment variable. If not 'settings' is used by default

Inject the dependency into the nameko service with the DjangoModels dependency.

Supposing you injected the DjangoModels dependency into the `models` variable, you can use from your procedures like `self.models.MyModel.objects.all()`.


## Example

```python
from django_nameko_standalone import DjangoModels
from nameko.rpc import rpc


class NamekoService:
    name = "nameko_service"
    models = DjangoModels()  # Inject the django model dependency

    @rpc
    def get_items(self, host):
        cars = self.models.Item.objects.all()
        ...

```