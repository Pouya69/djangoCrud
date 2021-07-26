from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Order, UserMain
from .forms import OrderForm, UserForm
from django.contrib.auth.models import User

def hello(request):
    return render(request, "home.html", {'result': 5+5})


def operations(request):
    return render(request, "operations.html", {})


def result(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        return render(request, "result.html", {'full_name': f"{first_name} {last_name}"})


#################################################################


def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('/')
            
    context = {'form': form}
    return render(request, "create_order.html", context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            user = order.user
            user.orders.remove(order)
            user.orders.add(order)
            user.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "create_user.html", context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'order': order}
    return render(request, 'delete_order.html', context)


def create_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            original_user = User.objects.get(username=request.POST.get("username"))
            user = UserMain(original_user=original_user)
            user.save()
            return redirect('/')


    context = {'form': form}
    return render(request, "create_user.html", context)


def dashboard(request):
    return render(request, 'dashboard.html', {'users': User.objects.all(), 'orders': Order.objects.all()})
