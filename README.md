# RestfulAPI
Using Python Django to build and consume RESTful services using JSON. In coding assignments, created the model, serializer, views and urls for Kanban card with a many (tasks)-to-one(card) relationship, implemented the JWT-based &amp; basic authentications

* 'restProject' folder contains in-class Practices using Bookstore as an example.
* 'kanbanProject' folder contains all assignments for Kanban card project.

Please see the kanban Project requirements as follows:

Assignment 1:

In assignment 1, you need to create the model, serializer, views, and urls for
Kanban card , which has 1 the following fields:
1. title: as a required string (cannot be blank)
2. description: as a optional string
3. status: as a required string
The Kanban card APIs should be
GET /cards
POST /cards
with JSON request body of title, description, and status
GET /cards/1
PUT /cards/1
with JSON request body of title, description, and status
DELETE /cards/1
Please follow the simple approach we did in class 1.
Bonus points: (We have not talked about them yet.)
1. make title unique and check the error message in Postman if you POST a
card with the same title
https://docs.djangoproject.com/en/2.1/ref/models/fields/#unique
2. make status values from the choices of ‘to-do’, ‘in-process’, or
‘done’, and check the error message in Postman if you POST a card with a
different status
https://docs.djangoproject.com/en/2.1/ref/models/fields/#choices
Please zip the top-level project folder and submit the zip fil

Assignment 2:

Please add a many-to-one relationship, i.e., a Kanban card may have 0 or more
tasks. Each task has the following fields:
1. description: as a required string
2. done: as a boolean value, with False as the default value
When a card or a list of cards are queried through GET, the tasks in a card
should be included as a nested structure, such as
[
{
"id": 1,
"tasks": [
{
"id": 1,
"description": "Foo Desp1",
"done": false,
"card": 1
}
],
"title": "Foo",
"description": "Foo",
"status": "to-do"
},
{
"id": 2,
"tasks": [
{
"id": 2,
"description": "Bar Desc12",
"done": false,
"card": 2
}
],
"title": "Bar",
"description": "Bar",
"status": "in-progress"
}
]
When a task or a list of tasks are queried through GET, only the card Id will be
included in each task, such as
[
{
"id": 1,
"description": "Foo Desp1",
"done": false,
"card": 1
},
{
"id": 2,
"description": "Bar Desc12",
"done": false,
"card": 2
}
]

Assignment 3:

Please implement the JWT-based authentication so that
1. Each kanban card has an owner
2. Only the Kanban card owner can see and manage his/her own cards and the
related tasks
You have to manually create user through Python shell.
Here is the documentation for djangorestframework-jwt
http://jpadilla.github.io/django-rest-framework-jwt/

Assignment 4:

Re-configure your Kanban project using basic authentication with username
and password.
Write the following test cases:
1. Creating a Kanban card anonymously receives 401 status;
2. Creating a Kanban card with valid username and password will receive 201
status;
3. Creating a task for an existing Kanban card with valid username and
password.
