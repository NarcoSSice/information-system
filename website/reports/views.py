from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from .forms import AddPublicationForm, RegisterUserForm, LoginUserForm
from .models import *
from .word_document import word_document

list_tables = [One, Two, Three, Four, FiveOne, FiveTwoOne, FiveTwoTwo, FiveThreeOne,
               FiveThreeTwo, FiveFourOne, FiveFourTwo, Six, Seven]

def based(cleaned_data, data):
    if cleaned_data['foreign_editions']:
        if cleaned_data['published']:
            FiveTwoOne.objects.create(**data)
        if cleaned_data['ready_for_print']:
            FiveTwoTwo.objects.create(**data)
    if cleaned_data['mnbd_publications']:
        if cleaned_data['published']:
            FiveThreeOne.objects.create(**data)
        if cleaned_data['ready_for_print']:
            FiveThreeTwo.objects.create(**data)
    if cleaned_data['foreign_authors']:
        if cleaned_data['published']:
            FiveFourOne.objects.create(**data)
        if cleaned_data['ready_for_print']:
            FiveFourTwo.objects.create(**data)
    if cleaned_data['publications_with_students']:
        Six.objects.create(**data)


# functions
def monograph(cleaned_data, data):
    if cleaned_data['monograph_check']:
        One.objects.create(**data)
    if cleaned_data['collective_monograph']:
        Two.objects.create(**data)


def article(cleaned_data, data):
    if cleaned_data['professional_publication']:
        FiveOne.objects.create(**data)
    based(cleaned_data, data)


def thesis(cleaned_data, data):
    based(cleaned_data, data)


# views

class ReportsIndex(ListView):
    paginate_by = 5
    template_name = 'reports/index.html'
    context_object_name = 'pubs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = {
            'title': 'Головна сторінка',
            'tables': list_tables,
        }
        context.update(add_context)
        return context

    def get_queryset(self):
        return AllReports.get_data()


class Addpub(FormView):
    template_name = 'reports/addpublication.html'
    form_class = AddPublicationForm
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Додати публікацію', 'tables': list_tables}

    def form_valid(self, form):
        type_publication = form.cleaned_data['category'].name
        data = {
            'name': form.cleaned_data['name'],
            'category': form.cleaned_data['category'],
        }
        executions = {
            'Монографія': 'monograph(form.cleaned_data, data)',
            'Підручник': 'Three.objects.create(**data)',
            'Навчальний посібник': 'Four.objects.create(**data)',
            'Інший вид публікації': 'Seven.objects.create(**data)',
            'Стаття': 'article(form.cleaned_data, data)',
            'Тези': 'thesis(form.cleaned_data, data)'
        }
        eval(executions[type_publication])
        AllReports.objects.create(**data)
        return super().form_valid(form)


class ShowTable(ListView):
    paginate_by = 5
    template_name = 'reports/table.html'
    context_object_name = 'pubs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = {
            'title': eval(self.kwargs['name'] + '.get_name()'),
            'tables': list_tables,
        }
        context.update(add_context)
        return context

    def get_queryset(self):
        return eval(self.kwargs['name'] + '.objects.all()')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'reports/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Реєстрація', 'tables': list_tables}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'reports/login.html'
    extra_context = {'title': 'Авторизація', 'tables': list_tables}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    context = {
        'title': 'Про сайт',
        'tables': list_tables,
    }
    word_document()
    return render(request, 'reports/about.html', context=context)
