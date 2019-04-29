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
        starting_node = 'C:\\GitHub\\a'
        current_node = starting_node
        trimed_dirs = [["name: ", starting_node]]
        trimed_nested = []
        #trimed_dirs = recur_get_dir(current_node, starting_node, trimed_dirs, trimed_nested)
        #list_files(starting_node)
        #roots = get_roots(starting_node)
        #formated_roots = format_roots(roots)
        #print(formated_roots)
        json_roots = json.dumps(path_to_dict(starting_node))
        print(json_roots)
		# print(trimed_dirs)
        # json_str = json.dumps(trimed_dirs)
        # print(json_str)
        #json_str = json.dumps(dir_nodes)
        #print(json_str)
        data =  {
					'tree_data': json_roots,
				}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
		


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
        d['parentid'] = os.path.abspath(os.path.join(path, os.pardir))
        d['id'] = path
    else:
        d['type'] = "file"
    return d



def format_roots(roots):	
    i = 0
    tree_data = ["name:" , roots[0]]
    while i < len(roots): 
        tree_data.append(["name:" , roots[i][0]])
        i += 1
    return tree_data
	
def get_roots(path):
    roots = []
    for root,d_names,f_names in os.walk(path):
	    roots.append([root, f_names])
    return roots
		
def recur_get_dir (current_node, starting_node, trimed_dirs, trimed_nested):
    
    dirs = os.listdir(current_node)
    print(dirs)
    for dir in dirs:
        full_path = os.path.join(current_node, dir)
        trimed_dir = dir
        if (os.path.isdir(full_path)):
            nested_dirs = os.listdir(full_path)
            if len(nested_dirs) > 0:
                nested_dir = nested_dirs[0]
                starting_node = os.path.join(current_node, dir) 
                current_node = os.path.join(full_path, nested_dir)
                trimed_nested.append(["name:", nested_dir])
                print("Nested: " + nested_dir)
                recur_get_dir(current_node, starting_node, trimed_dirs, trimed_nested)
				# recuversive call to start processes next level
                # for nested_dir in nested_dirs:
                    # print("nested:" + nested_dir)
                    # full_nested_path = os.path.join(current_node, nested_dir)
                    # print("nested path:" + full_nested_path)
                    # current_node =  full_nested_path
                    # trimed_nested.append(["name:", nested_dir])
                    # recur_get_dir(current_node, starting_node, trimed_dirs, trimed_nested)
				# # add nested tuple that represents entire nested level after recursion
                # nested_tuple = [["name: ", trimed_dir], ["children:", trimed_nested]]
                # trimed_dirs.append(nested_tuple)
				# # clear trimed_nested list
                # trimed_nested = []
			# # add single dir to trimmed
            else:
				# add nested tuple that represents entire nested level after recursion
                nested_tuple = [["name: ", current_node], ["children:", trimed_nested]]
                #trimed_dirs.append(["name: ", trimed_dir])
                trimed_dirs.append(nested_tuple)
		# add file to trimed
        else:
			# add nested tuple that represents entire nested level after recursion
            nested_tuple = [["name: ", current_node], ["children:", trimed_nested]]
            trimed_dirs.append(nested_tuple)
    # end of dirs at current level
    return trimed_dirs
    
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        previous_indent = ' ' * 4 * (level - 1)
        print('{}{}{},'.format(indent, "{name: ", "'"+os.path.basename(root)+"'"))
        if len(os.listdir(root)) > 0:
            print('{}{}'.format(indent, "children: ["))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}{},'.format(subindent, "{name: ",  "'"+f+"'}"))
        #if len(os.listdir(root)) > 0:
            #print('{}{}'.format(indent, "]"))
            #print('{}{}'.format(indent, "}"))	
    #print('{}'.format("}"))