from django.urls import path

from .views import TODOListView, TODODetailView

urlpatterns = [
    path('<int:pk>/', TODODetailView.as_view()),
    path('', TODOListView.as_view()),
]