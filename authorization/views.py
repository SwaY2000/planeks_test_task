from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
    success_url = 'home'
