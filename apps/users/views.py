from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views, View

from apps.quiz.models import QuizResult
from apps.users.forms import RegistrationForm, LoginForm
from django.contrib.auth import get_user_model, login, authenticate

UserModel = get_user_model()


# Create your views here.
class RegisterView(views.CreateView):
    model = UserModel
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class SignInView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


class Logout(LoginRequiredMixin, View):
    login_url = reverse_lazy('home')

    def get(self, request):
        logout(request)
        return redirect('home')


class ProfileView(LoginRequiredMixin, views.DetailView):
    model = UserModel
    template_name = 'users/profile.html'

    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_results_python'] = (QuizResult.objects.filter(user=self.get_object(), quiz_name='Python').
                                          order_by('quiz_name', '-correct_answers', 'finish_time')[:7])

        context['best_results_js'] = (QuizResult.objects.filter(user=self.get_object(), quiz_name='Js').
                                      order_by('quiz_name', '-correct_answers', 'finish_time')[:7])
        return context

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            if request.user == user:
                return super().get(request, *args, **kwargs)
            else:
                return redirect(reverse('profile', kwargs={'username': str(request.user.username)}))
        except Http404:
            return redirect(reverse('profile', kwargs={'username': str(request.user.username)}))
