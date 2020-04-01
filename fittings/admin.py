from django.contrib import admin
from fittings.models import Fitting


@admin.register(Fitting)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "user_key",
        "kid_name",
        "parent_name",
        "location",
        "birthdate",
        "phone_number",
    )
