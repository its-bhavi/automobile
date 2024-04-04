from django.contrib import admin
from automobile.models import *


class Details1(admin.ModelAdmin):
    list_display=('cname','model')

admin.site.register(Details,Details1)
# Register your models here.
