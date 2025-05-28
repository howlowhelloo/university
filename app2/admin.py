from django.contrib import admin
from .models import Peer

    
@admin.register(Peer)
class PeerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)  # ← вот она, сортировка по алфавиту

