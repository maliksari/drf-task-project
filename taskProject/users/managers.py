from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy


class CustomUserManager(BaseUserManager):
    """
    E-postanın benzersiz tanımlayıcılar olduğu özel kullanıcı modeli yöneticisi
    kullanıcı adları yerine kimlik doğrulama için.
    """

    def create_user(self, email, password, **extra_field):
        """
                Verilen e-posta ve şifre ile bir Kullanıcı oluşturun ve kaydedin.
        """
        if not email:
            raise ValueError(gettext_lazy('E-posta gereklidir'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
          Verilen e-posta ve şifre ile bir Süper Kullanıcı oluşturun ve kaydedin.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
