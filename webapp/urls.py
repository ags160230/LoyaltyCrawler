from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html')),
    path('session/<int:session_id>/', views.get_session, name='get_session'),
    path('artifact/<int:artifact_id>/', views.view_artifact, name='view_artifact'),
    path('criteria', views.get_search_criteria, name='get_search_criteria'),
    path('criteria/edit', views.edit_search_criteria, name='get_search_criteria'),
]

# As a final step, create a file inside your catalog folder called urls.py,
# and add the following text to define the (empty) imported urlpatterns.
# This is where we'll add our patterns as we build the application.