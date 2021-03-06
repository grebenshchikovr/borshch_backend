from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from authapp.forms import BorshchUserLoginForm, BorshchUserRegisterForm
from authapp.models import BorshchUser
from myrecipeapp.models import MyRecipe
from mainapp.models import Cuisine, Recipe
from mainapp.views import RecipeList
from django.contrib import auth
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView


class LogIn(LoginView):
    template_name = 'authapp/login.html'
    from_class = BorshchUserLoginForm

    def get_success_url(self):
        return reverse('main')

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['submit_label'] = 'ОК'
        return context


class LogOut(LogoutView):
    next_page = 'main'


def register(request):

    if request.method == 'POST':
        register_form = BorshchUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = BorshchUserRegisterForm()

    context = {
        'form': register_form,
        'title': 'Регистрация',
        'submit_label': 'Зарегистрироваться'
    }
    return render(request, 'authapp/register.html', context)


class BorshchUserDetailView(DetailView):

    model = BorshchUser
    context_object_name = 'borshchuser'
    template_name = 'authapp/user_details.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_recipe_list'] = MyRecipe.objects.filter(borshchuser=self.kwargs['pk'])
        context['cuisine_list'] = Cuisine.objects.all()
        return context


class UserCuisineRecipeList(RecipeList):

    def get_queryset(self):
        self.cuisine = get_object_or_404(Cuisine, name=self.kwargs['cuisine'])
        return Recipe.objects.filter(myrecipe__borshchuser=self.kwargs['pk'], cuisine=self.cuisine)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the cuisines
        context['cuisine_list'] = Cuisine.objects.all()
        context['cuisine'] = self.cuisine
        return context