from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):

    def get(self, request):
        return Response(data={
            'hello': 'world'
        })
    

urlpatterns = [
    path('hello', HelloView.as_view(), name='hello.world'),
    path('chat/', include('api.chat.urls')),
]