

####Thank You and Happy Hacking Guys

just clone and ```pip install -r requeriments.txt && python manage.py runserver```

login credentials:

username: admin <br>
password: admin

### Relation of requeriments applied to this project:

* The quiz should have a dynamic title from database;

    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/apps/quiz/views.py#L51)

* Quiz should have between 1 and 10 questions;
    
    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/apps/quiz/admin.py#L20)
    
* Each question should contain between 2 and 4 answers;
    
    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/apps/quiz/admin.py#L12)

* Each question should have an image on the left side if the image is not
available, the application must provide a default;

    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/apps/quiz/templatetags/quiz_tags.py#L6)
 
* A "Send" button must be added at the end of the form and only allow action if all questions have been answered
    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/templates/quiz/index.html#L205)
    
* Number of People answered the quiz; 
    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/apps/statistics/views.py#L57)
    
* for Each Question the most voted answer
 
    * : [Related code](https://github.com/rodgomesc/survey_manager/blob/ba96215540ab6b91e82d0f593db239fb0c18b7a4/apps/statistics/views.py#L23)