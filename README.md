## PHASE 0: Setup the Github Repo
   Project Name : Action Suggester
   git clone https://github.com/SimpleCyber/Assignment-Action-Suggester.git



## PHASE 1: Project Initialization & Setup

    1.1 : Install all requirements
    pip install django djangorestframework python-dotenv psycopg2-binary openai

    1.2 : Create Django Project and App
    django-admin startproject actionsuggester 
    cd actionsuggester
    python manage.py startapp core

    1.3 : setup settings.py


## PHASE 2: .gitignore & .env

   2.1 : Create .gitignore and .env

   2.2 : Read .env using python-dotenv pip install python-dotenv



## PHASE 3: Creating Model and setup database (postgresql)

   3.1 : database name : Learn02

   3.2 : Create models.py
            query
            tone
            intent
            suggestion actions




## PHASE 4: Serializers

   4.1 : Create Serializers 


## PHASE 5: LLM api creation {OPEN AI api}

   5.1 : prompt
      Analyze the following input and respond in this format:
      Tone: <tone>
      Intent: <intent>
      Suggested actions:
      1. <step 1>
      2. <step 2>
      3. <step 3>
   
   5.2 : choose model of openai

   5.3 : parse the data

   5.4 : extract the data from the response

   5.5 : return tone, intent and suggestions





