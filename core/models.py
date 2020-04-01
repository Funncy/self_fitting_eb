from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamp Model """

    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now=True)

    # DB에 등록되지 않는 모델
    class Meta:
        abstract = True
