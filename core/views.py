from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Property, Owner, Cat, Application
from .forms import RegisterForm, CatForm, ApplicationForm
from django.shortcuts import redirect

def home(request):
    return render(request, 'core/home.html')

def property_list(request):
    query = request.GET.get('state', '')
    if query:
        properties = Property.objects.filter(is_available=True, state__icontains=query)
    else:
        properties = Property.objects.filter(is_available=True)
    return render(request, 'core/property_list.html', {'properties': properties, 'query': query})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'core/property_detail.html', {'property': property})

def create_owner(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # create owner profile
            owner = Owner.objects.create(
                name=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            # log in automatically
            login(request, user)
            return redirect('create_cat', owner_id=owner.pk)
    else:
        form = RegisterForm()
    return render(request, 'core/create_owner.html', {'form': form})

def create_cat(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.owner = owner
            cat.save()
            return redirect('property_list')
    else:
        form = CatForm()
    return render(request, 'core/create_cat.html', {'form': form, 'owner': owner})

def apply_to_property(request, property_pk):
    property = get_object_or_404(Property, pk=property_pk)
    submitted = False
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.property = property
            application.save()
            submitted = True
            form = ApplicationForm()
    else:
        form = ApplicationForm()
    return render(request, 'core/apply.html', {'form': form, 'property': property, 'submitted': submitted})

def application_success(request):
    return render(request, 'core/application_success.html')

def forgot_password(request):
    sent = False
    if request.method == 'POST':
        sent = True
    return render(request, 'core/forgot_password.html', {'sent': sent})

def create_admin(request):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@pawport.com', 'pawport123')
    return render(request, 'core/home.html')

def home(request):
    if request.user.is_authenticated:
        return redirect('property_list')
    return redirect('login')