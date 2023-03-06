from django.contrib import admin

from django.contrib import admin
from iranian_cities.admin import IranianCitiesAdmin
from test_app.models import TestModel

@admin.register(TestModel)
class TestModelAdmin(IranianCitiesAdmin):
    pass