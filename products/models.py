from django.db import models
class Category(models.Model):
    #category table-Electronics,clothing,etc
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): #when you print category object it will shows name so use __str__
        return self.name
    class Meta: #in django admin shows categories instead of category
        verbose_name_plural="Categories"
class Product(models.Model):
    #Product table
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField(default=0)
    image=models.ImageField(upload_to='products/', blank=True,null=True) #stores images in media/products folder, form field is optional,database column can be empty
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')  #Foreign_key links Product to category
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) #updates the time stamp everytime record is saved
    is_active=models.BooleanField(default=True) #used to show/hide products without deleting them
    def __str__(self): #defines what to shows when you print an object
        return self.name