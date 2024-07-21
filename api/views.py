from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from .serializers import ClassPeriodSerializer
from .serializers import TeacherSerializer
from teacher.models import Teacher
from course.models import Course
from classes.models import Class
from classPeriod.models import ClassPeriod
from rest_framework import status
from .serializers import CourseSerializer
from .serializers import ClassSerializer





# Create your views here.
class StudentListView(APIView):
    # FUNCTION FOR THE GET METHOD
    def get(self, request):
        # RETRIEVING ALL STUDENTS DATA
        students = Student.objects.all()
        # SERIALIZING IT TO JSON FORMAT
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassListView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeachersListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class ClassPeriodListView(APIView):
    def get(self, request):
        classPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classPeriod, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # DESERIALIZING
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GETTING THE DETAILS OF A USER
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classPeriod = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classPeriod)
        return Response(serializer.data)



class StudentDetailView(APIView):
    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class TeacherDetailView(APIView):
    def put(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class CourseDetailView(APIView):
    def put(self, request, id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class StudentDetailView(APIView):
    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TeacherDetailView(APIView):
    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CourseDetailView(APIView):
    def delete(self, request, id):
        course = Course.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ClassDetailView(APIView):
    def delete(self, request, id):
        classes = Class.objects.get(id = id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


    