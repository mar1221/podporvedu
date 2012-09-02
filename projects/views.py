from django.http import HttpResponse, HttpResponseRedirect

from projects.models import Project
from projects.models import Donor
from projects.models import News
from projects.models import Post
# from projects.forms import PostForm

from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from django.forms import ModelForm


# Create your views here.

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('project',)

def about(request):
    return render_to_response('projects/about.html')

def kontakt(request):
    return render_to_response('projects/kontakt.html')

def akce(request):
    return render_to_response('projects/akce.html')


def index(request):
    projects = Project.objects.all()
    """     funding_progress = int(round(float(p.earned) / p.funding_needed, 2) * 100) """
    p = {
        'projects' : projects,
        'description' : "Projects",
        'earned' : "Projects",
        'funding_needed' : "Projects",
        'count_donors' : "Projects",
    }
    return render_to_response('projects/index.html', p, context_instance=RequestContext(request))

def projekt(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    d = p.donor_set.all()
    n = p.news_set.all()
    s = p.post_set.all()
    funding_progress = int(round(float(p.earned) / p.funding_needed, 2) * 100)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.project = p
            post.save()
            
            return redirect("/project/" + str(p.id) + "/")

    else:
        form = PostForm()            

    return render_to_response('projects/projekt.html', { 'project' : p, 'donors': d, 'news' : n, 'posts' : s, 'form' : form, 'funding_progress' : funding_progress}, context_instance=RequestContext(request))