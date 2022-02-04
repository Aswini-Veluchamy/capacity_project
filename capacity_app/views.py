from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import CapacityData

import time, datetime
from datetime import datetime
# Create your views here.
@csrf_exempt
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user1 = authenticate(request, username=username, password=password)
        if user1:
            login(request, user1)
            return HttpResponseRedirect(reverse("dashboard"))

        else:
            context["error"] = "Provide Valid Credentials"
            return render(request, "capacity_app/login.html", context)

    else:
        return render(request, "capacity_app/login.html")


@csrf_exempt
def dashboard(request):
    return render(request, 'capacity_app/dashboard.html')


@csrf_exempt
def create_request(request):

    tkt_status = "ACTIVE"

    if request.method == "POST":
        data_center = request.POST['dc']
        project = request.POST['project']
        user_id = request.POST['user_id']
        move_group_name = request.POST['move_group_name']
        std_stable1 = request.POST['std_stable1']
        std_stable2 = request.POST['std_stable2']
        std_arbor = request.POST['std_arbor']
        stable1 = request.POST['stable1']
        stable2 = request.POST['stable2']
        arbor = request.POST['arbor']
        gravit = request.POST['gravit']
        remarks = request.POST['remarks']

        request_id = str(int(time.time() * 1000))
        now = datetime.now()
        date_time = str(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(date_time)
        request_data_create = CapacityData.objects.create(
            request_id=request_id,
            updated_time=date_time,
            data_center=data_center,
            project_name=project,
            user_id=user_id,
            std_stable_1=std_stable1,
            std_stable_2=std_stable2,
            std_arbor=std_arbor,
            stable_1=stable1,
            stable_2=stable2,
            arbor=arbor,
            gravit=gravit,
            move_group_name=move_group_name,
            remarks=remarks,
            tkt_status=tkt_status,
        )
        request_data_create.save()
        return HttpResponseRedirect(reverse("view_request"))
    else:
        # print(dc, project, remarks)
        return render(request, 'capacity_app/create_request.html')


@csrf_exempt
def view_request(request):
    data = CapacityData.objects.all()
    return render(request, 'capacity_app/view_request.html', {'data': data})


@csrf_exempt
def update_request(request, pk):
    print(pk)
    data = CapacityData.objects.get(pk=pk)
    return render(request, 'capacity_app/update_request.html', {"data": data})


@csrf_exempt
def completed_request(request):
    return render(request, 'capacity_app/completed_request.html')
