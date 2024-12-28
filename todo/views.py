from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo

# Create your views here.


def index(request):
    items = Todo.objects.order_by("-date")
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item has been added successfully!")
            return redirect("todo")

    page = {"list": items, "forms": form, "title": "Todo List"}
    return render(request, "todo/index.html", page)


def remove(request, item_id):
    item = Todo.objects.get(pk=item_id)
    item.delete()
    messages.success(request, "Item has been deleted successfully!")
    return redirect("todo")
