from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random as rd
from .forms import CreateNewPassword

# Create your views here.

LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
NUMS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["@","%","+","/","\ ","'","!","#","$","?",":",".","(",")","{","}","[","]","-","_","."]

def home(response):
    return render(response, "main/home.html")

def create(response):
    global joined_password
    form = CreateNewPassword()
    m = {}
    temp = []
    temp2 = []

    if response.method == "POST":
        form = CreateNewPassword(response.POST)

        if form.is_valid():
            d = form.cleaned_data["digits"]
            t = form.cleaned_data["check"]
            t1 = form.cleaned_data["check1"]
            t2 = form.cleaned_data["check2"]
            t3 = form.cleaned_data["check3"]

            if t:
                m[0] = LOWER
            if t1:
                m[1] = UPPER
            if t2:
                m[2] = NUMS
            if t3:
                m[3] = SPECIAL
            for i in m.keys():
                temp2.append(i)

            while len(temp) != int(d):
                list_choice = rd.choice(temp2)
                attempt = rd.choice(m[list_choice])
                temp.append(attempt)

            joined_password = "".join(temp)

            return HttpResponseRedirect("/show/")
    return render(response, "main/create.html", {"form":form})



def show_password(response):
    return render(response, "main/show.html", {"joined_password":joined_password})

def samples(response):

    return render(response, "main/samples.html", {})