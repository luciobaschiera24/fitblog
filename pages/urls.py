from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoutineListView.as_view(), name='routine_list'),
    path('<int:pk>/', views.RoutineDetailView.as_view(), name='routine_detail'),
    path('create/', views.routine_create, name='routine_create'),
    path('<int:pk>/update/', views.routine_update, name='routine_update'),
    path('<int:pk>/delete/', views.routine_delete, name='routine_delete'),
]
