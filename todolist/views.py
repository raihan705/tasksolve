from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.




def index(request):
    context={
        'welcome_index': "Welcome to Home page",
    }
    return render(request,'index.html',context)


@login_required
def todolist(request):

    if request.method == "POST" :
        form = TaskForm(request.POST or None)  

        if form.is_valid():
            instance = form.save( commit=False)
            instance.user = request.user
            instance.save()
        
        messages.success(request,("The new task is added successfully"))

        return redirect('todolist')

    else:

        all_task = Tasklist.objects.filter(user = request.user)
        paginator = Paginator(all_task, 5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request,'task.html', {'all_task':all_task})

def deletetask(request, task_id):
     task= Tasklist.objects.get(pk=task_id)
     if task.user == request.user :
        task.delete()
     else :
        messages.error(request,("Access Restricted"))

     return redirect('todolist')
        
def edit_task(request, task_id):
    if request.method == 'POST' :
        id =Tasklist.objects.get(pk=task_id)
        form_id= TaskForm(request.POST or None , instance=id)

        if form_id.is_valid():
            form_id.save()


        messages.success(request,("The task is updated"))
        return redirect('todolist')

    else:
        task_obj=Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj})

    
def complete_task(request, task_id):
         task= Tasklist.objects.get(pk=task_id)
         if task.user == request.user:
            task.done=True
            task.save()
         else :
            messages.error(request,("Access Restricted"))

         return redirect('todolist')


def notcomplete_task(request, task_id):
                task= Tasklist.objects.get(pk=task_id)
                task.done=False
                task.save()
                return redirect('todolist')







def contact(request):
    context={
        'welcome_contact': "Welcome to contactpage",
    }
    return render(request,'contact.html',context)






def about(request):
    context={
        'welcome_about': "Welcome to aboutpage",
    }
    return render(request,'about.html',context)


    