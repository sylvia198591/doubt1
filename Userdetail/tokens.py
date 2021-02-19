from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six
import six
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.cuser.email_confirmed) + six.text_type(user.profile.accno)
        )

account_activation_token = AccountActivationTokenGenerator()