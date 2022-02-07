from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_request/', views.create_request, name='create_request'),
    path('view_request/', views.view_request, name='view_request'),
    path('update_request/<int:pk>', views.update_request, name='update_request'),
    path('history_request/<str:id>', views.history_request, name='history_request'),
    path('completed_ticket_data/', views.completeticketdata, name='completed_ticket_data'),
    path('completed_request/<int:pk>', views.completed_request, name='completed_request')
]