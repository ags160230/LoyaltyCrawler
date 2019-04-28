import json
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from .file_operations import *
import os

# demo get function for ajax
# get is used when you don't need data from the webpage
@require_http_methods(["GET"])
def demo_get(request):
    print("called: demo_get")
    if request.is_ajax():
        todo_items = ['Mow Lawn', 'Buy Groceries',]
        data = json.dumps(todo_items)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
		
# demo post function for ajax
# post is used to access the webpage elements
@require_http_methods(["POST"])	
def demo_post(request):
    print("called: demo_post")
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into ajax-item
        webpageItem = request.POST.get('ajax-item')
        print("The item from page has a value of: " + webpageItem)
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': webpageItem + " then python edited the string"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
# filtree get function for ajax
@require_http_methods(["GET"])
def filetree_get(request):
    print("called: filetree_get")
    if request.is_ajax():
        todo_items = ['Child1', 'Child2',]
        data = json.dumps(todo_items)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
		
# filtree get function for ajax
@require_http_methods(["POST"])
def filetree_move(request):
    print("called: filetree_move")
    print(request)
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into the single quoted parts of the POST request
        moved_node = request.POST.get('moved_node_name')
        target_node = request.POST.get('target_node_name')
        position = request.POST.get('position')
        previous_parent = request.POST.get('previous_parent_name')
		
        print("moved_node_name: " + moved_node)
        print("target_node_name: " + target_node)
        print("position: " + position)
        print("previous_parent_name: " + previous_parent)
		# test copy
        source = 'C:/GitHub/a/a1.txt'
        destination = 'C:/GitHub/a/a2.txt'
        copy_file(source, destination)		
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': moved_node + " then python edited the string"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
# filtree post function for ajax
@require_http_methods(["POST"])	
def filetree_post(request):
    print("called: filetree_post")
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from ajax
		# earlier, ajax stored the element from webpage into ajax-item
        webpageItem = request.POST.get('ajax-file-tree-root')
        print("The item from page has a value of: " + webpageItem)
        directory = 'C:/GitHub/a'
        dir_nodes = []
        file_nodes = []
        # walk through directory
        for root, directories, filenames in os.walk(directory):
            dir_nodes.append(root)
            #for directory in directories:
                #print(os.path.join(root, directory))
            dir_nodes.append(directories)
            #for filename in filenames:
                #print(os.path.join(root,filename))
            file_nodes.append(filenames)
		# this shows python maniuplating the string before sending back to ajax
        root = 'C:/GitHub/a'
        trim = root
        trimed_dirs = [root]
        trimed_nested = ""
        trimed_dirs = (recur_get_dir (root, trim, trimed_dirs, trimed_nested))
        print(trimed_dirs)
        json_str = json.dumps(trimed_dirs)
        print(json_str)
        #json_str = json.dumps(dir_nodes)
        #print(json_str)
        data = {
					'directories': trimed_dirs,
					'files': file_nodes,
				}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		
def recur_get_dir (root, trim, trimed_dirs, trimed_nested):
    trimed_nested = ""
    dirs = os.listdir(root)
	#print(root)
    #print(dirs)
    for dir in dirs:
        full_path = os.path.join(root, dir)
        trimed_dir = dir
        if (os.path.isdir(full_path)):
            nested_dirs = os.listdir(full_path)
            if len(nested_dirs) != 0:
                trim = full_path
                root = full_path
				# recuversive call to start processes next level
                for nested_dir in nested_dirs:
                    full_nested_path = os.path.join(root, nested_dir)
                    root = full_nested_path
                    root = full_nested_path
                    trimed_nested = ["name:", nested_dir]
                    recur_get_dir(root, trim, trimed_dirs, trimed_nested)
				# add nested tuple that represents entire nested level after recursion
                nested_tuple = [["name: ", trimed_dir], ["children:", trimed_nested]]
                trimed_dirs.append(nested_tuple)
				# clear trimed_nested list
                trimed_nested = []
			# add single dir to trimmed
            else:
                trimed_dirs.append(["name: ", trimed_dir])
		# add file to trimed
        else:
            trimed_dirs.append(["name: " , trimed_dir])
    # end of dirs at current level
    return trimed_dirs
    