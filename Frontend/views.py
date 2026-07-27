from django.shortcuts import render
from .models import Food

def menu(request):
    normal_food = Food.objects.filter(category='Normal', available=True)
    event_food = Food.objects.filter(category='Event', available=True)

    return render(request, 'menu.html', {
        'normal_food': normal_food,
        'event_food': event_food,
    })

    
def order_page(request, id):
    food = get_object_or_404(Food, id=id)

    return render(request, 'order.html', {
        'food': food
    })