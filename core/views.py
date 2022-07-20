from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name='pages/index.html'
        context = {

        }
        return render(request, template_name, context)
