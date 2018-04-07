from django.template.context_processors import csrf
def setPage(request):
    if request.user.is_authenticated:
        base_page = 'base.html'
    else:
        base_page= 'base_visitor.html'
    return {'base_page':base_page}

def searchform(request):
    c={}
    c.update(csrf(request))
    return c