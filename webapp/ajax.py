import json
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods

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
        data = {'message': webpageItem + " then python edited then string"}
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
		# earlier, ajax stored the element from webpage into ajax-item
        webpageItem = request.POST.get('ajax-item')
        print("The item from page has a value of: " + webpageItem)
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': webpageItem + " then python edited then string"}
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
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': webpageItem + " then python edited then string"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404