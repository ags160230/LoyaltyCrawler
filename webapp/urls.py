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
	path('ajax/filetree/get/', ajax.filetree_get, name='filetree_get'),
	path('ajax/filetree/post/', ajax.filetree_post, name='filetree_post'),
	path('ajax/filetree/move/', ajax.filetree_move, name='filetree_move'),
	# simple demonstrations of get and post from page
	path('ajax/demo/get/', ajax.demo_get, name='demo_get'),
	path('ajax/demo/post/', ajax.demo_post, name='demo_post'),
]

# As a final step, create a file inside your catalog folder called urls.py,
# and add the following text to define the (empty) imported urlpatterns.
# This is where we'll add our patterns as we build the application.
