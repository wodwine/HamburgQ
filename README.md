<p align="center">
    <a href="https://hamburgq.herokuapp.com/"><img src="Game/static/Base/img/logo.png"></a>
</p>


# HamburgerQ [![Build Status](https://travis-ci.com/wodwine/HamburgQ.svg?branch=master)](https://travis-ci.com/wodwine/HamburgQ) [![codecov](https://codecov.io/gh/wodwine/HamburgQ/branch/master/graph/badge.svg)](https://codecov.io/gh/wodwine/HamburgQ)
**HamburgQ** is a Quiz-Game. The game is about answering the questions. There are many types of quiz which contains about 10-15 questions, and 4 choices per question. Host can create a room, the host also can choose the quiz type and the time per question, or you can access the the friend's room by Code ID which generate after the host create a room. The room show the number of player and each of the player name who now in the room waiting to play the game (including Host). After the game start, the 1st question will show and you have to answer in fix time. When the game end, each of the player score will show in the last and the score will be kept in the database to show in the first page of the game which is Score Board.

## Documents

- Iteration plan - [Iteration plan](https://docs.google.com/document/d/133HPHjWUwl43IdhKVEMPJiHcuoHuUlzp2-9CJC1oEoE/edit)
- Task Board - [Trello](https://trello.com/b/OzYse9c9/hamburgq)  
- Github - [Github](https://github.com/kidstylex/HamburgQ)
- Mockup Papers - [Mockup Papers](https://docs.google.com/presentation/d/1iLrLxaDiU9liUZJI3gHnZ0y2dnxpwuQllvGP1yIU29o/edit#slide=id.p)
- Project Proposal - [Project Proposal](https://docs.google.com/document/d/1UD7B5s0sYkI1M6M1O-IvHSsvIg23JR0TkrShE1AXIk0/edit#heading=h.vkq3s4w01uy9)
- Code Review Script and Checklist- [Code Review Script
](https://docs.google.com/document/d/1zPGRHCFPNvA5OCWQc-J3Q4h8VnlXVnxrC8IPeDdF7vw/edit?usp=sharing)  and [Code Review Checklist
](https://docs.google.com/document/d/1X7eSuoDbGrmmTzt0P9sBkal2dof4DjkpO62N1ioPEQ8/edit?usp=sharing)

## Team Members

GitHub       |           Name           |               Roles
-------------|--------------------------|-------------------------------------
wodwine      |   Panthakarn Kiatpaisansopon    |       Scrum Master, Developer (Full stack)
kidstylex    |   Arisa Pangpeng |              Developer (Front-end)
326th  |  Thananan Eim-on        |              Developer (Back-end)

## Prerequisite

- Python 3.7 or above
- Django 2.2.5

## Installation Steps

### Step 1: Clone the project to your local directory.

Open the Terminal and use command:

    git clone https://github.com/wodwine/HamburgQ

### Step 2: Go to the directory.

    cd HamburgQ/

### Step 3: Create new virtual enviroment.

    virtualenv env

### Step 4: Activate virtualenv.

***On MacOS and Linux:***

    source venv/bin/activate

***On Windows:***

    venv\Scripts\activate

### Step 5: Rename `.env-example` in the root directory of project to `.env`

### Step 6: Install all required packages.

    pip install -r requirements.txt

### Step 7: Create database tables.

    python3 manage.py migrate

### Step 8: Load data dump from `data.json`

   This is for adding our premade data
    
    python3 manage.py loaddata data.json

### Step9: Run server at localhost:8000

    python3 manage.py runserver --insecure

### Step 10: create question yourself

   to create a question you must first create superuser (stop your server from running when doing this)
   
    python3 manage.py createsuperuser
    
   and add infomation of superuser (user, email and password) then runserver
   
    python3 manage.py runserver --insecure
    
   then click admin button at [your homepage](https://127.0.0.1:8000/) and login with your superuser, now you can edit, add or remove any quiz, question, choices, waiting room or player you like
