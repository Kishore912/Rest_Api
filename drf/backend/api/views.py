# from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import productSerializer

@api_view(["GET"])
def api_home(request,*args,**kwargs):


    # if request.method!="POST":
    #     return Response({                  # we dont need to specify all this instead everything is done by restframework
    #         "message":"POST not allowed"
    #     })




    # model_product = products.objects.all()
    # li = []
    # for data in model_product:
    #     di = {
    #         'id' : data.id,             # to get all the values from the models
    #         'title' : data.title,
    #         'content' : data.content,
    #         'price' : data.price
    #     }
    #     li.append(di)
    # return JsonResponse(li , safe=False)



    
    instance = products.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data['id'] = model_product.id
        # data['title'] = model_product.title           # we can do this entire step in a single line of code using model_to_dict
        # data['content'] = model_product.content
        # data['price'] = model_product.price
        # data = model_to_dict(model_product,fields=['id','title','price','sales_price'])
        data = productSerializer(instance).data

    return Response(data)      
          
  