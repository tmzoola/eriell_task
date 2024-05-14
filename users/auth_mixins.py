from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ADMIN, TEACHER, STUDENT


class AdminRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        elif not request.user.user_role == ADMIN:
            return HttpResponseRedirect(reverse('users:login_page'))
        return super().dispatch(request, *args, **kwargs)


class TeacherRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        elif not request.user.user_role == TEACHER:
            return HttpResponseRedirect(reverse('users:login_page'))
        return super().dispatch(request, *args, **kwargs)


class StudentRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        elif not request.user.user_role == STUDENT:
            return HttpResponseRedirect(reverse('users:login_page'))
        return super().dispatch(request, *args, **kwargs)