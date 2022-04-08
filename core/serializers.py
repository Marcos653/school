from core.models import *
from rest_framework.serializers import ModelSerializer

class TeachSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__' 


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'         


class QuizzSerializer(ModelSerializer):
    class Meta:
        model = Quizz
        fields = '__all__'  

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'      

class StudentPointSerializer(ModelSerializer):
    class Meta:
        model = StudentPoint
        fields = '__all__'              
