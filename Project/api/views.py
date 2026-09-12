from rest_framework.response import Response
from  rest_framework import status
from .serializer import EmployeeSerializer , DepartmentSerializer
from .models import Employee, Department
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_data(request):
    departments = Department.objects.all()
    employees = Employee.objects.all()
    serializer_department = DepartmentSerializer(departments,many=True)
    serializer_employee = EmployeeSerializer(employees , many=True)
    data = {
        'employee': serializer_employee.data,
        'department': serializer_department.data,
    }
    return Response(data , status=status.HTTP_200_OK)

@api_view(['POST'])
def post_department(request):
    serializer_department = DepartmentSerializer(data=request.data)
    if serializer_department.is_valid():
        serializer_department.save()
    else:
        return Response({"Error": "Please Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer_department.data, status=status.HTTP_201_CREATED)
        
@api_view(['POST'])
def post_employee(request):
    serializer_employee = EmployeeSerializer(data=request.data)
    if serializer_employee.is_valid():
        serializer_employee.save()
    else:
        return Response({"Error": "Please enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer_employee.data , status=status.HTTP_201_CREATED)


@api_view(['PUT', 'PATCH'])
def put_patch_data_employee(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response({"Error":"Data not found"} , status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer_employee = EmployeeSerializer(employee , data=request.data ,  partial=True)
    else:   
        serializer_employee = EmployeeSerializer(employee , data=request.data)
    

    if serializer_employee.is_valid():
        serializer_employee.save()
        return Response(serializer_employee.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer_employee.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'PATCH'])
def put_patch_data_department(request,pk):
    try:
        department  = Department.objects.get(id=pk)
    except Department.DoesNotExist:
        return Response({"Error":"Data Not found"} , status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        serializer_department = DepartmentSerializer(department , data=request.data , partial=True)
    else:
        serializer_department = DepartmentSerializer(department, data=request.data)
    
    if serializer_department.is_valid():
        serializer_department.save()
        return Response(serializer_department.data  , status=status.HTTP_200_OK)
    else:
        return Response(serializer_department.errors , status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_employee(request,pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response({"Error":"Data not found"}, status=status.HTTP_404_NOT_FOUND)
  
    employee.delete()

    return Response({"Message":"Data deleted successfully"} , status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_department(request,pk):
    try:
        department = Department.objects.get(id=pk)
    except Department.DoesNotExist:
        return Response({"Error":"Data not found"}  , status=status.HTTP_404_NOT_FOUND)
    
    department.delete()

    return Response({"Message":"Data deleted Successfully"} ,status=status.HTTP_200_OK)


    
