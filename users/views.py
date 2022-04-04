from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreatorForm
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreatorForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'