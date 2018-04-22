from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Artifact
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'docstore/index.html'
    context_object_name = 'all_artifacts'

    def get_queryset(self):
        return Artifact.objects.all()


class DetailView(generic.DeleteView):
    model=Artifact
    template_name = 'docstore/detail.html'


class ArtifactCreate(CreateView):
    model = Artifact
    fields = [
        'docname',
        'category',
        'type',
        'remark',
        'artifact_file'
    ]


class ArtifactUpdate(UpdateView):
    model=Artifact
    fields = [
        'remark',
        'artifact_file'
    ]


class ArtifactDelete(DeleteView):
    model = Artifact
    success_url = reverse_lazy('docstore:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'docstore/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.save()
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('docstore:index')
        return render(request,self.template_name,{'form':form})
