from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserRecord
from django.db.models import Q
import logging
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

# register view
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration is completed Sucessfully")
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'web/register.html', context)

# login view
def userLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Loged in Sucessfully")
                return redirect('dashboard')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'web/login.html', context)


# dashboard view
@login_required(login_url='login')
def dashboard(request):
    records = UserRecord.objects.all()
    return render(request, 'web/dashboard.html', context={'records': records})


# logout view
def userLogout(request):
    logout(request)
    messages.success(request, "Loged out Sucessfully")
    return redirect('login')

# create record
@login_required(login_url='login')
def createRecord(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Created Sucessfully")
            return redirect('dashboard')
    else:
        form = CreateRecordForm()

    context = {'form': form}
    return render(request, 'web/create-record.html', context)


# view single record
@login_required(login_url='login')
def viewRecord(request, record_id):
    single_record = get_object_or_404(UserRecord, id=record_id)
    context = {'record': single_record}
    return render(request, 'web/view_record.html', context)

# update record
@login_required(login_url='login')
def updateRecord(request, record_id):
    single_record = get_object_or_404(UserRecord, id=record_id)
    form = UpdateRecordForm(instance=single_record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=single_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record is Updated Sucessfully")
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'web/update_record.html', context)

# delete record
@login_required(login_url='login')
def deleteRecord(request, record_id):
    single_record = get_object_or_404(UserRecord, id=record_id)
    single_record.delete()
    messages.success(request, "Record is Deleted Sucessfully")
    return redirect('dashboard')

# search record
logger = logging.getLogger(__name__)
@login_required(login_url='login')
def searchRecord(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = UserRecord.objects.filter(Q(f_name__icontains=query) | Q(id__icontains=query))
    except Exception as e:
        logger.error('Invalid Error while searching with: %s', e)

    return render(request, 'web/search.html', context={'results': results, 'query': query})


# 404 page handling
def custom404Page(request, exception):
    return render(request, 'web/404.html', status=404)