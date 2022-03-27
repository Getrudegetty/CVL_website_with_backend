from django.contrib import admin
from .models import   Services, Contact, Media

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname',)

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

