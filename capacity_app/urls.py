from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_request/', views.create_request, name='create_request'),
    path('view_request/', views.view_request, name='view_request'),
    path('update_request/<str:pk>', views.update_request, name='update_request'),
    path('history_request/<str:id>', views.history_request, name='history_request'),
    path('completed_ticket_data/', views.completeticketdata, name='completed_ticket_data'),
    path('completed_request/<str:pk>', views.completed_request, name='completed_request'),
    path('project_create_request/', views.project_create_request, name='project_create_request'),
    path('project_view_request/', views.project_view_request, name='project_view_request'),
    path('logout/', views.user_logout, name="logout")
]