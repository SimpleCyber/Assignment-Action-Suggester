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


## PHASE 6: Views [ Interaction between OpenAI, Database]

   6.1 : accept query
   ``` JSON
      { "query": "Mobile is like an addiction" }
   ```

   6.2 : Validates it using Serializer

   6.3 : save the response to the database

   6.4 : return the structured JSON response
   ``` JSON
      {
         "query": "User's message",
         "analysis": {
         "tone": "Identified Tone",
         "intent": "Identified Intent"
         },
         "suggested_actions": [
         {"action_code": "ACTION_1", "display_text": "Suggestion 1"},
         // ... more suggestions (up to 3)
         ]
      }
   ```


## PHASE 7: Creating end point { api/analyze/ }

   7.1 : create urls.py in core and update urls.py in action_suggester

   7.2 : Tesing through the postman

         1. start server : python manage.py runserver
         2. open postman
         3. Select post
         4. enter url : http://127.0.0.1:8000/api/analyze/
         5. Body -> raw -> Json
         6. Enter query : 
            {
               "query": "Amazon forset is lungs of the world"
            }
         7. click send
   

   





