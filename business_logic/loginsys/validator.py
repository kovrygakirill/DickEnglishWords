from django.contrib.auth.models import User


class Validator:
    @staticmethod
    def get_error_valid_user(user: User | None) -> str:
        error = ''

        if user is None:
            error = "User wasn't found"
        elif not user.user_profile.is_confirm:
            error = "Confirm registration(The letter sent to email)"

        return error

    @staticmethod
    def check_exist_username(username: str) -> bool:
        res = True
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            res = False

        return res

    @staticmethod
    def check_exist_email(email: str) -> bool:
        res = True
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            res = False

        return res

    def get_error_valid_fields(self, username: str | None = None, email: str | None = None,
                               password: str | None = None, c_password: str | None = None) -> str:
        result = ""
        if username is not None:
            result = 'This username already existed' if self.check_exist_username(username=username) else result

        elif email is not None:
            result = 'This email already used' if self.check_exist_email(email=email) else result

        return result
