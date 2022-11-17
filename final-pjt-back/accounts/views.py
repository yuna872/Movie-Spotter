from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    password = request.data.get('password')
    # password2 = request.data.get('password2')

    # if password != password2:
    #     return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.is_valid(raise_exception=True):
        # 비밀번호 해싱
        if serializer.validated_data.get('password') == serializer.validated_data.get('password2'):
            user = serializer.save()
            print(user)
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    pass
