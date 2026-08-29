import secrets
from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting

def create_meeting(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Zoom Meeting')
        passcode = secrets.token_hex(3)
        host_user = request.user if request.user.is_authenticated else None
        
        meeting = Meeting.objects.create(
            host=host_user,
            title=title,
            passcode=passcode
        )
        return redirect(f"/join/{meeting.meeting_id}/?pwd={meeting.passcode}")
    
    return render(request, 'video_app/enter_passcode.html', {'mode': 'create'})

def join_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, meeting_id=meeting_id)
    pwd_provided = request.GET.get('pwd') or request.POST.get('passcode')
    
    if pwd_provided != meeting.passcode:
        return render(request, 'video_app/enter_passcode.html', {
            'mode': 'join',
            'meeting_id': meeting_id, 
            'error': 'Galat Passcode!' if pwd_provided else None
        })

    is_host = request.user.is_authenticated and request.user == meeting.host

    return render(request, 'video_app/room.html', {
        'room_name': meeting.meeting_id,
        'meeting': meeting,
        'is_host': is_host,
        'join_url': meeting.get_join_url(request)
    })
