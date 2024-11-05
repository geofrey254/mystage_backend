from django.contrib import admin
from .models import Stage, Stop, Sacco, Road


@admin.register(Stage)
class stageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Stop)
class stopAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Sacco)
class saccoAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Road)
class roadAdmin(admin.ModelAdmin):
    list_display = ['name']
