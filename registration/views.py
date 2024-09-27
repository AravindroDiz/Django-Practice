from .serializers import EmployerSerializers
from .models import Employers
from rest_framework.views import APIView
from rest_framework.response import Response


class Registration(APIView):
    def get(self,request):
        employers = Employers.objects.all()
        serializer = EmployerSerializers(employers, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = EmployerSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request):
        try:
            employer = Employers.objects.get(id = request.data['id'])
        except:
            return Response({"error":"Employer not found"})
        
        serializer = EmployerSerializers(employer,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self,request):
        try:
            employer = Employers.objects.get(id = request.data['id'])
        except:
            return Response({"error":"Employer not found"})
        
        serializer = EmployerSerializers(employer,data = request.data,partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request):
        try:
            employer = Employers.objects.get(id = request.data['id'])
        except:
            return Response({"error":"Employer not found"})
        
        employer.delete()
        return Response({'message':'Employer deleted successfully.'})
