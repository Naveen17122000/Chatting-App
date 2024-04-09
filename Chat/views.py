from django.shortcuts import render,redirect
from .forms import MessageForm
from .models import Message

def chat_view(request):
    if request.method == 'POST':
        form =  MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat:chat_view')
    else:
        form = MessageForm()
    messages = Message.objects.all()
    return render(request,'chat.html',{'form':form, 'messages': messages})

def clear_messages(request):
    if request.method == 'POST':
        Message.objects.all().delete()
    return redirect('chat:chat_view')

