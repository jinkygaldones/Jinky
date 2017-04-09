from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm
from django.db.models import Q

# Create your views here.
def posts_home(request):
    return HttpResponse("<h1>Showbizz Portal.</h1>")

def posts_list(request):
    queryset =News.objects.all()
    query = request.GET.get("search")

    if query:
        queryset = queryset.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query)
            ).distinct()

    context = {
        "queryset": queryset,
        "title": "Showbizz Portal"
    }
    return render(request, "posts_list.html", context)
    #return HttpResponse("<h1>this is list.</h1>")

def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.user = request.user
        instance.save()

        return HttpResponseRedirect(instance.get_absolute_url())
    context= {
        "form": form,
    }
    return render(request, "posts_form.html", context)
    #return HttpResponse("<h1>create.</h1>")

def posts_detail(request, id=None):
    instance= get_object_or_404(News, id=id)
    context = {
        "title": "Showbizz Portal",
        "instance": instance,
    }
    return render(request, "posts_detail.html", context)
    #return HttpResponse("<h>detail.</h1>")

def posts_update(request, id=None):
        instance = get_object_or_404(News, id=id)
        form = NewsForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance= form.save(commit=False)
            print form.cleaned_data.get("title")
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "title": instance.title,
            "instance": instance,
            "form": form,
        }
        return render(request, "posts_form.html", context)
    #return HttpResponse("<h1>update.</h1>")

def posts_delete(request, id=None):
    isinstance = get_object_or_404(News, id=id)
    isinstance.delete()
    return redirect("posts:list")
    return HttpResponse("<h1>delete.</h1>")
