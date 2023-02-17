# Practical Interview Question

You are hired to develop a web system to register students in Kilimo High School.

### Installation
```
    $ git clone git@github.com:KaigaMunene/fintech_interview_question.git
    $ cd fintech_interview_question
    $ sudo apt install pipenv (https://pipenv.pypa.io/en/latest/install/#installing-pipenv) ensure you have python and pip installed
    $ pip install -r requirements.txt 
    $ pipenv install (you should be able to install the files in the requirements.txt) 
```

### Running the application 
```
$ python manage.py runserver
```

### How the system works
run the following url:
```
http://127.0.0.1:8000/admin/
```
then in the terminal run,
```
$ python manage.py createsuperuser
```

then you will see you various models were you can add the students and there various classes.