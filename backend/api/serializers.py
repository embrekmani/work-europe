from rest_framework import serializers
from jobs.models import Job

class JobSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format """
    class Meta:
        """ Meta class to map serializer's data fields with the model fields """
        model = Job
        fields = ('id', 'title', 'location', 'company', 'applicationLink', 'languages', 'description', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
