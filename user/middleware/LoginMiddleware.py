from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from user.views import UserLoginApiview
from django.shortcuts import redirect

class ShowTodayOrdersMiddleware(MiddlewareMixin):

    flag = False

    def process_request(self, request):
        ShowTodayOrdersMiddleware.flag = False
        print("in process_request")
        if request.user.is_staff:
            print("*******",request.user)
            print("in is__staff if")
            ShowTodayOrdersMiddleware.flag = True
    
    def process_view(self, request, func, args, kwargs):
        print("in process_view") 
        print(" ###### ",request.META['REMOTE_USER'])
        if func == UserLoginApiview and request.user.is_staff:
            print(" ###### ",request.META['REMOTE_USER'])
            print(" &&&&&& ", request.user)
            print("in func if")
            return redirect('/finance/show_today_orders')
    
    def process_response(self, request, response):
        print("in process_response")
        return response
    
