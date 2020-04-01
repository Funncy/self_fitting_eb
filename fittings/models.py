from django.db import models
import datetime
from core import models as core_models


class Fitting(core_models.TimeStampedModel):
    def front_image_path(self, filename):
        dirname = "fitting/%Y/%m/%d/{}_{}/{}".format(
            self.kid_name, self.parent_name, filename,
        )
        dirname = datetime.datetime.now().strftime(str(dirname))
        return dirname

    """ Abstract Item Model """

    user_key = models.AutoField(primary_key=True)
    kid_name = models.CharField(max_length=200, verbose_name="아동이름")
    parent_name = models.CharField(max_length=200, verbose_name="법정대리인 이름")
    location = models.CharField(max_length=200, verbose_name="거주지")
    birthdate = models.DateField(verbose_name="생년월일")
    phone_number = models.CharField(max_length=200, verbose_name="연락처")
    height = models.IntegerField(verbose_name="키")
    weight = models.IntegerField(verbose_name="몸무게")
    check1 = models.BooleanField(verbose_name="개인정보 수집 및 활용 동의")
    check2 = models.BooleanField(verbose_name="개인정보 수집 및 활용 동의2")
    chair_width = models.IntegerField(verbose_name="좌폭")
    back_height = models.IntegerField(verbose_name="등 높이")
    leg_length = models.IntegerField(verbose_name="다리 길이")
    seat_depth = models.IntegerField(verbose_name="좌석 깊이")
    front_picture = models.ImageField(upload_to=front_image_path, verbose_name="정면사진")
    side_picture = models.ImageField(upload_to=front_image_path, verbose_name="측면사진")

    def __str__(self):

        return str(self.created.date()) + "_" + self.kid_name + "_" + self.parent_name
