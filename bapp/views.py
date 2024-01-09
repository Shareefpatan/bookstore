import uuid
import json
from django.shortcuts import render,redirect, get_object_or_404
from .models import  Books, User,Buy,Review
from django.http import HttpResponse
from bapp import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from .forms import ReviewForm,RentForm

def base(request):
    return render(request, 'base.html')

def main(request):
    b=Books.objects.all()
    if request.GET.get('q'):
      query = request.GET.get('q') 
      b = Books.objects.filter(title__icontains=query)
    context={'b':b,}
    return render(request,'main.html',context)
from django.db.models import Avg

def detail(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    reviews = Review.objects.filter(book=book)
    context = {'d': book,'reviews': reviews}
    return render(request, 'detail.html', context)

def form(request):
    return render(request,'form.html')

def returned(request):
    return render(request,'returned.html')

def rent_book(request, book_id):
    book = get_object_or_404(Books, pk=book_id)

    if request.method == 'POST':
        user_id = request.POST.get('user')
        email = request.POST.get('email')
        rented_date = request.POST.get('rented_date')
        return_date = request.POST.get('return_date')
        messages.success(request, f"You have successfully rented '{book.title}'. You can now take the book.")
        return redirect('bapp:main')
    return render(request, 'rent_book.html', {'book': book})

def calculate_fine(return_date):
    days_overdue = (timezone.now().date() - return_date).days
    fine_amount = 5 * days_overdue
    return fine_amount

@login_required
def order(request, book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        return HttpResponse("Invalid book ID")
    current_user = request.user
    book = Books.objects.get(pk=book_id)
    total_amount = book.price
    order = Buy.objects.create(user=current_user, product=book, quantity=1, price=total_amount)
    order.save()
    success_message = "Your order has been successfully placed."
    context = {"success_message": success_message, "total_amount": total_amount}
    return render(request, "success.html", context)

def return_view(request):
    return render(request,'done.html')

def cancel_view(request):
    return render(request,'cancel.html') 

def book_detail(request, book_id):
    book = Books.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    is_available = book.book_available
    context = {
        'book': book,
        'reviews': reviews,
        'is_available': is_available    
    }
    book = get_object_or_404(Books, pk=book)
    return render(request, 'book_detail.html', {'book': book})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=review.book.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('book_detail', book_id=review.book.id)
    return render(request, 'delete_review.html', {'review': review})

def add_review(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user if request.user.is_authenticated else None
            review.save()
            return redirect('bapp:main')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'book': book})
 
def rent_book(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            rent_instance = form.save(commit=False)
            rent_instance.book_id = book_id
            rent_instance.rented_date = form.cleaned_data['rented_date']
            rent_instance.save()
            book = Books.objects.get(pk=book_id)
            book.book_available = False
            book.save()
            messages.success(request, f"You have successfully rented '{book.title}'. You can now take the book.")
            return redirect('bapp:detail', book_id=book_id)
    else:
        form = RentForm()
    return render(request, 'rent_book.html', {'form': form, 'book_id':book_id})
