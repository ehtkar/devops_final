devops_final
## Devops Portfolio Project

### What are the various features you would like your project to offer? 

For my project, I am creating a reading tracker. The database will consist of a list of books including title, author, and genre. Users can add, remove, or view books using HTTP requests.
### What are the API endpoints that you would need to set up for each feature? List them along with the respective HTTP verb, endpoint URL, and any special details (query parameters, request bodies, headers). 

POST - http://localhost:8000/books - add a new item to the book list
DELETE -  http://localhost:8000/books - remove an item from the book list
GET - http://localhost:8000/books/<genre> - display a list of books that belong to a specific genre
  
### Provide a description of the database tables required for your application, including column names, data types, constraints, and foreign keys. Include your database name. You can optionally include an ER diagram. 
  
The database table Books will include title, author, and genre. These will be text fields with maximum length constraints. I will eventually expand the database to include an Author table. The relationship between Books and Authors will be many-to-many. I will add HTTP commands to add/delete/get specific authors.



