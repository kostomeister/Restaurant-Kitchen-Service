
# Restaurant-Kitchen-Service

This site is a management system where cooks can create new dishes and dish types. They can also specify which cooks are responsible for cooking each dish

## Run Locally

Clone the project

```bash
  git clone https://github.com/kostomeister/Restaurant-Kitchen-Service.git
```

Go to the project directory

### Create virtual env

On windows
```
  python -m venv venv
  venv\Scripts\activate
```
On macOS
```
  python3 -m venv my_env
  source my_env/bin/activate
```

Install dependencies

```
  pip install -r requirements.txt
```

### Set up DB

Make migrations and migrate

```
  python manage.py makemigrations
  python manage.py migrate
```

Load data from fixture

```
  python manage.py loaddata data.json
```

Then you can authenticate as admin with following credentials:
```
username: admin
password: mysuperdjangoproject
```

### Run server
Finally, you can run server with
```
python manage.py runserver
```

## Why us?
### It's easy to use!

Staff can simply create | update | delete \
dish types or dishes through interface \
But only admins can do those operations with Cooks


## Let me walk you through the main pages of the website
Link
```
https://kitchen-service-k661.onrender.com
```
    
Credentials to Log in:
```
username: user
password: user12345
``` 
    
### Main page
![img.png](static%2Fassets%2Fimg%2Fimg.png)

## Pages with objects where you can look through of all objects, search and create new objects!
![img_1.png](static%2Fassets%2Fimg%2Fimg_1.png)

## Object's details page where you can see details of object update or delete object
![img_2.png](static%2Fassets%2Fimg%2Fimg_2.png)