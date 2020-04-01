from django.urls import path
from . import views

app_name = "fittings"

urlpatterns = [
    path("", views.FittingInit.as_view(), name="init"),
    path("fitting", views.FittingCreate.as_view(), name="fitting"),
    path("finish", views.FittingFinish.as_view(), name="finish"),
    path("certi1", views.FittingCerti1.as_view(), name="certi1"),
    path("certi2", views.FittingCerti2.as_view(), name="certi2"),
    path("opt", views.FittingOpt.as_view(), name="opt"),
    path("opt_list", views.FittingOptList.as_view(), name="opt_list"),
]
