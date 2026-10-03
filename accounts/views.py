from rest_framework.views import APIView
from rest_framework.views import Response

from .models import SignIn
from .Serializer import SignInSerializer

class Accounts(APIView):
    
    def post(self,request):

        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success":True
            },
            status=status.HTTP_201_CREATED
            )

            return Response({
                "Success":False
            },
            status=status.HTTP_400_BAD_REQUEST
            )



        

