from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm
from .models import Faq


def contact(request):
    """ A view to return the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_request = form.save()

            # Send confirmation email to user
            cust_email = contact_request.email
            subject = 'TravelTableTop Contact Request Received'
            body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'contact_request': contact_request}
            )

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [cust_email]
                )
            except Exception:
                messages.error(
                    request,
                    'There was an error sending your confirmation email. '
                    'Your message was still received.'
                )

            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect(reverse('contact_success'))
        else:
            messages.error(
                request,
                'Failed to send message. Please check the form and try again.')
    else:
        # Pre-populate form with user info if authenticated
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = ContactForm(initial=initial_data)

    template = 'contact/contact.html'
    # Get all FAQs
    faqs = Faq.objects.all()

    context = {
        'form': form,
        'faqs': faqs,
    }

    return render(request, template, context)


def contact_success(request):
    """ A view to return the contact success page """
    return render(request, 'contact/contact_success.html')
