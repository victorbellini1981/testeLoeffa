from django.shortcuts import render, redirect  
from funcionario.forms import EmployeeForm  
from funcionario.models import Funcionario  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Funcionario.objects.all()  
    return render(request,"mostrar.html",{'employees':employees})  
def edit(request, id):  
    employee = Funcionario.objects.get(id=id)  
    return render(request,'editar.html', {'employee':employee})  
def update(request, id):  
    employee = Funcionario.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'editar.html', {'employee': employee})  
def destroy(request, id):  
    employee = Funcionario.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
