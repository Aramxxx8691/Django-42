import os
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import History
from django.conf import settings

def get_history():
    if os.path.exists(settings.HISTORY_LOG_FILE):
        with open(settings.HISTORY_LOG_FILE, 'r') as file:
            history = file.readlines()
    else:
        history = []
    return history

def ex02(request):
    if request.method == 'POST':
        form = History(request.POST)
        if form.is_valid():
            text = form.cleaned_data['history']
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp} - {text}\n"
            with open(settings.HISTORY_LOG_FILE, 'a') as file:
                file.write(log_entry)
            return redirect('ex02')
    else:
        form = History()
    
    history = get_history()

    return render(request, 'ex02.html', {'form': form, 'history': history})
