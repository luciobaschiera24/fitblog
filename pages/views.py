from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Routine
from .forms import RoutineForm

class RoutineListView(ListView):
    model = Routine
    template_name = 'pages/routine_list.html'
    context_object_name = 'routines'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Routine.objects.filter(title__icontains=query)
        return Routine.objects.all()

class RoutineDetailView(LoginRequiredMixin, DetailView):
    model = Routine
    template_name = 'pages/routine_detail.html'
    context_object_name = 'routine'

@login_required
def routine_create(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('routine_list')
    else:
        form = RoutineForm()
    return render(request, 'pages/routine_form.html', {'form': form, 'action': 'Crear'})

@login_required
def routine_update(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        form = RoutineForm(request.POST, request.FILES, instance=routine)
        if form.is_valid():
            form.save()
            return redirect('routine_list')
    else:
        form = RoutineForm(instance=routine)
    return render(request, 'pages/routine_form.html', {'form': form, 'action': 'Editar'})

@login_required
def routine_delete(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        routine.delete()
        return redirect('routine_list')
    return render(request, 'pages/routine_confirm_delete.html', {'routine': routine})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

