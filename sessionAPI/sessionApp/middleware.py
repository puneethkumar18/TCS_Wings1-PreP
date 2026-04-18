class MiddleWareLifeCycle:
    def __init__(self,get_response):
        print("MiddleWare Init")
        self.get_response = get_response

    def __call__(self,request):
        print("Before the view or next middleare runs and gets response")
        result = self.get_response(request)
        print("After the view or next middleare runs and gets response")
        return result
    
from django.http import HttpResponse
class ExceptionHandlingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        return self.get_response(request)
    

    def process_exception(self,request,exception):
        print(exception)
        return HttpResponse(exception)