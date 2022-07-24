from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})


def lists(request):
    lists = ToDoList.objects.all()
    return render(request, "main/lists_display.html", {'lists': lists})


def id_page(response, id):
    list = ToDoList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get('save'):
            for item in list.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get('newItem'):
            txt = response.POST.get("new")

            if len(txt) > 2:
                list.item_set.create(text=txt, complete=False)
            else:
                print("ERROR: LULS")

    return render(response, "main/lists.html", {'ls': list})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            todo = ToDoList(name=name)
            todo.save()
        
        return HttpResponseRedirect("/%i" %todo.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {'form': form})
