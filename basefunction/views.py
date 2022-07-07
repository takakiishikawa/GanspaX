from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy

from django.views.generic import TemplateView
from .forms import AccountForm,AddAccountForm

from django.views.generic.edit import UpdateView,DeleteView


from .models import Account

from django.contrib.auth.models import User

from django.views import View
from django.template.response import TemplateResponse


from django.contrib.auth import login as auth_login

from django.views.generic import ListView


class topView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "basefunction/top.html")


class guideView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"basefunction/guide.html")


class usersView(ListView):
        template_name = 'basefunction/users.html'
        model=Account
        context_object_name="ganspa_list"


class registerView(TemplateView):

    def __init__(self):
        self.params={
            "AccountCreate":False,
            "account_form":AccountForm(),
            "add_account_form":AddAccountForm(),
        }
    
    def get(self,request):
        self.params["account_form"]=AccountForm()
        self.params["add_account_form"]=AddAccountForm()
        self.params["AccountCreate"]=False
        return render(request,"registration/register.html",context=self.params)
    
    def post(self,request):
        self.params["account_form"]=AccountForm(data=request.POST)
        self.params["add_account_form"]=AddAccountForm(data=request.POST)

        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            account=self.params["account_form"].save()
            account.set_password(account.password)
            account.save()
            add_account=self.params["add_account_form"].save(commit=False)
            add_account.user=account
            add_account.save()
            self.params["AccountCreate"]=True
        else:
            print(self.params["account_form"].errors)
        
        
        return render(request,"registration/register.html",context=self.params)




