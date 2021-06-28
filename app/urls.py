from django.urls import path

from app.views import review, spot, user

app_name = 'app'

urlpatterns = [
    path('', user.Login.as_view(), name='user_login'),

    path('user/', user.List.as_view(), name='user_list'),
    path('user/create/', user.Create.as_view(), name='user_create'),
    path('user/<int:pk>/', user.Detail.as_view(), name='user_detail'),
    path('user/<int:pk>/update/', user.Update.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', user.Delete.as_view(), name='user_delete'),

    path('spot/', spot.List.as_view(), name='spot_list'),
    path('spot/create/', spot.Create.as_view(), name='spot_create'),
    path('spot/<int:pk>/', spot.Detail.as_view(), name='spot_detail'),
    path('spot/<int:pk>/update/', spot.Update.as_view(), name='spot_update'),
    path('spot/<int:pk>/delete/', spot.Delete.as_view(), name='spot_delete'),

    path('review/', review.List.as_view(), name='review_list'),
    path('review/create/<int:spot_pk>/',
         review.Create.as_view(), name='review_create'),
    path('review/<int:pk>/', review.Detail.as_view(), name='review_detail'),
    path('review/<int:pk>/update/', review.Update.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', review.Delete.as_view(), name='review_delete'),
]
