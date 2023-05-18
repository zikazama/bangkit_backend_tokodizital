import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated   

from applibs.response import prepare_success_response, prepare_error_response
from authentication.models import AuthUser
from authentication.serializers.user_serializer import LoginSerializer, RegisterSerializer
from authentication.serializers.profile_serializer import ProfileSerializer

logger = logging.getLogger('general')


class UserRegistration(APIView):
    def __init__(self):
        super(UserRegistration, self).__init__()
        self.register_serializer = RegisterSerializer

    def post(self, request):
        register_serializer = self.register_serializer(data=request.data)
        if register_serializer.is_valid():
            password = register_serializer.validated_data.pop('password')
            user = AuthUser.objects.create_user(password=password,
                                         **register_serializer.validated_data)

            return Response(prepare_success_response(data=self.register_serializer(user).data),
                            status.HTTP_200_OK)

        return Response(prepare_error_response(register_serializer.errors),
                        status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def __init__(self):
        super(UserLogin, self).__init__()

        self.login_serializer = LoginSerializer

    def post(self, request):
        login_serializer = self.login_serializer(data=request.data)
        if login_serializer.is_valid():
            serializer_data = login_serializer.validated_data
            return Response(prepare_success_response(serializer_data), status.HTTP_200_OK)

        return Response(prepare_error_response(login_serializer.errors),
                        status.HTTP_400_BAD_REQUEST)

class EditProfile(APIView):

    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(EditProfile, self).__init__()
        self.serializer = ProfileSerializer

    def put(self, request):
        serializer = self.serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = request.user

            update_user = AuthUser.objects.update_user(old_phone_number=user.phone_number, **serializer.validated_data)
            return Response(prepare_success_response(data=self.serializer(update_user).data), status.HTTP_200_OK)

        except Exception as ex:
            logger.error(ex)
            return Response(prepare_error_response("The phone number or email is already taken"), status=status.HTTP_400_BAD_REQUEST)
