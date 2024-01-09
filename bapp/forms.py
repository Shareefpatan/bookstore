from collections.abc import Mapping
from typing import Any
from django import forms
from .models import Review,Rent

class User(forms.Form):
    Username=forms.CharField(max_length=55)
    Bookname=forms.CharField(max_length=55)
    email_id=forms.EmailField()
    city=forms.CharField(max_length=20)
    date=forms.DateField()
    def __init__(self,request,*args,**kwargs):
        self.request=request
        super(User,self).__init__(*args,**kwargs)

class CartForm(forms.Form):
    quantity=forms.IntegerField(initial=1)
    product_id=forms.IntegerField(widget=forms.HiddenInput)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

class BookRent(forms.Form):
    user=forms.CharField(max_length=25)
    email=forms.EmailField(max_length=55)
    return_date=forms.DateField()
    rented_date=forms.DateField()

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['username', 'email', 'rented_date', 'return_date']
        widgets = {
            'rented_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

