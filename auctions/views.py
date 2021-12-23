from django.contrib.auth import authenticate, login, logout, models
from django.db import IntegrityError
from django.db.models import fields
from django.db.models.fields import FloatField
#from django.forms.models import _Labels
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Staff, Propositions
from PIL import Image
from django import forms

#Bound form with an image field


def index(request):
    staff = Staff.objects.all()
    return render(request, "auctions/index.html", {
        "staff": staff
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

#----------------------------------------------------------------
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
    staff_descript = forms.CharField(label="Description", widget=forms.Textarea)
    start_price = forms.FloatField(label='Start price')
    staff_photo = forms.ImageField(label="Add staff photo", required=False)

#-------------------------------------------------------------
def add_listing(request):
    if request.method == "POST":
        staff_form = Staff_Form(request.POST, request.FILES)
        if staff_form.is_valid():
            staff_name = staff_form.cleaned_data["staff_name"]
            staff_descript = staff_form.cleaned_data['staff_descript']
            start_price = staff_form.cleaned_data['start_price']
            staff_photo = staff_form.cleaned_data['staff_photo']
            current_user = request.user
            new_staff = Staff.objects.create(staffname=staff_name, staff_descript=staff_descript, startprice=start_price, image_one=staff_photo,  staff_owner=current_user )
            new_staff.save()
    else:
        staff_form = Staff_Form()
      #  staff_form.staff_name.label="new staff name"
    return render(request, "auctions/add_listing.html", { 
        "listingform": staff_form
    })

class AddSumForm(forms.Form):
    add_sum = fields.FloatField(default=1.0)  
      
#--------------------------------------------------------------
def staff_one(request, staff_id):
    staff_item = Staff.objects.get(id=staff_id)
    max_prop = staff_item.startprice
    price_max = Propositions.objects.aggregate('price')
    if price_max and max_prop < price_max:
        max_prop = price_max
    if request.method == "POST":
        add_form = AddSumForm(request.POST)
        if add_form.is_valid():
            newprop = add_form.changed_data['add_sum']
            newprop_obj = Propositions.objects.create(price=newprop, )

    propositions = Propositions.objects.filter(staff_id=staff_id)
    return render(request, "auctions/staffone.html", {
        "staff_item": staff_item, "propositions": propositions, "adddorm": add_form
    })

#----------------------------------------------------------------
def add_proposition(request, staff_id, summ_add):
    staff_item = Staff.objects.get(id=staff_id)

    return render(request, "auctions/staffone.html", {
        "staff_item": staff_item, "newprice": summ_add, 
        "addform": 
    })
        


