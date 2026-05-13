from django.shortcuts import redirect, render , get_object_or_404
from .forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required 
from .models import *
from django.db.models import Q
import logging
from django.contrib import messages


def index (request):
    return render (request , 'web/index.html')

def register (request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration completed successfully')
            return redirect('login')
        else:
            form = CreateUserForm()
    context = {'form':form}
    return render (request , 'web/register.html' , context)



def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request , data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('dashboard')
    else:
        form = LoginForm()

    context = {'form':form}
    return render (request , 'web/login.html' , context)


@login_required(login_url='login') 
def dashboard(request):
    records = Record.objects.all()
    category = Category.objects.all()
    context = {'records':records , 'category':category}
    return render (request , 'web/dashboard.html' , context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def create_record(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record is Created')
            if 'create' in request.POST:
                return redirect('dashboard')
            elif 'create_another' in request.POST:
                form = RecordForm()
    context = {'form':form}
    return render(request , 'web/create_record.html' , context)
        
@login_required(login_url='login')
def view_record(request , record_id):
    record = get_object_or_404(Record , id = record_id)
    context = {'record':record}
    return render (request , 'web/view_record.html' , context) 

@login_required(login_url='login')
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = RecordForm(instance= record)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance= record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record is Updated')
            return redirect('dashboard')
    context = {'form':form}
    return render(request , 'web/update_record.html' , context)



@login_required(login_url='login')
def delete_record(request, record_id):
    record= get_object_or_404(Record, id = record_id)
    record.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('dashboard')



@login_required(login_url='login')
def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'Created Successfully')
            if 'create' in request.POST:
                return redirect('dashboard')
            elif 'create_another' in request.POST:
                form = CategoryForm()
        else:
            form = CategoryForm()
    context = {'form':form}
    return render(request, 'web/create_category.html' , context)

@login_required(login_url='login')
def delete_category(request, category_id):
    category= get_object_or_404(Category, id = category_id)
    category.delete()
    messages.success(request , 'Deleted Successfully')
    return redirect('dashboard')

@login_required(login_url='login')
def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = CategoryForm(instance= category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance= category)
        if form.is_valid():
            form.save()
            messages.success(request , 'Updated successfully')
            return redirect('dashboard')
        else:
            form = CategoryForm(instance= category)
            return redirect('update_category', category_id=category.id)
    context = {'form':form}
    return render(request , 'web/update_category.html' , context)
 




# Search Records View
logger = logging.getLogger(__name__)
@login_required(login_url='login')
def search_records(request):
    query = request.GET.get('query')
    results =[]
    try:
        if query:
            results = Record.objects.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) | 
                Q(id__icontains=query) | 
                Q(phone__icontains=query) |
                Q(address__icontains=query) |
                Q(category__name__icontains=query) |
                Q(height__icontains=query) |
                Q(weight__icontains=query)
            )
    except Exception as e :
        logger.error("An error occurred during search. Error details: %s", e)
    results_count=len(results)
    context = {'results':results, 'query':query,'resualt_count':results_count}
    return render(request , 'web/search_records.html' , context)

@login_required(login_url='login')
def search_category(request):
    query = request.GET.get('query')
    results = []
    try : 
        if query:
            results= Category.objects.filter(
                Q(name__icontains = query)
            )
    except Exception as e : 
        logger.error("An error occurred during search. Error details: %s", e)
    results_count = len(results)
    context = {'results':results , 'query':query , 'resault_count':results_count}
    return render(request, 'web/search_records.html' , context)


def custom_page_not_found(request, exception):
    return render(request, 'web/404.html', status=404)