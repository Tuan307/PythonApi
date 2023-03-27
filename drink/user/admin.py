from django.contrib import admin

from .models import UserRegistration


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile', 'password',)
    list_display_links = ('email',)
    list_per_page = 50
    search_fields = ['email', 'name', 'fname']


# Register your models here.


admin.site.register(UserRegistration, UserAdmin)
