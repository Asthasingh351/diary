from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm

@login_required
def diary_entry_list(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'diary/diary_entry_list.html', {'entries': entries})

@login_required
def diary_entry_add(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary_entry_list')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/diary_entry_form.html', {'form': form})

@login_required
def diary_entry_edit(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_entry_list')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/diary_entry_form.html', {'form': form})

@login_required
def diary_entry_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk)

    if request.method == 'POST':
        entry.delete()
        return redirect('diary_entry_list')  # Redirect to the list view after deletion

    return render(request, 'diary/diary_entry_confirm_delete.html', {'entry': entry})
