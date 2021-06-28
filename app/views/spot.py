from app.mixins import OnlyYourSpotMixin
from app.models import Spot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic


class Create(LoginRequiredMixin, generic.CreateView):
    template_name = 'app/spot/create.html'
    model = Spot
    success_url = reverse_lazy('app:spot_list')
    fields = ['title', 'text', 'prefecture', 'address', 'image', ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'app/spot/list.html'
    model = Spot

    def get_queryset(self):
        query = super().get_queryset()
        query = query.order_by('prefecture', 'created_at',)
        return query


class Detail(LoginRequiredMixin, generic.DetailView):
    template_name = 'app/spot/detail.html'
    model = Spot


class Update(OnlyYourSpotMixin, generic.UpdateView):
    template_name = 'app/spot/update.html'
    model = Spot
    success_url = reverse_lazy('app:spot_list')
    fields = ['title', 'text', 'prefecture', 'address', 'image', ]


class Delete(OnlyYourSpotMixin, generic.DeleteView):
    template_name = 'app/spot/delete.html'
    model = Spot
    success_url = reverse_lazy('app:spot_list')
