from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


def home(request):

    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
       

    #    save to database
        Contact.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            subject = subject,
            message = message,
        )



        # send to mail
        send_mail(
            subject= f"FBEC contact: {subject}",
            message=f"""

        New contact from submission

        Name: {first_name} {last_name}

        Email: {email}

        subject: {subject}


        message:
        {message}
""",

        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["techace48@gmail.com"],
        fail_silently=False
        )


        messages.success(request, "Your message has been sent successfully")

        return redirect("home")


    return render(request, "index.html" )


def single(request):
    return render(request, "single.html")