import json
from django.db.models import Q
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core import serializers
from django.utils.text import slugify
from rtf.models import Protest, Chapter
from rtf.forms import VolunteerForm
from geopy import geocoders
from django.utils import timezone


# Protests
def protests(request):
  show_all = request.GET.get('show_all', 'false');
  if(show_all is 'false'):
    protest_list = Protest.objects.filter(date__gte = timezone.now()).order_by('city')
  else:
    protest_list = Protest.objects.all().order_by('city')
  context = {'protest_list' : protest_list, 'showing_all' : show_all}
  return render(request, 'protests/protests.html', context)

def protests_by_state(request, state=None):
  protests = get_list_or_404(Protest, state_slug=state.lower())
  return render(request, 'protests/protest.html', {'protests': protests})

def protest_by_city(request, state=None, city=None, protest=None):
  if protest is None:
    protest = get_object_or_404(Protest, state_slug=state.lower(), city_slug=city.lower())
  return render(request, 'protests/protest.html', {'protest': protest})

def protest_by_id(request, protest_id=None):
  protest = get_object_or_404(Protest, pk=protest_id)
  return redirect(protest.get_absolute_url(), protest=protest)

def protests_json(request):
  protest_list = Protest.objects.all().exclude(state=None).order_by('-state')
  data = [protest.to_json() for protest in protest_list]
  return HttpResponse(json.dumps(data), mimetype="application/json")

@staff_member_required
def protest_lat_long(request):
  protests = Protest.objects.all()
  for protest in protests:
    protest.generateLatLong()
    protest.save()
  context = {'protest_list' : protests}
  return render(request, 'protests/protests.html', context)

# Chapters
def chapters(request):
  chapter_list = Chapter.objects.all().order_by('city')
  context = {'chapter_list' : chapter_list}
  return render(request, 'chapters/chapters.html', context)

def chapters_by_state(request, state=None):
  chapters = get_list_or_404(Chapter, state_slug=state.lower())
  return render(request, 'chapters/chapter.html', {'chapters': chapters})

def chapter_by_city(request, state=None, city=None):
  chapter = get_object_or_404(Chapter, state_slug=state.lower(), city_slug=city.lower())
  return render(request, 'chapters/chapter.html', {'chapter': chapter})

def chapters_json(request):
  chapter_list = Chapter.objects.all().order_by('-state')
  data = [chapter.to_json() for chapter in chapter_list]
  return HttpResponse(json.dumps(data), mimetype="application/json")

@staff_member_required
def chapter_lat_long(request):
  chapters = Chapter.objects.all()
  for chapter in chapters:
    chapter.generateLatLong()
    chapter.save()
  context = {'protest_list' : chapters}
  return render(request, 'chapters/chapters.html', context)

def blitzio(request):
  return HttpResponse("42")

def volunteer(request):
  if request.method == 'GET':
    # return form
    form = VolunteerForm()
    context = {'form': form}
    return render(request, 'forms/volunteer.html', context)
  elif request.method == 'POST':
    # process form
    form = VolunteerForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/thanks/')
    else:
      context = {'form': form}
      return render(request, 'forms/volunteer.html', context)
