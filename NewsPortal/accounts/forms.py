from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='Common users')
        user.groups.add(common_users)

        subject='Welcome to our news portal!'
        text = f'{user.username}, you have successfully registered!'
        html = (
            f'<b>{user.username}</b>, you have successfully registered on the '
            f'<a href="http://127.0.0.1:8000/news">site</a>'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, 'text/html')
        msg.send()

        return user
