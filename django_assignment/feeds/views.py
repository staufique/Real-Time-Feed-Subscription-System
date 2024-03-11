
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer,UserLoginSerializer,BinanceLiveFeedSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
import websockets
import asyncio

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }

class UserSignupView(APIView):
    def get(self,requuest):
        return Response("Signup Page")
    def post(self,request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response({'msg':'Register Successful'},status=status.HTTP_201_CREATED)
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserLoginView(APIView):
    def get(self,requuest):
        return Response("login")
    
    def post(self,request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            print(email,password)
            user = User.objects.filter(email=email,password=password).first()
            # user = authenticate(email=email,password=password)
            print(user)
            if user is not None :
                msg=''
                check = User.objects.filter(email=email).first()
                if check.channel_subscription:
                    channel_layer = get_channel_layer()
                    async_to_sync(channel_layer.group_add)("live_feeds", 'groups')
                else:
                    msg+="subscribe to live_feeds channel through this link http://localhost:8000/channel-subscription/"
                token = get_tokens_for_user(user)
                response = Response({"msg":msg,"token":token,"msg":"login success"},status=status.HTTP_200_OK)
                return response
            return Response({"errors":{"validation_erros":['password and email is not valid']}},status=status.HTTP_404_NOT_FOUND)


class ChannelSubscription(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        user.channel_subscription = True 
        user.save()
        return Response({"msg": "Channel subscription updated successfully."}, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):

        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token:
            RefreshToken(refresh_token).blacklist()
        response = Response({'msg': 'Logout Successful'}, status=status.HTTP_200_OK)
        response.delete_cookie('refresh-token')
        response.delete_cookie('access-token')
        return response

class LiveFeedAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    async def fetch_live_feed_data(self, uri):
        async with websockets.connect(uri) as websocket:
            while True:
                data = await websocket.recv()
                return data

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.channel_subscription:
            uri = "ws://localhost:8000/ws/live-feed/"
            live_feed_data = asyncio.run(self.fetch_live_feed_data(uri))
            serializer = BinanceLiveFeedSerializer({"data": live_feed_data})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("first subscribe to channel")