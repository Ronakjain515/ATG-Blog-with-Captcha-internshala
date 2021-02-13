from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegisterForm, CreateBlogForm
from .models import User, Blog

# Create your views here.
def Register(request):
    msg = ""
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
        else:
            msg = "Exist"

    return render(request, "Register.html", context={"msg": msg})


def Login(request):
    msg = ""
    try:
        if request.method == "POST":
            try:
                print("heollo")
                user = User.objects.get(userName=request.POST["userName"], password=request.POST["password"])
                request.session["userName"] = user.userName
                request.session["id"] = user.id
                return redirect("Dashboard")
            except User.DoesNotExist:
                msg = "wrong"
                print("hhhh")
    except KeyError:
        msg = "try again"


    # making Captcha
    from PIL import Image
    import base64
    from io import BytesIO, StringIO
    from PIL import ImageDraw, ImageFont
    import random


    Quest = str(random.randint(1, 9)) + " " + random.choice(["+", "-", "*"]) + " " +  str(random.randint(1, 9))
    ans = eval(Quest)

    output = BytesIO()
    im = Image.new(mode = "RGB", size = (100, 50), color = (211,211,211))
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(Quest)
    draw.text(((100-w)/2,(50-h)/2), Quest, fill=(0, 0, 0))
    im.save(output, format='PNG')
    cimg_str = base64.b64encode(output.getvalue())
    output.close()
    cimg_str = str(cimg_str)[2:-1]

    return render(request, "Login.html", context={"msg": msg, "captcha": str(cimg_str), "answer": ans})


def Logout(request):
    try:
        del(request.session["userName"])
        del(request.session["id"])
    except KeyError:
        return redirect("Login")

    return redirect("Login")


def Dashboard(request):
    try:
        userName = request.session["userName"]
        userId = request.session["id"]
    except KeyError:
        return redirect("Login")
    
    user = User.objects.get(id=userId)
    blog = Blog.objects.all().filter(userId=user)

    return render(request, "Dashboard.html", context={"userName": userName, "Blogs": blog})


def CreateArticle(request):

    msg = ""
    try:
        userName = request.session["userName"]
        userId = request.session["id"]
    except KeyError:
        return redirect("Login")

    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "save"
        else:
            msg = "not"


    return render(request, "CreateArticle.html", context={"userName": userName, "msg": msg, "userId": userId})


def Search(request):
    try:
        userName = request.session["userName"]
        userId = request.session["id"]
    except KeyError:
        return redirect("Login")

    if request.method == "POST":
        blogs = Blog.objects.all().filter(visibility="public", title__contains=request.POST["searchName"])
    else:
        blogs = Blog.objects.all().filter(visibility="public")
    
    return render(request, "Search.html", context={"userName": userName, "blogs": blogs})