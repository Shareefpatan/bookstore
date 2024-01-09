from django.contrib import admin
from .models import Books,Buy,Review,User,UserProfile,Rent

# Register your models here.
admin.site.register(Books)
admin.site.register(Buy)
admin.site.register(Rent)
admin.site.register(UserProfile)