from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


# Create your views here.
def todo_view(request):
    all_todo_item = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_todo_item})


def add_todo(request):
    # create a new todo item
    # save
    # redriect to todoView
    c = request.POST ['content']
    new_item = TodoItem(content=c)
    new_item.save()
    return HttpResponseRedirect('/todo/')


def delete_todo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
