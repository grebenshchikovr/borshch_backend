from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import BorshchUserLoginForm
from authapp.models import BorshchUser
from myrecipeapp.models import MyRecipe
from django.contrib import auth
from django.urls import reverse
from django.views.generic import DetailView


def login(request):
    title = 'вход'

    login_form = BorshchUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


class BorshchUserDetailView(DetailView):

    model = BorshchUser
    context_object_name = 'borshchuser'
    template_name = 'authapp/user_details.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['my_recipe_list'] = MyRecipe.objects.filter(borshchuser=self.kwargs['pk'])
        return context
