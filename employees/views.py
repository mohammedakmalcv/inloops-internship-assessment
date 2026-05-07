from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

   
    def get_queryset(self):
        return Employee.objects.filter(status='ACTIVE')

    
    def destroy(self, request, *args, **kwargs):
        employee = self.get_object()
        employee.status = 'INACTIVE'
        employee.save()
        return Response({"message": "Employee marked as INACTIVE"}, status=status.HTTP_204_NO_CONTENT)