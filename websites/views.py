from django.shortcuts import render

# Create your views here.

def zhongkao(request):
    context = {}
    return render(request,'websites/zhongkaotime.html',context=context)