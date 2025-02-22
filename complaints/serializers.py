# submissions/serializers.py
from rest_framework import serializers
from .models import Submission, Document

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'site', 'name','email','address','message', 'created_at']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'uploaded_at', 'processed']

class QuerySerializer(serializers.Serializer):
    query = serializers.CharField()