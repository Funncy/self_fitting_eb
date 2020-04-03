from django.contrib import admin
from fittings.models import Fitting
from django.utils.safestring import mark_safe

import csv
from django.http import HttpResponse


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Fitting)
class FittingAdmin(admin.ModelAdmin):

    list_display = (
        "user_key",
        "kid_name",
        "parent_name",
        "location",
        "birthdate",
        "phone_number",
        "get_front_picture",
        "get_side_picture",
        "created",
    )

    def get_front_picture(self, obj):
        return mark_safe(f'<img width="100" src="{obj.front_picture.url}"/>')

    def get_side_picture(self, obj):
        return mark_safe(f'<img width="100" src="{obj.side_picture.url}"/>')

    search_fields = ["kid_name", "parent_name"]

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [
            "user_key",
            "kid_name",
            "parent_name",
            "location",
            "birthdate",
            "phone_number",
            "height",
            "weight",
            "chair_width",
            "back_height",
            "leg_length",
            "seat_depth",
            # "front_picture",
            # "side_picture",
        ]

        row_name = {
            "user_key": "번호",
            "kid_name": "아동 이름",
            "parent_name": "법정대리인 이름",
            "location": "지역",
            "birthdate": "생년월일",
            "phone_number": "연락처",
            "height": "키",
            "weight": "몸무게",
            "chair_width": "좌폭",
            "back_height": "등 높이",
            "leg_length": "다리 길이",
            "seat_depth": "좌석 깊이",
        }

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)

        writer.writerow([row_name[field] for field in field_names])

        data = []
        for obj in queryset:
            for field in field_names:
                field_data = getattr(obj, field)
                # 번호가 11자리이면서 -가 없는 경우
                if field == "phone_number":
                    if len(field_data) == 11 and len(field_data.split("-")) != 3:
                        field_data = (
                            field_data[0:3]
                            + "-"
                            + field_data[3:7]
                            + "-"
                            + field_data[7:]
                        )

                data.append(field_data)
            row = writer.writerow(data)
            data.clear()

        return response

    export_as_csv.short_description = "Export Selected"
