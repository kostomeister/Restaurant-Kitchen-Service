from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View


class SuperUserCheckMixin(UserPassesTestMixin, View):
    """Checks if user is superuser or not"""
    def test_func(self):
        return self.request.user.is_superuser
