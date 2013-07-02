
from django.http import HttpResponse
import simplejson


def json_response(func):
    '''
    A decorator that takes a view response and generate JSON response.
    If callback is found in request response is JSONP.
    '''
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = simplejson.dumps(objects)
            if 'callback' in request.REQUEST:
                data = '%s(%s)' % (request.REQUEST['callback'], data)
                return HttpResponse(data, 'text/javascript')
        except:
            data = simplejson.dumps(str(objects))

            return HttpResponse(data, 'application/json')

    return decorator