# from django.core import serializers
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category


@api_view()
def categories(request):
    return Response(
        {
            "ok": True,
        }
    )
    # categories = Category.objects.all()
    # json_data = serializers.serialize("json", categories)
    # return JsonResponse({'ok': True, 'categories': json_data, })
