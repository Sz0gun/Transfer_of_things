from django.shortcuts import render
from django.views import View


# Create your views here.

class ShowPage(View):
    def get(self, request):
        return render(request, 'app/index.html')