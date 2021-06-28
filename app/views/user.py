from django.urls.base import reverse
from app.forms import MyLoginForm, MyUserChangeForm, MyUserCreationForm
from django.contrib.auth import authenticate, get_user_model, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()


class Create(generic.CreateView):
    template_name = 'app/user/create.html'
    model = User
    form_class = MyUserCreationForm
    success_url = reverse_lazy('app:spot_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        un = form.cleaned_data.get('username')
        pw = form.cleaned_data.get('password1')
        user = authenticate(username=un, password=pw)
        login(self.request, user)
        return response


class List(generic.ListView):
    template_name = 'app/user/list.html'
    model = User


class Detail(generic.DetailView):
    template_name = 'app/user/detail.html'
    model = User


class Update(generic.UpdateView):
    template_name = 'app/user/update.html'
    model = User
    form_class = MyUserChangeForm
    success_url = reverse_lazy('app:spot_list')

    def get_success_url(self):
        kw = {'pk': self.kwargs['pk'], }
        return reverse_lazy('app:user_detail', kwargs=kw)


class Delete(generic.DeleteView):
    template_name = 'app/user/delete.html'
    model = User
    success_url = reverse_lazy('login')


class Login(generic.FormView):
    template_name = 'app/user/login.html'
    form_class = MyLoginForm
    success_url = reverse_lazy('app:spot_list')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('app:spot_list'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        em = self.request.POST['email']
        pw = self.request.POST['password']

        if not User.objects.filter(email=em).exists():
            return HttpResponseRedirect(reverse_lazy('app:user_login'))

        un = User.objects.get(email=em).username
        user = authenticate(username=un, password=pw)
        if not user:
            return HttpResponseRedirect(reverse_lazy('app:user_login'))

        login(self.request, user)
        return super().form_valid(form)
