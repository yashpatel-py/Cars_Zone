from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        contact.save()
        messages.success(request, 'Your inquiry has been submitted, we will get back to you soon.')

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            'New care inquiry',
            'You have a new care inquiry for the ' + car_title + ' car. Please check the admin panel for more details.',
            'gameforyash@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        return redirect('/cars/' + car_id)
