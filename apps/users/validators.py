from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django import forms

UserModel = get_user_model()


def validate_username(value: str):
    error_msg = ""
    if " " in value:
        error_msg = "Username must be one word only"

    elif value[0].isdigit():
        error_msg = "Username cannot start with a digit"

    elif len(value) < 3:
        error_msg = "Username must be at least 3 characters"

    elif not value.isalnum():
        error_msg = "Username must be alphanumeric"

    if error_msg:
        raise ValidationError(error_msg)


def validate_unique_email(email, username):
    if UserModel.objects.filter(email=email).exclude(username=username).exists():
        raise forms.ValidationError('The email address has already been registered.')
