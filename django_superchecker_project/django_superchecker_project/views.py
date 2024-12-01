from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from .scrape import scrape_all

from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate



        
@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


@api_view(['POST', 'GET'])
def loginUser(request):
    # uName = request["user"]
    # password = request.form["password"]
    print(request.data)
    print("We talking")

    new_user_info = request.data

    print(new_user_info["email"])


    try: 
        print("yo")
        user = User.objects.create_user(username=new_user_info["email"], email=new_user_info["email"], password=new_user_info["password"], first_name=new_user_info["fName"], last_name=new_user_info["lName"])
        print("yo")
        user.save()
        print("yo")
        resp_data = {'Result': 'Useradded'}
        return JsonResponse(resp_data)
    except:
        print("failed")
        resp_data = {'Result': 'User not added'}
        return JsonResponse(resp_data)
    
@api_view(['POST','GET'])
def sign_in(request):

    print(request.data)

    attempt=request.data

    user = authenticate(username=attempt["email"], password=attempt["password"])
    if user is not None:
        resp_data = {'Result': 'User Exists', 'fName' : user.first_name, 'userName' : user.username}
        return JsonResponse(resp_data)
        
    else:
        resp_data = {'Result': 'User Does not Exist'}
        return JsonResponse(resp_data)
        
        

    

@api_view(['GET'])
def scrape(request):
    scrape_all()
    data = {"data": "yay"}
    return Response(data)
    