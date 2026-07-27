from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Food, Order



# =========================
# ADMIN LOGIN
# =========================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:


            if user.is_staff:

                login(request, user)

                return redirect("admin_order")


            else:

                messages.error(
                    request,
                    "❌ Admin Access Only"
                )


        else:

            messages.error(
                request,
                "❌ Invalid Username or Password"
            )


    return render(
        request,
        "login.html"
    )





# =========================
# NORMAL PAGES
# =========================

def home(request):

    return render(
        request,
        'home.html'
    )



def about(request):

    return render(
        request,
        'about.html'
    )



def services(request):

    return render(
        request,
        'services.html'
    )



def contact(request):

    return render(
        request,
        'contact.html'
    )





# =========================
# MENU PAGE
# =========================

def menu(request):


    normal_food = Food.objects.filter(

        category='Normal',

        available=True

    )


    event_food = Food.objects.filter(

        category='Event',

        available=True

    )



    return render(

        request,

        'menu.html',

        {

            'normal_food': normal_food,

            'event_food': event_food

        }

    )






# =========================
# CUSTOMER ORDER
# =========================

def order_page(request,id):


    food = get_object_or_404(

        Food,

        id=id

    )



    if request.method == "POST":


        customer_name = request.POST.get(
            "customer_name"
        )


        mobile = request.POST.get(
            "mobile"
        )


        address = request.POST.get(
            "address"
        )


        quantity = int(
            request.POST.get(
                "qty",
                1
            )
        )


        payment_method = request.POST.get(
            "payment"
        )


        location = request.POST.get(
            "location"
        )



        total_amount = (
            float(food.price)
            *
            quantity
        )



        Order.objects.create(


            food=food,


            customer_name=customer_name,


            mobile=mobile,


            address=address,


            quantity=quantity,


            total_amount=total_amount,


            payment_method=payment_method,


            payment_status="Pending",


            order_status="Pending",


            location=location


        )



        messages.success(

            request,

            "🎉 Order Placed Successfully"

        )



        return redirect(
            "menu"
        )




    return render(

        request,

        "order.html",

        {

            "food":food

        }

    )






# =========================
# ADD TO CART
# =========================

def add_to_cart(request,id):


    return redirect(

        "order_page",

        id=id

    )






def order(request):


    return render(

        request,

        "order.html"

    )






# =========================
# ADMIN ORDER + ADD FOOD
# =========================
# =========================
# ADMIN ORDER + ADD FOOD
# =========================

@login_required
def admin_order(request):

    # ADD FOOD
    if request.method == "POST":

        Food.objects.create(
            name=request.POST.get("name"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
            available=True
        )

        messages.success(request, "🍔 Food Added Successfully")
        return redirect("admin_order")

    # SHOW ORDERS
    orders = Order.objects.all().order_by("-created_at")

    # SHOW PRODUCTS
    foods = Food.objects.all().order_by("-id")

    return render(
        request,
        "admin_order.html",
        {
            "orders": orders,
            "foods": foods,
        }
    )


# =========================
# EDIT FOOD
# =========================

@login_required
def edit_food(request, id):

    food = get_object_or_404(Food, id=id)

    if request.method == "POST":

        food.name = request.POST.get("name")
        food.category = request.POST.get("category")
        food.price = request.POST.get("price")
        food.description = request.POST.get("description")

        if request.FILES.get("image"):
            food.image = request.FILES.get("image")

        food.save()

        messages.success(request, "✅ Food Updated Successfully")
        return redirect("admin_order")

    return render(
        request,
        "edit_food.html",
        {
            "food": food
        }
    )


# =========================
# DELETE FOOD
# =========================

@login_required
def delete_food(request, id):

    food = get_object_or_404(Food, id=id)

    food.delete()

    messages.success(request, "🗑 Food Deleted Successfully")

    return redirect("admin_order")