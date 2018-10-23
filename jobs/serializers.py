from rest_framework.serializers import ModelSerializer
from jobs.models import Job
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class JobSerializer(TaggitSerializer,ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Job
        fields = ('id', 'title','description','tags','submitInfo','slug','publish','status','image','tipo','company','salary')
        