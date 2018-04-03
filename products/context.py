from .models import Category,SubCategory

def category(request):
    categories=Category.objects.filter(is_main=True)
    subcategories=dict()
    for cgr in categories:
        sub = SubCategory.objects.filter(category=cgr)
        subcategories[cgr]=list(sub)

    return {'CATEGORIES':categories,'SUBCATEGORIES':subcategories}

