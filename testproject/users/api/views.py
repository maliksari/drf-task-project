import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializer import RegisterSerializer

CLIENT_ID = 'XUh5Ml6oJPi5JMqcs0qGW9XeyVi41lEy9KVSDNYf'
CLIENT_SECRET = 'etpWoSVpn12oWiMCbvfiBa2oPPSg5FoLm5Cgajj41nXgw4C8VTdDMHp4uwpTarO4QDZVtzyqX231Ji7AJjg96oYeEOFwV9LVFnTF18Dhw8DAz7mwCRC5QzvgHLVPAJfW'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post('http://127.0.0.1:8000/oauth2/token/',
                          data={
                              'grant_type': 'client_credentials',
                              'email': request.data['email'],
                              'password': request.data['password'],
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    r = requests.post('http://127.0.0.1:8000/oauth2/token/',
                      data={
                          'grant_type': 'client_credentials',
                          'email': request.data['email'],
                          'password': request.data['password'],
                          'client_id': CLIENT_ID,
                          'client_secret': CLIENT_SECRET,
                      },
                      )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post('http://127.0.0.1:8000/oauth2/token/',
                      data={
                          'grant_type': 'refresh_token',
                          'refresh_token': request.data['refresh_token'],
                          'client_id': CLIENT_ID,
                          'client_secret': CLIENT_SECRET,
                      },
                      )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    print("*****", request.data)
    r = requests.post('http://127.0.0.1:8000/oauth2/revoke_token/',
                      data={
                          'token': request.data['token'],
                          'client_id': CLIENT_ID,
                          'client_secret': CLIENT_SECRET,
                      },
                      )
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    return Response(r.json(), r.status_code)
