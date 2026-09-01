from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import RegisterSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    
    serializer_class = RegisterSerializer 

    def get(self, request):
        return Response(RegisterSerializer().data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "User created"}, status=status.HTTP_201_CREATED)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer 
    def get(self, request):
        return Response(RegisterSerializer().data)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {"detail": "ایمیل یا رمز عبور اشتباه است"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)



class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_object(self):
        return self.request.user
