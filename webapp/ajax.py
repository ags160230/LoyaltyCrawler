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
        moved_node = request.POST.get('moved_node_name')
        target_node = request.POST.get('target_node_name')
        position = request.POST.get('position')
        previous_parent = request.POST.get('previous_parent_name')
		
		# test copy
        source = 'C:/GitHub/a/a1.txt'
        destination = 'C:/GitHub/a/a2.txt'
        copy_file(source, destination)		
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': moved_node + " then python edited the string"}
		
		# print data during debug mode before return
        if debugMode == True:
            print("moved_node_name: " + moved_node)
            print("target_node_name: " + target_node)
            print("position: " + position)
            print("previous_parent_name: " + previous_parent)
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
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['id'] = path
        #d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
        #d['parentid'] = os.path.abspath(os.path.join(path, os.pardir))
    #else:
        #d['type'] = "file"
    return d