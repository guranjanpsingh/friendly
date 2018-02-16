from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Help django manager profile user"""

    def create_user(self, email, name, password=None):
        """"""

        if not email:
            raise ValueError("Users must have email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save super user"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
