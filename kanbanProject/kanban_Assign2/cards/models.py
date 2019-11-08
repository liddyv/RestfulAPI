from django.db import models


'''
@author: WanLing (Liddy) Hsieh 
Assignment2 - http://127.0.0.1:8000/api/cards 
Description - Add a many-to-one relationship, i.e., a Kanban card may have 0 or more
tasks. Each task has the following fields:
1. description: as a required string
2. done: as a boolean value, with False as the default value
'''
# Create your models here.
class Card(models.Model):
    title = models.CharField(
        max_length=250,
        unique= True)   #unique, required, not blank
    description = models.CharField(
        max_length=250,
        blank=True, #optional
        default='')
    status = models.CharField(
        max_length=250, #required
        choices=(
            ('to-do', 'To Do'),
            ('in-progress', 'In Progress'),
            ('done', 'Complete')
        )
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {} ({})'.format(
            self.id,
            self.title,
            self.get_status_display()
        )


class Task(models.Model):
    description = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    card = models.ForeignKey(
        Card,
        related_name='tasks',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('card', 'description')