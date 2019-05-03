from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from . import ajax

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html')),
    path('get_session/<int:session_id>/', views.get_session, name='get_session'),
    path('artifact/<int:artifact_id>/', views.view_artifact, name='view_artifact'),
    path('criteria', views.get_search_criteria, name='get_search_criteria'),
    path('criteria/add/<str:new_criterion>/', views.add_search_criteria, name='add_search_criteria'),
    path('criteria/remove/<str:criterion_to_remove>/', views.remove_search_criteria, name='remove_search_criteria'),
    path('start_session/', views.start_session, name='start_session'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
    path('check_last_session_index/', views.check_last_session_index, name='check_last_session_index'),
	path('ajax/filetree/post_tree/', ajax.filetree_post_tree, name='filetree_post_tree'),
	path('ajax/filetree/move_node/', ajax.filetree_move_node, name='filetree_move_node'),
	path('ajax/filetree/delete_node/', ajax.filetree_delete_node, name='filetree_delete_node'),
	path('ajax/filetree/rename_node/', ajax.filetree_rename_node, name='filetree_rename_node'),
	path('ajax/filetree/create_node/', ajax.filetree_create_node, name='filetree_create_node'),
	path('ajax/filetree/copy_node/', ajax.filetree_copy_node, name='filetree_copy_node'),
]

# As a final step, create a file inside your catalog folder called urls.py,
# and add the following text to define the (empty) imported urlpatterns.
# This is where we'll add our patterns as we build the application.
