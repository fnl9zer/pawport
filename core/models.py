from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cat(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveBigIntegerField()
    is_neutered = models.BooleanField(default=False)
    vaccination_record = models.TextField(blank=True)
    landlord_reference = models.TextField(blank=True)
    photo = models.ImageField(upload_to='cats/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.owner.name})"
    
class Landlord(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Property(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.TextField()
    state = models.CharField(max_length=100)
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    pet_deposit = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.state}"
    
    class Meta:
        verbose_name_plural = "Properties"
    
class Application(models.Model):
    STATUS_CHOICES =    [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cat.name} → {self.property.title} ({self.status})"
