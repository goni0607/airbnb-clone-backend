from django.http import JsonResponse
from .models import Category


def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'ok': True, 'categories': categories, })
