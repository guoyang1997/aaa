from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .form import LoginForm,RegisterForm
from .models import User,Users
from django.views.generic import View

def index(request):

    return render(request, "index.html")

#登录
class Login(View):
    def get(self, request):
        return render(request, "User/login.html")
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.filter(username=username, password=password).first()
            if user:
                return redirect(reverse('index'))
            else:
                print("用户名或密码错误！")
                return redirect(reverse('login'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))


# 注册用户
class AddUser(View):

    def get(self,request):
        return render(request,'adduser.html')
    def post(self, request):
        form = RegisterForm(request.POST)
        # aa = form['username'].data
        # print('++++++++++++++++++++++++++',aa,form)
        if form.is_valid():
            form.save()
            datas = Users.objects.all()
            return render(request, 'index.html',{'form_data':datas})
        else:
            # errors = form.edit_error_message()
            #             # # for error in errors:
            #             #     # messages.add_message(request, messages.INFO,’信息’)
            #             # print(errors)

            return render(request,'User/index.html')

#展示数据
def adsf(request):
    a = Users.objects.all()

    return render(request, "aaaaa.html",{'aaa':a})

# 删
class Del_data(View):
    def get(self,request):
        del_id = request.GET.get('del_id')
        a = Users.objects.filter(id=del_id).delete()
        # # 将客户端的json字符串转换成python字典
        # python_dict = request.POST.get_json()
        # # 解析python字典获取author_id值
        # del_id = python_dict.get("del-id")
        # print(del_id)
        return redirect(reverse('a'))
#
# #改
# class ChangeData(View):
#     def get(self,request):
#         cha_id = request.GET.get('cha_id')
#         # global cha_id
#         print(cha_id)
#         datas = Users.objects.filter(id=cha_id).first()
#         print(datas)
#         return render(request,"change_data.html",{"id":cha_id,"datas":datas})
#     def post(self,request):
#         print('++++++++++++++++++++',request)
#         a = request.POST.get('change_id')
#         print(a)
#         form = RegisterForm(request.POST)
#         print(form)
#         username = form['username'].value()
#         password = form['password'].value()
#         realname = form['realname'].value()
#         email = form['email'].value()
#         role = form['role'].value()
#         status = form['status'].value()
#         print(status, email, role, password)
#         # id = form['id'].value()
#         # Users.objects.filter(id=ids).update(name=username, password=password,realname=realname,email=email,role=role,status=status)
#         return redirect(reverse("a"))

def change(request):
    cha_id =request.GET.get("cha_id")
    print('++++++++++++++',cha_id)
    if request.method == "GET":
        cha_id = request.GET.get('cha_id')
        # global cha_id
        print(cha_id)
        datas = Users.objects.filter(id=cha_id).first()
        print(datas)
        return render(request,"change_data.html",{"id":cha_id,"datas":datas})
    else:
        print('++++++++++++++++++++',request)
        a = request.POST.get('change_id')
        print(a)
        form = RegisterForm(request.POST)
        print(form)
        username = form['username'].value()
        password = form['password'].value()
        realname = form['realname'].value()
        email = form['email'].value()
        role = form['role'].value()
        status = form['status'].value()
        print(status, email, role, password)
        # id = form['id'].value()
        Users.objects.filter(id=cha_id).update(username=username, password=password,realname=realname,email=email,role=role,status=status)
        return redirect(reverse("a"))