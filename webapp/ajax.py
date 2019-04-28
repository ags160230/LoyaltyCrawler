import json
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods

# method for get request from ajax
@require_http_methods(["GET"])
def more_todo(request):
    print("called: more_todo")
    if request.is_ajax():
        todo_items = ['Mow Lawn', 'Buy Groceries',]
        data = json.dumps(todo_items)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
		
# method for post request from ajax
@require_http_methods(["POST"])	
def add_todo(request):
    print("called: add_todo")
    if request.is_ajax() and request.POST:
	    # this line allows python to retrive data from the text box
        webpageItem = request.POST.get('item')
        print("The item from page has a value of: " + webpageItem)
		# this shows python maniuplating the string before sending back to ajax
        data = {'message': webpageItem + " then python edited then string"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404