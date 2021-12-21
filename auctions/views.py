from django.contrib.auth import authenticate, login, logout, models
from django.db import IntegrityError
from django.db.models.fields import FloatField
#from django.forms.models import _Labels
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Staff, Propositions
from django import forms


def index(request):
    staff = Staff.objects.get(id=3)
    #staff.startprice =1000
    #staff.save()
    staff2 = Staff.objects.get(id=4)
    #staff2.startprice =899
    #staff2.save()
    
    return render(request, "auctions/index.html",{
        "staff": [staff, staff2]
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class Staff_Form(forms.Form):
    staff_name = forms.CharField(label="Staff name", max_length=64)
    staff_descript = forms.CharField(label="Description", max_length=200)
    start_price = forms.FloatField(label='Start price')
    staff_photo = forms.ImageField(label="Add staff photo")


def add_listing(request):
    if request.method == "POST":
        staff_form = Staff_Form(request.POST, request.FILES)
        if staff_form.is_valid():
            staff_name = staff_form.cleaned_data["staff_name"]
            staff_descript = staff_form.cleaned_data['staff_descript']
            start_price = staff_form.cleaned_data['start_price']
            staff_photo = staff_form.cleaned_data['staff_photo']
            current_user = request.user
            new_staff = Staff.objects.create(staffname=staff_name, staff_descript=staff_descript, startprice=start_price, image_one=staff_photo, staff_owner=current_user.id )
            new_staff.save()
    else:
        staff_form = Staff_Form()
      #  staff_form.staff_name.label="new staff name"
    return render(request, "auctions/add_listing.html", { 
        "listingform": staff_form
    })

