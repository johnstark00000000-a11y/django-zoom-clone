import secrets
from django.db import models
from django.contrib.auth.models import User

def generate_meeting_id():
    raw = secrets.token_urlsafe(9).lower().replace('_', 'a').replace('-', 'b')
    return f"{raw[:3]}-{raw[3:6]}-{raw[6:9]}"

class Meeting(models.Model):
    meeting_id = models.CharField(max_length=15, unique=True, default=generate_meeting_id)
    title = models.CharField(max_length=100, default="Zoom Meeting")
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    passcode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_join_url(self, request):
        return f"{request.scheme}://{request.get_host()}/join/{self.meeting_id}/?pwd={self.passcode}"
