from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
    success_url = 'home'


class CustomLogoutView(LogoutView):
    next_page = 'login'
