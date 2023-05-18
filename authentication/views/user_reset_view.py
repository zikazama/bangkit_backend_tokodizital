import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated   

from applibs.response import prepare_success_response, prepare_error_response
from authentication.models import AuthUser
from authentication.serializers.password_serializer import ResetPasswordSerializer

logger = logging.getLogger('general')


class ResetPassword(APIView):
    
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(ResetPassword, self).__init__()
        self.serializer = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = request.user
            password = serializer.validated_data['password']

            AuthUser.objects.reset_password(phone_number=user.phone_number, password=password)
            return Response(prepare_success_response(), status.HTTP_200_OK)

        except Exception as ex:
            logger.error(ex)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
