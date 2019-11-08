from django.db import models


'''
@author: WanLing (Liddy) Hsieh 
Assignment1 - http://127.0.0.1:8000/api/cards 
Description - Create the model, serializer, views, and urls for Kanban card , which has the following fields:
1. title: as a required string (cannot be blank)
2. description: as a optional string
3. status: as a required string
4. make title unique and check the error message in Postman if you POST a card with the same title
5. make status values from the choices of ‘to-do’, ‘in-process’, or ‘done’, and check the error message in Postman 
   if you POST a card with a different status
'''
# Create your models here.
class Card(models.Model):
    TODO = 'to-do'
    INPROGRESS = 'in-progress'
    DONE = 'done'

    STATUS_CHOICE = (
        (TODO, 'To Do'),
        (INPROGRESS, 'In Progress'),
        (DONE, 'Done'),
    )

    title = models.CharField(
        max_length=250,
        unique= True)   #unique, required, not blank
    description = models.CharField(
        max_length=250,
        blank=True, #optional
        default='')
    status = models.CharField(
        max_length=250, #required
        choices=STATUS_CHOICE,
        default=TODO)

