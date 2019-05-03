import json
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from .file_operations import *
from .folder_operations import *
import os
from django.conf import settings

# get is used when you don't need to access the webpage elements
# post is used to access the webpage elements

# filtree post function for ajax
# move file or folder node
@require_http_methods(["POST"])
def filetree_create_node(request):

	# determine if we are in debug mode for print statements and sanity checks
    debugMode = settings.DEBUG
	
	# print that this function was called
    if debugMode == True:
        print("called: filetree_create")
        print(request)
		
	# logic for handling request	
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into the single quoted parts of the POST request
        moved_node_id = request.POST.get('my_jq_tree_moved_node_id')
        target_node_id = request.POST.get('my_jq_tree_target_node_id')
        position = request.POST.get('my_jq_tree_position')
        previous_parent_id = request.POST.get('my_jq_tree_previous_parent_id')
		
		# print data during debug mode before move
        if debugMode == True:
            print("moved_node_id: " + moved_node_id)
            print("target_node_id: " + target_node_id)
            print("position: " + position)
			
		# do the move
        source = moved_node_id
        destination = target_node_id
		# this will work for directories as well as files
        create_file(source, destination)
		
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': "Python created file: " + source}
		

			
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		

# filtree post function for ajax
# copy file or folder node
@require_http_methods(["POST"])
def filetree_copy_node(request):

	# determine if we are in debug mode for print statements and sanity checks
    debugMode = settings.DEBUG
	
	# print that this function was called
    if debugMode == True:
        print("called: filetree_rename")
        print(request)
		
	# logic for handling request	
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into the single quoted parts of the POST request
        copied_node_id = request.POST.get('my_jq_tree_copied_node_id')
        copied_node_type = request.POST.get('my_jq_tree_copied_node_type')
        parent_node_id = request.POST.get('my_jq_tree_parent_node_id')
        new_name = request.POST.get('my_jq_tree_new_name')
		
		# print data during debug mode before move
        if debugMode == True:
            print("copied_node_id: " + copied_node_id)
            print("copied_node_type: " + copied_node_type)
            print("parent_node_id: " + parent_node_id)
            print("new_name: " + new_name)
			
		# do the rename
        source = copied_node_id
        destination = parent_node_id + os.sep + new_name
		# this will work for directories as well as files
        if copied_node_type == 'directory':
            copy_folder(source, destination)
        elif copied_node_type == 'file':
            copy_file(source, destination)

		# this shows python maniuplating the string before sending back to ajax
        data = 	{
					'message': "Python copied file: " + source + " with new name: " + new_name,
                    'new_node_id': destination
				}
			
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
		
# filtree post function for ajax
# delete file or folder node
@require_http_methods(["POST"])
def filetree_delete_node(request):

	# determine if we are in debug mode for print statements and sanity checks
    debugMode = settings.DEBUG
	
	# print that this function was called
    if debugMode == True:
        print("called: filetree_delete")
        print(request)
		
	# logic for handling request	
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into the single quoted parts of the POST request
        deleted_node_id = request.POST.get('my_jq_tree_deleted_node_id')

		# print data during debug mode before move
        if debugMode == True:
            print("deleted_node_id: " + deleted_node_id)
			
		# do the move
        source = deleted_node_id
		# this will work for files as well as directories
        delete_folder(source)
		
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': "Python deleted file: " + source}
		

			
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
# filtree post function for ajax
# move file or folder node
@require_http_methods(["POST"])
def filetree_rename_node(request):

	# determine if we are in debug mode for print statements and sanity checks
    debugMode = settings.DEBUG
	
	# print that this function was called
    if debugMode == True:
        print("called: filetree_rename")
        print(request)
		
	# logic for handling request	
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into the single quoted parts of the POST request
        renamed_node_id = request.POST.get('my_jq_tree_renamed_node_id')
        parent_node_id = request.POST.get('my_jq_tree_parent_node_id')
        new_name = request.POST.get('my_jq_tree_new_name')
		
		# print data during debug mode before move
        if debugMode == True:
            print("renamed_node_id: " + renamed_node_id)
            print("parent_node_id: " + parent_node_id)
            print("new_name: " + new_name)
			
		# do the rename
        source = renamed_node_id
        destination = parent_node_id + os.sep + new_name
		# this will work for directories as well as files
        rename_file(source, destination)
		
		# this shows python maniuplating the string before sending back to ajax
        data = 	{
					'message': "Python renamed file: " + source + " to: " + destination,
					'new_node_id': destination
				}
			
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404

		
# filtree post function for ajax
# move file or folder node
@require_http_methods(["POST"])
def filetree_move_node(request):

	# determine if we are in debug mode for print statements and sanity checks
    debugMode = settings.DEBUG
	
	# print that this function was called
    if debugMode == True:
        print("called: filetree_move")
        print(request)
		
	# logic for handling request	
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into the single quoted parts of the POST request
        moved_node_id = request.POST.get('my_jq_tree_moved_node_id')
        target_node_id = request.POST.get('my_jq_tree_target_node_id')
        position = request.POST.get('my_jq_tree_position')
        previous_parent_id = request.POST.get('my_jq_tree_previous_parent_id')
		
		# print data during debug mode before move
        if debugMode == True:
            print("moved_node_id: " + moved_node_id)
            print("target_node_id: " + target_node_id)
            print("position: " + position)
			
		# do the move
        source = moved_node_id
        destination = target_node_id
		# this will work for directories as well as files
        move_file(source, destination)
		
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': "Python moved file: " + source + " to location: " + destination}
		

			
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
# filtree post function for ajax
# post file tree to page
@require_http_methods(["POST"])	
def filetree_post_tree(request):

	# determine if we are in debug mode for print statements and sanity checks
    debugMode = settings.DEBUG
	
	# print that this function was called
    if debugMode == True:
        print("called: filetree_post")
        print(request)
		
	# logic for handling request	
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from my.ajax.py
		# earlier, ajax stored the element from webpage into my-ajax-file-tree-root
        webpageItemFromAJAX = request.POST.get('my-ajax-file-tree-root')
        directory = webpageItemFromAJAX
		# create root_dictionary on the starting_node
        root_dictionary = path_to_dict(directory)
		# get the children nodes from the root node
        children_dictionary = root_dictionary.get('children')
		# convert dictionary to JSON string
        json_string_children = json.dumps(children_dictionary)
		# convert JSON string to JSON object
        json_children = json.loads(json_string_children)
        data =  {
					'tree_data': json_children,
				}
		# print data during debug mode before return
        if debugMode == True:
            print("The item from page, which was stored to ajax, has a value of: ")
            print(webpageItemFromAJAX)
            print("The dictionary's children from the root node are: ")
            print(children_dictionary)	
		# return data item, as formated above, with HttpResponse
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		

# function to create a dictionary object from a specified path
# this data must be in the format that jqtree can understand
# the object must be a dictionary which will be transformed into a JSON object by pthon later
# ---------------------------------------------------------------------------------------------
# there are no required fields for jqtree
# you can also add more fields if your functions need them later on
# name = basename of directory or file
# id = absolute path of directory or file
# children = all children ids inside this id
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    d['id'] = path
    if os.path.isdir(path):
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
        d['type'] = "directory"
        #d['parentid'] = os.path.abspath(os.path.join(path, os.pardir))
    else:
        d['type'] = "file"
    return d