from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import address
from django.forms import forms

from .forms import addressForm


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the orm01 index.")

def address_list(request):
        all_address = address.objects.all()
        return render(request,'addresss_list.html',context={'all':all_address})


def address_add(request):
    #만일에 요청한 메소드가 post라면
    if(request.method == 'POST'):
    #addressForm의 객체를 생성해서
        form = addressForm(request.POST)

    #검증하고
        if form.is_valid():
    #저장한 후
            form.save()
    #전체 데이터를 출력
            return redirect('address_list')
    #그렇지 않으면
    else:

    #빈폼을 생성한다
            form = addressForm()
    #추가하는 페이지 랜더링 한다
            return render(request, 'addresss_add.html', context={'form': form})