from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, SignupSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    password = request.data.get('password')
    # password2 = request.data.get('password2')
    # if password != password2:
    #     return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid(raise_exception=True):
        # 비밀번호 해싱
        if serializer.validated_data.get('password') == serializer.validated_data.get('password2'):
            user = serializer.save()
            # print(user)
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    pass


@api_view(['GET'])
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializer(person)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = get_object_or_404(get_user_model(), pk=request.data['user_id'])

    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            is_followed = False
        else:
            person.followers.add(user)
            is_followed = True
        return Response(is_followed)