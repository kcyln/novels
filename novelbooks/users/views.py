from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class RegisterView(View):
    def get(self ,request):
        return render(request, "register.html")
    
    def post(self, request):
        pass



class LoginView():
    def get(self):
        pass
    
    def post(self):
        pass