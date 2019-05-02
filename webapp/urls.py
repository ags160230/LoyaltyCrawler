from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from . import ajax

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html')),
    path('session/<int:session_id>/', views.get_session, name='get_session'),
    path('artifact/<int:artifact_id>/', views.view_artifact, name='view_artifact'),
    path('criteria', views.get_search_criteria, name='get_search_criteria'),
    path('criteria/edit', views.edit_search_criteria, name='edit_search_criteria'),
    path('start/<int:search_criteria_id>/', views.start_session, name='start_session'),
    path('delete/<int:session_id>/', views.delete_session, name='delete_session'),
	path('ajax/filetree/post/', ajax.filetree_post, name='filetree_post'),
	path('ajax/filetree/move/', ajax.filetree_move, name='filetree_move'),
	path('ajax/filetree/delete/', ajax.filetree_delete, name='filetree_delete'),
	path('ajax/filetree/rename/', ajax.filetree_rename, name='filetree_rename'),
	path('ajax/filetree/create/', ajax.filetree_create, name='filetree_create'),
]

# As a final step, create a file inside your catalog folder called urls.py,
# and add the following text to define the (empty) imported urlpatterns.
# This is where we'll add our patterns as we build the application.
