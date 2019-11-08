from django.db import models

'''
@author: WanLing (Liddy) Hsieh 
Assignment4 - http://127.0.0.1:8000/api/cards 
Re-configure your Kanban project using basic authentication with username and password.
Write the following test cases (See detail in test//test_post_card.py):
1. Creating a Kanban card anonymously receives 401 status;
2. Creating a Kanban card with valid username and password will receive 201
status;
3. Creating a task for an existing Kanban card with valid username and
password
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