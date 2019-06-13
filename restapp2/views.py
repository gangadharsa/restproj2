from django.shortcuts import render
from datetime import datetime
from rest_framework.renderers import JSONRenderer
from .serializers import CommentSerializer
from django.http import HttpResponse



# Create your views here.
class Comment:
    def __init__(self,email,content,created=None):
        self.email=email
        self.content=content
        self.created=created or datetime.now()
def myapi(request):
    comment = Comment(email='chagulu1991@gmail.com', content='GANGA')
    serializer = CommentSerializer(comment)
    return HttpResponse(JSONRenderer().render(serializer.data))
