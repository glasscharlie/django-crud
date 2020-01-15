from utensils.views import HomePageView, UtensilsDetailView, UtensilsCreateView, UtensilsUpdateView, DeleteUpdateView
from django.urls import path

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', UtensilsDetailView.as_view(), name='detail'),
    path('new/', UtensilsCreateView.as_view(), name='utensils_new'),
    path('update/<int:pk>', UtensilsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteUpdateView.as_view(), name='delete'),
]