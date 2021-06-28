from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Review, Spot, User


class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_active', ]


class SpotAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'prefecture', ]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'spot', 'star', ]


admin.site.register(User, MyUserAdmin)
admin.site.register(Spot, SpotAdmin)
admin.site.register(Review, ReviewAdmin)
