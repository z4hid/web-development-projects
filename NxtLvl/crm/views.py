from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import ClientRecord
from django.contrib import messages

# Homepage
def home(request):
    
    return render(request, 'crm/index.html')


# Register
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created succesfully!')
            
            return redirect('my-login')
    
    context = {'form': form}
    
    return render(request, 'crm/register.html', context=context)


# Login a User
def my_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                
                return redirect('dashboard')
                
    context = {'login_form':form}
    return render(request, 'crm/my-login.html', context=context)


# Logout 
def user_logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('my-login')


# Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    
    my_records = ClientRecord.objects.all()

    context = {'records': my_records}
    
    return render(request, 'crm/dashboard.html', context=context)

# Add a record
@login_required(login_url='my-login')
def create_record(request):
    form = AddRecordForm
    
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your record was created!')
            
            return redirect('dashboard')
        
    context = {'form': form}
    
    return render(request, 'crm/create-record.html', context=context)
  

# Update a record
@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = ClientRecord.objects.get(id=pk)
    
    form  = UpdateRecordForm(instance=record) # Get a perticular user record by instance
    
    if request.method == 'POST':
        
        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your record was updated!')
            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'crm/update-record.html', context=context)
        
# Read or view a singular record
@login_required(login_url='my-login')
def single_record(request, pk):
    all_records = ClientRecord.objects.get(id=pk)
    
    return render(request, 'crm/view-record.html', {'record':all_records}) # without context


# Delete a Record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = ClientRecord.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Your record was deleted!')
    return redirect('dashboard')