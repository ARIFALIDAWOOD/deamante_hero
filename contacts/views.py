from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
#from django.contrib.auth.models import User
from .models import Contact,Contact_Specific


def contact_sub(request):
    if request.method == 'POST':
        # listing_id = request.POST['listing_id']
        # listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        locality = request.POST['locality']
        subject = request.POST['subject']
        message = request.POST['message']
        if request.user.is_authenticated:
          user_id = request.POST['user_id']
          contact = Contact(name=name,email=email, phone=phone,locality=locality,subject=subject,message=message, user_id=user_id)
        else:
          contact = Contact(name=name,email=email, phone=phone,locality=locality,subject=subject,message=message)

        contact.save()

        # Send email
        # send_mail(
        #   'Property Listing Inquiry',
        #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #   'traversy.brad@gmail.com',
        #   [realtor_email, 'techguyinfo@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(
            request, 'Your request has been submitted, an executive will get back to you soon')
        return redirect('contact')

def contact_specific(request):
    if request.method == 'POST':
        prop = request.POST['prop']
        prop_Id = request.POST['prop_Id']
        prop_address = request.POST['prop_address']
        name = request.POST['name']
        phone = request.POST['phone']
        subject = request.POST['subject']
        email = request.POST['email']
        locality = request.POST['locality']
        message = request.POST['message']
        if request.user.is_authenticated:
          user_id = request.POST['user_id']
          contact = Contact_Specific(prop=prop,prop_Id=prop_Id,prop_address=prop_address,name=name,email=email, phone=phone,locality=locality,subject=subject,message=message, user_id=user_id)
        else:
          contact = Contact_Specific(prop=prop,prop_Id=prop_Id,prop_address=prop_address,name=name,email=email, phone=phone,locality=locality,subject=subject,message=message)

        contact.save()

        # Send email
        # send_mail(
        #   'Property Listing Inquiry',
        #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #   'traversy.brad@gmail.com',
        #   [realtor_email, 'techguyinfo@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(
            request, 'Your request has been submitted, an executive will get back to you soon')
        return redirect('contact')