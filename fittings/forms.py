from django import forms
from .models import Fitting

YEARS = [x for x in range(1940, 2021)]


class MySelectDateWidget(forms.SelectDateWidget):
    def get_context(self, name, value, attrs):
        old_state = self.is_required
        self.is_required = False
        context = super(MySelectDateWidget, self).get_context(name, value, attrs)
        self.is_required = old_state
        return context


class FittingForm(forms.ModelForm):
    class Meta:
        model = Fitting
        fields = [
            "kid_name",
            "parent_name",
            "location",
            "birthdate",
            "phone_number",
            "height",
            "weight",
            "check1",
            "check2",
            "chair_width",
            "back_height",
            "leg_length",
            "seat_depth",
            "front_picture",
            "side_picture",
        ]
        widgets = {
            "kid_name": forms.TextInput(attrs={"placeholder": "예)홍길동"}),
            "parent_name": forms.TextInput(attrs={"placeholder": "예)홍길동"}),
            "location": forms.TextInput(attrs={"placeholder": "예)경기도 시흥시"}),
            "birthdate": MySelectDateWidget(years=YEARS, empty_label=("년도", "월", "일")),
            "phone_number": forms.TextInput(attrs={"placeholder": "예)010-1111-2222"}),
            "height": forms.TextInput(attrs={"maxlength": "3", "style": "width:30px;"}),
            "weight": forms.TextInput(attrs={"maxlength": "3", "style": "width:30px;"}),
            "check1": forms.CheckboxInput(),
            "check2": forms.CheckboxInput(),
            "chair_width": forms.TextInput(
                attrs={"maxlength": "3", "style": "width:30px;"}
            ),
            "back_height": forms.TextInput(
                attrs={"maxlength": "3", "style": "width:30px;"}
            ),
            "leg_length": forms.TextInput(
                attrs={"maxlength": "3", "style": "width:30px;"}
            ),
            "seat_depth": forms.TextInput(
                attrs={"maxlength": "3", "style": "width:30px;"}
            ),
            "front_picture": forms.FileInput(
                attrs={"onchange": "front_upload_img(this);"}
            ),
            "side_picture": forms.FileInput(
                attrs={"onchange": "side_upload_img(this);"}
            ),
        }
        error_messages = {
            "kid_name": {"required": "아동이름을 입력해주세요.",},
            "parent_name": {"required": "법정대리인을 입력해주세요.",},
            "location": {"required": "거주지를 입력해주세요.",},
            "birthdate": {"required": "생년월일을 입력해주세요.",},
            "phone_number": {"required": "연락처를 입력해주세요.",},
            "height": {"required": "아동의 키를 입력해주세요.",},
            "weight": {"required": "아동의 몸무게를 입력해주세요.",},
            "chair_width": {"required": "좌폭을 입력해주세요.",},
            "back_height": {"required": "등 높이를 입력해주세요.",},
            "leg_length": {"required": "다리 길이를 입력해주세요.",},
            "seat_depth": {"required": "좌석 깊이를 입력해주세요.",},
            "front_picture": {"required": "정면사진을 업로드해주세요.",},
            "side_picture": {"required": "측면사진을 업로드해주세요.",},
        }

    def clean_check1(self, *args, **kwargs):
        check1 = self.cleaned_data.get("check1")
        if check1 is False:
            raise forms.ValidationError("동의하셔야합니다.")
        return check1

    def clean_check2(self, *args, **kwargs):
        check2 = self.cleaned_data.get("check2")
        if check2 is False:
            raise forms.ValidationError("동의하셔야합니다.")
        return check2
