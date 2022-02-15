from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CapacityData, HistoryData
from datetime import datetime
import time
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@csrf_exempt
def user_login(request):
    context = {}
    user_group = ""
    if request.method == "POST":
        '''getting user data from form'''
        username = request.POST['username']
        password = request.POST['password']
        ''' verifying user with the database'''
        user1 = authenticate(request, username=username, password=password)
        if user1:
            login(request, user1)

            group = request.user.groups.all()
            user_groups = [i.name for i in group]
            print(user_groups)
            # if len(group) > 0:
            #     user_group = group[0].name
            # else:
            #     user_group = "member"

            request.session["user_group"] = [user_groups, username]
            '''redirecting to dashboard page'''
            return HttpResponseRedirect(reverse("dashboard"))

        else:
            ''' user provide wrong credentials sending error msg'''
            context["error"] = "Provide Valid Credentials"
            return render(request, "capacity_app/login.html", context)

    else:
        return render(request, "capacity_app/login.html")


def user_logout(request):
    logout(request)
    try:
        del request.session["user_group"]
    except:
        pass
    return HttpResponseRedirect(reverse('login'))


@csrf_exempt
@login_required
def dashboard(request):
    user_group = request.session["user_group"][0][0]
    return render(request, 'capacity_app/dashboard.html', {"user_group": user_group})


@csrf_exempt
@login_required
def create_request(request):
    tkt_status = "ACTIVE"
    user_group = request.session["user_group"][0][0]
    projects = request.session["user_group"][0]
    print(projects, "=============================")

    ''' getting data from user form'''
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

        request_id = project[0:3] + "_" + str(int(time.time() * 1000))
        now = datetime.now()
        date_time = str(now.strftime("%Y-%m-%d %H:%M:%S"))

        ''' storing data into database '''
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
        return render(request, 'capacity_app/create_request.html', {"user_group": user_group, "projects": projects})


@csrf_exempt
@login_required
def view_request(request):
    """render all request to the front end"""
    user_group = request.session["user_group"][0][0]
    user_name =  request.session["user_group"][1]
    if user_group == "admin":
        data = CapacityData.objects.all()
        return render(request, 'capacity_app/view_request.html', {'data': data,
                                                                  "user_group": user_group})
    else:
        data = CapacityData.objects.filter(user_id=str(user_name))
        return render(request, 'capacity_app/view_request.html', {'data': data,
                                                                  "user_group": user_group})


@csrf_exempt
@login_required
def update_request(request, pk):

    if request.method == "POST":
        std_stable1 = request.POST.get('std_stable1', None)
        std_stable2 = request.POST.get('std_stable2', None)
        std_arbor = request.POST.get('std_arbor', None)
        stable1 = request.POST.get('stable1', None)
        stable2 = request.POST.get('stable2', None)
        arbor = request.POST.get('arbor', None)
        gravit = request.POST.get('gravit', None)
        remarks = request.POST.get('remarks', None)

        ''' fetch the record the table based on pk'''
        data = CapacityData.objects.get(pk=pk)

        ''' create updated ticket data in history table'''
        history_data_create = HistoryData.objects.create(
            request_id=data.request_id,
            updated_time=data.updated_time,
            data_center=data.data_center,
            project_name=data.project_name,
            user_id=data.user_id,
            std_stable_1=data.std_stable_1,
            std_stable_2=data.std_stable_2,
            std_arbor=data.std_arbor,
            stable_1=data.stable_1,
            stable_2=data.stable_2,
            arbor=data.arbor,
            gravit=data.gravit,
            move_group_name=data.move_group_name,
            remarks=data.remarks,
            tkt_status=data.tkt_status,
        )
        history_data_create.save()  # saving the record in the table

        updated_at = datetime.now()
        ''' updating the new vales in table '''
        CapacityData.objects.filter(pk=pk).update(std_stable_1=std_stable1,
                                                  std_stable_2=std_stable2,
                                                  std_arbor=std_arbor,
                                                  stable_1=stable1,
                                                  stable_2=stable2,
                                                  arbor=arbor,
                                                  gravit=gravit,
                                                  remarks=remarks,
                                                  updated_time=updated_at)
        return HttpResponseRedirect(reverse("view_request"))
    else:
        data = CapacityData.objects.get(pk=pk)
        user_group = request.session["user_group"][0]
        return render(request, 'capacity_app/update_request.html', {"data": data, "user_group": user_group})


@csrf_exempt
@login_required
def completed_request(request, pk):
    """ fetch the record the table based on pk"""
    data = CapacityData.objects.get(pk=pk)

    closed_date = datetime.now()
    ''' create updated ticket data in history table'''
    history_data_create = HistoryData.objects.create(
        request_id=data.request_id,
        updated_time=closed_date,
        data_center=data.data_center,
        project_name=data.project_name,
        user_id=data.user_id,
        std_stable_1=data.std_stable_1,
        std_stable_2=data.std_stable_2,
        std_arbor=data.std_arbor,
        stable_1=data.stable_1,
        stable_2=data.stable_2,
        arbor=data.arbor,
        gravit=data.gravit,
        move_group_name=data.move_group_name,
        remarks=data.remarks,
        tkt_status="Completed",
    )
    history_data_create.save()  # saving the record in the table
    time.sleep(1)
    '''after updating into history table deleting record from capacity table'''
    data.delete()
    return HttpResponseRedirect(reverse("view_request"))


@login_required
def history_request(request, id):
    user_group = request.session["user_group"][0][0]
    data = HistoryData.objects.filter(request_id=id)
    return render(request, 'capacity_app/history_request.html', {"data": data, "user_group": user_group})


@login_required
def completeticketdata(request):
    user_group = request.session["user_group"][0][0]
    user_name = request.session["user_group"][1]
    if user_group == "admin":
        data = HistoryData.objects.filter(tkt_status="Completed")
        return render(request, 'capacity_app/completed_request.html', {"data": data, "user_group": user_group})
    else:
        data = HistoryData.objects.filter(user_id=user_name, tkt_status="Completed")
        return render(request, 'capacity_app/completed_request.html', {"data": data, "user_group": user_group})
