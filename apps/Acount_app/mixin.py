from django.shortcuts import redirect
class RedirectLogin:

    def dispatch(self,request):

        if request.user.is_authenticated:
            return redirect("Home:Home")

        else:
            return super(RedirectLogin, self).dispatch(request)

class CheckLogin:
    def dispatch(self,request,*args,**kwargs):

        if request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)
        else:
            return redirect("Home:Home")