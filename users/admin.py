from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class OrderItemAdmin(admin.ModelAdmin):
    pass
