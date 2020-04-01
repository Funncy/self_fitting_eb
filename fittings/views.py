from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .forms import FittingForm


class FittingInit(TemplateView):
    template_name = "fittings/init.html"


class FittingFinish(TemplateView):
    template_name = "fittings/finish.html"


class FittingCerti1(TemplateView):
    template_name = "certi/certi1.html"


class FittingCerti2(TemplateView):
    template_name = "certi/certi2.html"

class FittingOpt(TemplateView):
    template_name = "fittings/opt.html"

class FittingOptList(TemplateView):
    template_name = "fittings/opt_list.html"


class FittingCreate(CreateView):
    template_name = "fittings/fit.html"
    form_class = FittingForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = FittingForm(request.POST, request.FILES)
        if form.is_valid():
            fit = form.save(commit=False)
            # 동의 구했는지 확인
            # 연락처 폼 확인
            if fit.check1 is False:
                print("test")

            fit.save()
            print(reverse("fittings:finish"))
            return redirect(reverse("fittings:finish"))
        return render(request, "fittings/fit.html", {"form": form})
