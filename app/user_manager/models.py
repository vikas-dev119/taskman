from django.utils import timezone
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from user_manager.UserManager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField(_('Is superuser'), default=False)
    username = models.CharField(_("First Name"), max_length=30, blank=False, default=None)
    first_name = models.CharField(_("First Name"), max_length=30, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=30, blank=True)
    email = models.EmailField(_("Email Address"), unique=True)
    is_staff = models.BooleanField(_('Is staff'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)    