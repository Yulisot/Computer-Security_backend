from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from costumers.unsecured import costumersHandller
import json
# Create your views here.

def add_costumer(request: HttpRequest):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)
            if(costumersHandller.is_costumer_exists(data['email'])):
                return JsonResponse({'error': 'This email already in use'})
            res = costumersHandller.add_costumer(data['name'],data['email'],data['phone_number'])
            return JsonResponse({'message':'Costumer addedd successfully'})
        except Exception as E:
            print(str(E))
            return JsonResponse({'error':str(E)},500)

    else:
        return JsonResponse({'error':'Wrong request method'})
 

def get_costumer(request: HttpRequest):
    if(request.method == 'GET'):
        try:
            res = costumersHandller.get_costumer(request.GET.get('email'))
            return JsonResponse({'message': json.dumps(res)})
        except Exception as E:
            print(str(E))
            return JsonResponse({'error':str(E)},500)

    else:
        return JsonResponse({'error':'Wrong request method'},status = 400)
 