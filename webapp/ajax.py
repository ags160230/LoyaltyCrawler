import json
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_http_methods

# Page that returns search criteria list
@require_http_methods(["GET", "POST"])
def more_todo(request):
    if request.is_ajax():
        todo_items = ['Mow Lawn', 'Buy Groceries',]
        data = json.dumps(todo_items)
        return HttpResponse(data, content_type='application/json')
    else:
        console.log('more todo called')
        raise Http404
