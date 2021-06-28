from app.mixins import OnlyYourReviewMixin
from app.models import Review, Spot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic


class Create(LoginRequiredMixin, generic.CreateView):
    template_name = 'app/review/create.html'
    model = Review
    success_url = reverse_lazy('app:spot_list')
    fields = ['star', ]

    def get(self, request, *args, **kwargs):
        spot__pk = self.kwargs['spot_pk']
        user = self.request.user
        review_list = Review.objects.filter(spot__pk=spot__pk, user=user)
        if review_list.count() > 0:
            return HttpResponseRedirect(reverse_lazy('app:spot_list'))

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        spot = Spot.objects.get(pk=self.kwargs['spot_pk'])

        form.instance.spot = spot
        form.instance.user = self.request.user
        return super().form_valid(form)


class List(LoginRequiredMixin, generic.ListView):
    template_name = 'app/review/list.html'
    model = Review


class Detail(OnlyYourReviewMixin, generic.DetailView):
    template_name = 'app/review/detail.html'
    model = Review


class Update(OnlyYourReviewMixin, generic.UpdateView):
    template_name = 'app/review/update.html'
    model = Review
    fields = ['star', ]

    def get_success_url(self):
        kw = {'pk': self.kwargs['pk']}
        return reverse_lazy('app:review_detail', kwargs=kw)


class Delete(OnlyYourReviewMixin, generic.DeleteView):
    template_name = 'app/review/delete.html'
    model = Review
    success_url = reverse_lazy('app:review_list')
