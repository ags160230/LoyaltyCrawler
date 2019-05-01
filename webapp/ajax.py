import json
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from .file_operations import *
import os
from django.conf import settings

# get is used when you don't need to access the webpage elements
# post is used to access the webpage elements

# filtree get function for ajax
@require_http_methods(["POST"])
def filetree_move(request):

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
        move_file(source, destination)
		
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': "Python moved file: " + source + " to location: " + destination}
		

			
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
# filtree post function for ajax
@require_http_methods(["POST"])	
def filetree_post(request):

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