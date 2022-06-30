from django.urls import path

from .views import SignUpView, LocationDetailView, LocationCreateView, LocationUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('create', LocationCreateView.as_view(), name='create'),
    path('detail/<int:pk>', LocationDetailView.as_view(), name='detail'),
    path('update/<int:pk>', LocationUpdateView.as_view(),
         name='location_update_form'),
]
