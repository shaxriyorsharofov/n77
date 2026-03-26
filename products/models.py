from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from shared.models import BaseModel
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=90)
    
    class Meta:
        db_table = 'category'
        ordering = ['-id']
        
    def __str__(self):
        return self.name
        

# BMW, MERS, AUDI, CHEVROLET = ('bmw', 'audi', 'mers', 'chevrolet')

class Cars(BaseModel):
    MAKE = (
        ('BMW', "bmw"),
        ('AUDI', 'audi'),
        ('MERS', 'mers'),
        ('CHEVROLET', 'chevrolet')    
    )
    
    model = models.CharField(max_length=29)
    make = models.CharField(max_length=29, choices=MAKE, default="bmw")
    price = models.DecimalField(decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cars/', \
        validators=[FileExtensionValidator(allowed_extensions=['JPG', 'PNG', 'jpg', 'png'])])
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2026), MinValueValidator(1885)])
    desc = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.model
    
    
    
    class Meta:
        db_table = 'cars'
        ordering = ['-id']

class Order(BaseModel):
    user = models.CharField(max_length=20)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    
    class Meta:
        db_table = 'order'
        ordering = ['-id']
        
    def __str__(self):
        return f"{self.user} | {self.car.model}"
    
    def save(self, *args, **kwargs):
        self.total_price = self.count * self.car.price
        super().save(*args, **kwargs)
    
    
        
    