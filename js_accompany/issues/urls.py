from django.urls import path

from . import views


app_name = 'issues'
urlpatterns = [
    path('', views.IssueListView.as_view(), name='issue-list'),
    path('<int:pk>/', views.IssueDetailView.as_view(), name='issue-detail'),
    path('new/', views.create_issue, name='create-issue'),
    path('save/', views.save_issue, name='save-issue'),
    path('add-message/<int:issue_pk>', views.add_message, name='add-message'),
]