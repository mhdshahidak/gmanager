from django.shortcuts import redirect
from ceo . models import User

def auth_crm(func):
    def wrap(request, *args, **kwargs):
        employe_ex = request.user.employee.catagory.title
        if employe_ex == "CRM":
            return func(request, *args, **kwargs)
        else:
            return redirect('ceo:login')
        
    return wrap


def auth_employee(func):
    def wrap(request, *args, **kwargs):
        employe_ex = request.user.employee.catagory.catagory.catagory_title
        if employe_ex == "EMPLOYEE":
            return func(request, *args, **kwargs)
        else:
            return redirect('ceo:login')
        
    return wrap


def auth_hrm(func):
    def wrap(request, *args, **kwargs):
        employe_ex = request.user.employee.catagory.title
        if employe_ex == "HRM":
            return func(request, *args, **kwargs)
        else:
            return redirect('ceo:login')
        
    return wrap


def auth_pm(func):
    def wrap(request, *args, **kwargs):
        employe_ex = request.user.employee.catagory.title
        if employe_ex == "PM":
            return func(request, *args, **kwargs)
        else:
            return redirect('ceo:login')
        
    return wrap


def auth_accounts(func):
    def wrap(request, *args, **kwargs):
        employe_ex = request.user.employee.catagory.title
        if employe_ex == "ACCOUNTS":
            return func(request, *args, **kwargs)
        else:
            return redirect('ceo:login')
        
    return wrap


# def auth_client(func):
#     def wrap(request, *args, **kwargs):
#         employe_ex = request.user.client
#         if employe_ex == is_active:
#             return func(request, *args, **kwargs)
#         else:
#             return redirect('ceo:login')
        
#     return wrap