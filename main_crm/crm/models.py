from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator , RegexValidator

# Category model
class Category(models.Model):
    name = models.CharField(max_length=250 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['-created_at']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Client model
class Record(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='records' , null=False, blank=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^\d{11}$', message="Phone number must be 11 digits")]
    )
    tall = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(250)])
    weight = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Client Record"
        verbose_name_plural = "Client Records"
