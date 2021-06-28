from django.contrib.auth.mixins import UserPassesTestMixin

from app.models import Spot, Review


class OnlyYourSpotMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        spot = Spot.objects.get(pk=self.kwargs['pk'])
        return self.request.user == spot.user


class OnlyYourReviewMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        review = Review.objects.get(pk=self.kwargs['pk'])
        return self.request.user == review.user
