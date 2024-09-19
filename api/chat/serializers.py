from rest_framework import serializers

class SubmitMessageSerializers(serializers.Serializer):

    sender = serializers.CharField(required=True)
    message = serializers.CharField(required=True)