from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Owner, Cat, Application
from .forms import OwnerForm, CatForm, ApplicationForm

def home(request):
    return render(request, 'core/home.html')

def property_list(request):
    properties = Property.objects.filter(is_available=True)
    return render(request, 'core/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'core/property_detail.html', {'property': property})

def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('create_cat', owner_id=owner.pk)
    else:
        form = OwnerForm()
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
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.property = property
            application.save()
            return redirect('application_success')
    else:
        form = ApplicationForm()
    return render(request, 'core/apply.html', {'form': form, 'property': property})

def application_success(request):
    return render(request, 'core/application_success.html')