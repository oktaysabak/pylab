from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import PostModel
from .forms import PostModelForm



@login_required
def post_model_delete_view(request, id):
    obj = get_object_or_404(PostModel, id=id)
    if request.user.is_authenticated():
        if request.method == "POST":
            obj.delete()
            return HttpResponseRedirect("/blog/".format(id=obj.id))
        
        context = {
            'post': obj,
        }
        template_path = "delete-view.html"
        return render(request, template_path, context)




@login_required
def post_model_update_view(request, id=None):

    if request.user.is_authenticated():
        obj = get_object_or_404(PostModel, id=id)
        form = PostModelForm(request.POST or None, instance=obj)
        context = {
            'post' : obj,
            'form': form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, "Post updated!")
            
            #return HttpResponseRedirect("/blog/{id}".format(id=obj.id))
    
    # return HttpResponse("some data")
        template_path = "update-view.html"
        
        return render(request, template_path, context)
    else:
        raise Http404


@login_required
def post_model_create_view(request):
    # if request.method == 'POST':
    #     print(request)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    if request.user.is_authenticated():
        form = PostModelForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, "Created nw Post!")
            context = {
                "form": PostModelForm()
            }
            #return HttpResponseRedirect("/blog/{id}".format(id=obj.id))
    
    # return HttpResponse("some data")
        template_path = "create-view.html"
        
        return render(request, template_path, context)
    else:
        raise Http404
    



@login_required
def post_model_detail_view(request, id):
    obj = get_object_or_404(PostModel, id=id)
    if request.user.is_authenticated():
    # return HttpResponse("some data")
        template_path = "detail-view.html"
        context = {'post': obj}
        return render(request, template_path, context)


@login_required
def post_model_list_view(request):
    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    if request.user.is_authenticated():
    # return HttpResponse("some data")
        template_path = "list-view.html"
        context = {'posts': qs}
        return render(request, template_path, context)
    else:
        raise Http404