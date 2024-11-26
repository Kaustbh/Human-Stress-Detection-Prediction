from django.contrib import admin
from accounts.models import ConcreteUserProfile

class UserProfile(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(ConcreteUserProfile, UserProfile)

# Register your models here.
