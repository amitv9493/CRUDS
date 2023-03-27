from django.shortcuts import redirect, render
from .models import Food
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import array as arr
# Create your views here.

def homeview(request):
    objects = Food.objects.filter(person = request.user)
    calories = [int(i.total_calories) for i in objects]
    # total_consumption = 
    total = sum(calories)
    
    context = {
        'food':objects,
        'user':request.user,
        'total':total,
    }
    return render(request, 'functioncrud/index1.html', context=context)

def update_view(request):
    food = Food.objects.filter(person=request.id) 
    return redirect(request, 'functioncrud/index1.html',context={'food':food})

def delete_view(request,pk):
    object = get_object_or_404(Food,pk=pk)
    object.delete()
    return redirect('home')


def add(request):
    if request.method == "POST":
        food  = request.POST.get('food')
        quantity  = request.POST.get('quantity')
        calorie  = request.POST.get('calorie')
        
        
        Food.objects.create(
            person = request.user,
            food_name = food,
            quantity = quantity,
            calories = calorie,
        )
        
        return redirect('home')
    return render(request, 'functioncrud/index1.html')

def update(request, pk):
    if request.method =="POST":
        name = request.POST.get('food')
        qty = request.POST.get('quantity')
        tq = request.POST.get('calorie')
        print(name)
        print(qty)
        print(tq)
        object = Food.objects.filter(id=pk).update(food_name = name,quantity = qty, calories = tq)
    return redirect('home')