from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to="")
    book_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
#----------------------------------------------------------------------
class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    product = models.ForeignKey(Books, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}_{self.product.title}_{self.id}"

from django.db import models
from django.contrib.auth.models import User



class Cart(models.Model):
    cart_id = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Books, on_delete=models.PROTECT)

    def __str__(self):
        return self.product.title

class User(models.Model):
    username = models.CharField(max_length=55)  # Change 'user' to 'username'
    email_id = models.EmailField()
    city = models.CharField(max_length=20)
    date_joined = models.DateField()

    def __str__(self):
        return self.username  # Corrected to 'self.username'

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    # Other fields related to the user profile

    def __str__(self):
        return self.user.username
   
# models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.timestamp}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    # Other fields related to the user profile

    def __str__(self):
        return self.user.username
    
class Rent(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    rented_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.username} rented {self.book.title}"