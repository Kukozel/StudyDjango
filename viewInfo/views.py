from django.shortcuts import render
from viewInfo.models import Info
from django.core.paginator import Paginator

# Create your views here.

def view_info(request):
    limit=10
    infos = Info.objects
    paginator = Paginator(infos, limit)
    page_num = request.GET.get('page', 1)  # 从url中获取页码参数
    loaded = paginator.page(page_num)

    context = {
        'Infos': loaded
    }
    return render(request, 'infos.html',context)