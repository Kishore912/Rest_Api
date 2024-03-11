from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import products
def api_home(request,*args,**kwargs):

    # model_product = products.objects.all()
    # li = []
    # for data in model_product:
    #     di = {
    #         'id' : data.id,                                     # to get all the values from the models
    #         'title' : data.title,
    #         'content' : data.content,
    #         'price' : data.price
    #     }
    #     li.append(di)
    # return JsonResponse(li , safe=False)

    model_product = products.objects.all().order_by("?").first()
    data = {}
    if model_product:
        # data['id'] = model_product.id
        # data['title'] = model_product.title           # we can do this entire step in a single line of code using model_to_dict
        # data['content'] = model_product.content
        # data['price'] = model_product.price
        data = model_to_dict(model_product,fields=['id','title'])

    return JsonResponse(data)      
          
  