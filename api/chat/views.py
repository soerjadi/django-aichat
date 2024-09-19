from openai import OpenAI
from rest_framework import generics
from rest_framework.response import Response
from api.chat.serializers import SubmitMessageSerializers
import os

class SubmitChatMessageView(generics.CreateAPIView):
    serializer_class = SubmitMessageSerializers

    def post(self, request, *args, **kwargs):
        serializer = SubmitMessageSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        client = OpenAI(
            organization=os.getenv('OPENAI_ORG'),
            project=os.getenv('OPENAI_PROJECT'),
            api_key=os.getenv('OPENAI_API_KEY')
        )

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": data['message']}
            ]
        )

        response = completion.choices[0].message.content
        
        # Return JSON response
        result = {'response': response}

        return Response(data=result)