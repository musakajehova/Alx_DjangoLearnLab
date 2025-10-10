from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'actor_username', 'verb', 'target_repr', 'unread', 'timestamp']

    def get_target_repr(self, obj):
        if obj.target is None:
            return None
        # Return a small string representation (e.g., Post title or Comment id)
        try:
            return str(obj.target)
        except Exception:
            return f"{obj.target_content_type}({obj.target_object_id})"
