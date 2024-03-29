from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
import json
from costumers.secured import costumersHandller


# Create your views here.

def add_costumer(request: HttpRequest):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body)
            if(costumersHandller.is_costumer_exists(data['email'])):
                return JsonResponse({'error': 'This email already in use'})
            res = costumersHandller.add_costumer(data['name'],data['email'],data['phone_number'])
            return JsonResponse({'message':'Costumer addedd successfully'},status = 200)
        except costumersHandller.EmailIsTakenExeption:
            return JsonResponse({'error':'This costumer already exist'},status = 400)
        except Exception as E:
            print(str(E))
            return JsonResponse({'error' :'Internal server error'},status = 500)

    else:
        return HttpResponseBadRequest({'error' :'Wrong request method'},status = 200)
 

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
