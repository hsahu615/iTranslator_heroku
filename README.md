# iTranslator
## About
This is an Translator which can Translate the input language to any desired language, there are 108 different languages present.
You can open iTranslator by [Clicking Here](https://itranslator.herokuapp.com/home).

## Home Page
<a href="https://ibb.co/wzpsrXS"><img src="https://i.ibb.co/cr2LXH6/Screenshot-34.png" alt="Screenshot-34" border="0"></a>

## Language
- Python: I used Python Language to form this application. I used Flask framework for back-end development. There is Google Translator open source library **googletrans** for providing API of google translator. Rest of imported libraries you can see below

```
from flask import Flask, render_template, request, url_for
from googletrans import Translator
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
import os
import psutil
```
Here I imported googletrans as it is the foundation of this project, than I imported Flask Mail service for feedback of this app. So, the user can directly give feedback to me by entering there Name, Email and Description in it. You can see the user interface of feedback form below:-
<a href="https://ibb.co/NNzhydR"><img src="https://i.ibb.co/C9FdH3L/Screenshot-35.png" alt="Screenshot-35" border="0"></a>
<br>
 - HTMl(Hypertext Markup Language): I used HTML for front-end development. There are 7 HTML pages used in this project in which Base is the main HTML page and others are connected with it by **{% extends base.html %}** command. This html files are present in templates folder.
 - CSS: It has been used for the styling of Webpage by setting Background image and designing navbar, font, color etcetra.
 <br>
 ## Deployment
 I deployed this application on Heroku Cloud Platform it is an awesome cloud platform specially for beginner, It is absolutely for some deployment, you can deploy your
 application by GITHUB directly or you can use Heroku CLI commands.
 [Heroku Link](https://itranslator.herokuapp.com/home).
 <br>
 <img src = "https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" alt = "Python" height = 120 wodth = 200><img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png" alt = "HTML" height= 120 width=120><img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/1200px-CSS3_logo_and_wordmark.svg.png" alt = "CSS"  height = 120 width = 120><span></span><img src = "https://cdn.worldvectorlogo.com/logos/heroku.svg" alt = "CSS"  height = 120 width = 120>
 
