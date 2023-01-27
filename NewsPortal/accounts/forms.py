from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='Common users')
        user.groups.add(common_users)
        return user
