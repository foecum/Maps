from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def gitta_redirect_view(request, *args, **kwarg):
    return HttpResponse("hello")


class GittaRedirectView(View):
    def get(request, *args, **kwarg):
        return HttpResponse("hello again")
