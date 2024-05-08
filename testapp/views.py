from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee1,ProxyEmployee2
# Create your views here.
def display_view(request):
    #emp_list = Employee.objects.all()
    #emp_list = ProxyEmployee1.objects.all()
    emp_list = ProxyEmployee2.objects.all()
    #emp_list = Employee.objects.get_emp_sal_range(18000,20000)
    #emp_list = Employee.objects.get_emp_sorted_by('ename')
    #emp_list = Employee.objects.get_emp_sorted_by('-esal')
    return render(request,'testapp/index.html',{'emp_list':emp_list})
