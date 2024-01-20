from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator

from apps.users.validators import validate_username, validate_unique_email

UserModel = get_user_model()


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-style',
                'autocomplete': 'off',
                'id': 'logemail',
                'name': 'logemail',
            }
        ),
        validators=[validate_username],
    )

    email = forms.EmailField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-style',
                'autocomplete': 'off',
                'id': 'logemail',
                'name': 'logemail',
            }
        )
    )

    password1 = forms.CharField(
        label='',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-style',
                'autocomplete': 'off',
                'id': 'logpass',
                'name': 'logpass',
            }
        ),
        validators=[MinLengthValidator(
            6,
            "Password must be greater than 6 characters")
        ],
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-style',
                'autocomplete': 'off',
                'id': 'logpass',
                'name': 'logpass',
                'type': 'password',
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        validate_unique_email(email, username)

        return email

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username or Email',
                'class': 'form-style',
                'autocomplete': 'off',
                'id': 'logemail',
                'name': 'logemail',
                # 'type': 'text',
            }
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-style',
                'autocomplete': 'off',
                'id': 'logpass',
                'name': 'logpass',
            }
        )
    )

    error_messages = {
        'invalid_login': 'Invalid username or password!',
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Authenticate using both username and email
            self.user_cache = authenticate(
                self.request, username=username, password=password)

            if self.user_cache is None:
                raise self.get_invalid_login_error()

        self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
