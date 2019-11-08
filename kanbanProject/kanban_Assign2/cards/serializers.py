from rest_framework import serializers
from cards.models import Card, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# ImproperlyConfigured at /api/cards
# Could not resolve URL for hyperlinked relationship using view name "task-list".
# You may have failed to include the related model in your API, or incorrectly configured the `lookup_field` attribute on this field.

class CardSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(view_name='task-list', many=True, read_only=True)
    class Meta:
        model = Card
        #fields = ['title', 'description', 'tasks']
        fields = '__all__'


'''
class CardSerializer(serializers.ModelSerializer):    
    # tested. Good. i.e. 
    #         "id": 1,
    #         "tasks": [
    #             "read 1st chapter",
    #             "read 2nd chapter"
    #         ],
    tasks = serializers.SlugRelatedField(
        many=True,
        read_only =True,
        slug_field='description'
    )
    class Meta:
        model = Card
        fields = '__all__'
        
        
'''

'''
class CardSerializer(serializers.ModelSerializer):     
    # good for homework#2 i.e.
    #"id": 1,
    #"tasks": [
    #    {
    #        "id": 1,
    #        "description": "read 1st chapter",
    #        "done": false,
    #        "card": 1
    #    }, ...
    #]
    tasks = TaskSerializer( 
        many=True,
        read_only =True
    )
    
    status_task = serializers.SerializerMethodField(
        method_name='get_status_text',
        read_only=True
    )

    def get_status_text(self, instance):
        return instance.get_status_display()
    
    class Meta:
        model = Card
        fields = '__all__'
'''
