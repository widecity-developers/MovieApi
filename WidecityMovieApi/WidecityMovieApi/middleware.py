from django.http import JsonResponse


class Authenticate(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if request.GET.get('key') == 'widecitymakesitsimple':
            response = self.get_response(request)
            return response
        else:
            return JsonResponse({'status':'failed','error':'invalid key'})