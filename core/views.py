from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action

# Create your views here.


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class QuizzViewSet(ModelViewSet):
    queryset = Quizz.objects.all()
    serializer_class = QuizzSerializer 

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer  

    @action(detail=False, methods=['post'], url_path='is_valid')
    def post_is_valid(self, request):
        # try:
            answer_id = request.POST.get('answer_id', None)
            course_video = Answer.objects.get(id=answer_id)    
            if course_video:
                answer = course_video.valid
                post_point(StudentPoint, StudentPoint, StudentPoint)
                return Response({'answer': answer})
 

        # except:           
        #     return Response({'worked': False})             

class StudentPointViewSet(ModelViewSet):
    queryset = StudentPoint.objects.all()
    serializer_class = StudentPointSerializer

