from django.shortcuts import render
from .models import Food
# Create your views here.

def homeview(request):
    objects = Food.objects.filter(person = request.user)
    context = {
        'food':objects,
    }
    return render(request, 'functioncrud/index.html', context=context)