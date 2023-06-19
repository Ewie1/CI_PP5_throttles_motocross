from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
# This will get the user information


def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class ContactFeedback(View):

    template_name = 'contact/contact.html'
    success_message = 'Message has been sent.'

    