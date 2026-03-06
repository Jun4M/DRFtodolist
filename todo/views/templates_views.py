from django.shortcuts import render
from .models import Todo
from django.views import View
from django.views.generic import ListView


def todo_list(request):  #  함수형
    todos = Todo.objects.all()
    return render(request, "todo/todo.html", {"todos": todos})


class TodoListView(View):  # 클래스형
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, "todo/todo.html", {"todos": todos})


class TodoListGenericView(ListView):  # 제너릭뷰
    model = Todo
    template_name = "todo/todo.html"  # 기본값: todo_list.html
    context_object_name = "todos"  # 기본값: object_list
