from pyexpat import model
from django.contrib import admin
from . import models


admin.site.register(models.User)
admin.site.register(models.Agent)
admin.site.register(models.Lead)