# Recommend timetable for you

We are interested to work on school life. The detailed topic is 'Timetable Recommendation Program'. The target users for this application are all the Sungkyunkwan university students. The optimal timetable is recommended in consideration of personal information such as personal schedule, preferences of professors and lectures, and personal information such as lifestyle (meal time, etc.). At this time, according to the roadmap of the major, it reflects the classes that are good to take in the semester and recommends not to repeat the subjects students have taken before. In addition, this program also offers several alternatives because several plans are made in consideration of failure to register for courses when writing the timetable themselves. In this way, we want to dramatically reduce the time students spend thinking about timetables.

For further detail, please read `Presentation.pdf` file


## Running GUI

First, you need to make virtual environment by using 'requirements.txt' file.

Then, activate the virtual environment.  
To run the GUI, run the following command:

```
python manage.py runserver
```

This will start the server on port 8000.
There are 4 pages in the GUI and each has a different link:

1. Home Page
   http://127.0.0.1:8000/
2. Login Page
   http://127.0.0.1:8000/login/
3. Survey Page
   http://127.0.0.1:8000/survey/
4. Timetable Page
   http://127.0.0.1:8000/timetable/  
   When you click button or refresh the page(F5), the timetable will be changed.

## Test Cases

There are 3 students in the database.

1. login_id: yerim, password: 1234
    - major: Eastern Philosophy
    - double major: Statistics
2. login_id: holywood, password: 1234
    - major: Computer Science
    - double major: None
3. login_id: desa, password: 1234
    - major: Data Science
    - double major: Economics

## Description of each directory

### 1. data

In this directory, there are subject data as json files. We crawled the data from the website of the university.

### 2. templates

In this directory, there are html files. Each html file is a page of the GUI.

### 3. crawling

In this directory, there are python files for crawling the data from the website of the university.

### 4. datacleaning

In this directory, there are python files for cleaning the data. We used the data from the directory 'data'. We used
pandas library and python to clean the data.
(most of the data is cleaned by using python.)

## File that contains main functions

### 1. sql.py

This file contains functions that insert, update, select data from the database. + join tables

### 2. timetabling.py

This file contains functions that make timetable.

### 3. user/views.py

This files contains functions that are related to the GUI. There are classes named "Login","Survey","Timetable" ,

## Database

There are 15 tables in the dsc3037 database. But please ignore the tables written in the following list. They are not
used in the project. I left them because of dependency and backup.

- `auth_group`
- `auth_group_permissions`
- `auth_permission`
- `django_content_type`
- `django_migrations`
- `django_session`
- `liberal arts_subject`
- `major_subject`
- `skku_subject_1`

The table we used in the project is as follows.

- `skku_subject`
- `student_academic`
- `student_mandatory`
- `studnet_preference`
- `student_info`
- `user_info`

## Contact

If there are any questions or problems, please feel free to contact me.

- ownvoy@g.skku.edu
- 010-5279-5098
