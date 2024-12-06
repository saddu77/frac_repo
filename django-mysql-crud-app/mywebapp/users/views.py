from django.shortcuts import render
from users.models import Users
from users.serializers import UsersSerializer
from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Django Cookies Demo</h2>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Django Cookies created ")
    else:
        response = HttpResponse("Django Cookies <br> your browser doesnot accept cookies")
    return response
    
# Create your views here.
@api_view(['GET','POST'])
def users_list(request):
    # Fetch All Records
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data, safe=False)
        
    # Creating new record (user)
    elif request.method == 'POST':  
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_data)

        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    # find record by id
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message':'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Fetch record(user) by id
    if request.method == 'GET':
         user_serializer = UsersSerializer(user)
         return JsonResponse(user_serializer.data)

    # update user by Id
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    # delete user by Id
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message':'User deleted Successfully'}, status = status.HTTP_204_NO_CONTENT)
        



