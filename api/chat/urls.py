from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from api.chat.views import SubmitChatMessageView

class HelloView(APIView):

    def get(self, request):
        return Response(data={
            'hello': 'world'
        })
    

urlpatterns = [
    path('hello', HelloView.as_view(), name='hello.world'),
    path('message', SubmitChatMessageView.as_view(), name='submit.message'),
]