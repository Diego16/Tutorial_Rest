from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from snippets.permissions import IsOwnerOrReadOnly
class UserList(generics.ListAPIView):
	queryset= User.objects.all()
	serializers_class= UserSerializer
class UserDetail(generics.RetrieveAPIView):
	queryset= User.objects.all()
	serializer_class=UserSerializer
class SnippetList(generics.ListCreateAPIView):
	permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer