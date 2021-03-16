import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from mmsapi.models import MMSUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user
    Method arguments:
      request -- The full HTTP request object
    '''
    req_body = json.loads(request.body.decode('utf-8'))

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            mmsuser = MMSUser.objects.get(user_id=authenticated_user)
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key, "user_id": mmsuser.id})
            return HttpResponse(data, content_type='application/json')

        data = json.dumps({"valid": False})
        return HttpResponse(data, content_type='application/json')


@csrf_exempt
@api_view(['POST', ])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode('utf-8'))

    try:
        user = User.objects.get(username=req_body["username"])
        content = {'Username Already Exists'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    except User.DoesNotExist: 
        new_user = User.objects.create_user(
            username=req_body['username'],
            email=req_body['email'],
            password=req_body['password'],
            first_name=req_body['first_name'],
            last_name=req_body['last_name'],
        )

        mmsuser = MMSUser.objects.create(
            bio=req_body['bio'],
            profile_image_url=req_body["profile_image_url"],
            user_id=new_user,
            user_type= 1
        )

        # Commit the user to the database by saving it
        mmsuser.save()

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=new_user)

        # Return the token to the client
        data = json.dumps({"valid": True, "token": token.key, "user_id": mmsuser.id})
        return HttpResponse(data, content_type='application/json')
