from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from .models import Project
from .forms import ProjectCreateForm
from django.contrib.auth.models import User

# Create your views here.
class ProjectListView(View):
    def get(self, request, *args, **kwargs):
        template_name="projects/index.html"
        projects = Project.objects.all().filter(owner = request.user.id)
        print(projects)
        context = {
            'projects' : projects,
        }
        return render(request, template_name, context)

class ProjectCreateView(View):

    def get(self, request, *args, **kwargs):
        template = 'projects/create.html'

        form = ProjectCreateForm()
        context = {
            'form': form,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        template = 'projects/create.html'

        if request.method == 'POST':
            form = ProjectCreateForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')
                owner = get_object_or_404(User, id=request.user.id)

                p, created= Project.objects.get_or_create(name = name, description = description, owner = owner)
                p.save()
                return redirect('projects:home')
        context = {

        }
        return render(request, template, context)

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description']
    template_name = 'projects/update.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('projects:detail', kwargs={'pk':pk})

class ProjectDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        template_name = 'projects/detail.html'
        
        project = get_object_or_404(Project, pk=pk)

        context= {
            'project': project
        }
        return render(request, template_name , context)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('projects:home')