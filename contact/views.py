from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .forms import ContactForm
from products.models import Product, Category
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

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        categories_list = Category.objects.all()

        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactForm(initial={'email': email})
        else:
            contact_form = ContactForm()

        context = {
            'categories_list': categories_list,
            'contact_form': contact_form
        }

        return render(request, 'contact/contact.html',
                      context)
