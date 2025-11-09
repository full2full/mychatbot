from django.test import TestCase

# Create your tests here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os
import json
from django.conf import settings
chatbot = ChatBot(
    'DjangoBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3'
)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
trainer = ListTrainer(chatbot)
file_path = os.path.join(settings.BASE_DIR,"chat", "static", "data", "training_data.json")

# Load the data
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    for qa in data:
        trainer.train(qa)
# trainer = ListTrainer(chatbot)
# trainer.train([
# "Who are you?",
# "I am Subham's personal ChatBot, powered by your knowledge and skills.",

# "What skills do you have?",
# "I know Python, Django, Flask, MongoDB, OpenCV, Tesseract OCR, DeepFace, and chatbot development.",

# "What is your qualification?",
# "I am a professional Python developer with experience in web development and AI-based projects.",

# "Tell me about yourself.",
# "I am a personal assistant ChatBot trained to answer questions about Python, web development, Flask, MongoDB, OCR, and AI projects.",

# "How do I create a virtual environment in Python?",
# "You can create one using: python -m venv venv and then activate it based on your OS.",
# "Hi",
# "Hello! How are you?",

# "Hello",
# "Hey! How's it going?",

# "What's up?",
# "Not much! How about you?",

# "How are you?",
# "I'm good, thanks! What about you?",

# "I'm fine",
# "That's great to hear!",

# "Who are you?",
# "I'm a ChatBot created to help you.",

# "What can you do?",
# "I can chat, answer questions, and help you with Python, Flask, and general stuff.",

# "Your name?",
# "You can call me ChatBot!",

# "Where are you from?",
# "I'm from your computer 😉",

# "Do you know Python?",
# "Yes! I know Python very well.",

# "Do you know Django?",
# "Yes, I can help with Django too.",

# "Do you know Flask?",
# "Of course! I can guide you in Flask.",

# "What about databases?",
# "I can help with MongoDB and SQL basics.",

# "Do you know OpenCV?",
# "Yes, I can help with image and video processing.",

# "What is OCR?",
# "Optical Character Recognition – it reads text from images.",

# "Do you know Tesseract?",
# "Yes! It's used for OCR in Python.",

# "Can you recognize faces?",
# "Yes, using DeepFace or OpenCV we can detect and recognize faces.",

# "Tell me about yourself",
# "I'm a friendly ChatBot ready to assist you in coding and general questions.",

# "How old are you?",
# "I'm timeless 😎",

# "Do you like coding?",
# "Yes! Coding is fun.",

# "What's your favorite language?",
# "I love Python, of course!",

# "Teach me Python",
# "Sure! What do you want to learn?",

# "How to create a virtual environment?",
# "Use python -m venv venv and then activate it.",

# "How to install packages?",
# "Run pip install package_name or pip install -r requirements.txt.",

# "Can you help me with Flask?",
# "Yes, I can help you build web apps using Flask.",

# "Can you help me with Django?",
# "Sure! I can guide you with Django models, views, and templates.",

# "Do you know JavaScript?",
# "A little! I can help with basic JS for web apps.",

# "Can you make my website interactive?",
# "Yes, using JS, HTML, and CSS we can make it interactive.",

# "Do you know Bootstrap?",
# "Yes! Bootstrap helps make responsive websites easily.",

# "Can you make forms?",
# "Sure, I can help with HTML forms and Flask backend.",

# "How to store data?",
# "You can use MongoDB or SQL databases.",

# "How to read data from database?",
# "Use pymongo for MongoDB or SQL queries for SQL databases.",

# "How to capture image from camera?",
# "Use OpenCV in Python to capture frames from camera.",

# "How to detect objects?",
# "OpenCV can detect shapes, faces, or objects in images or video.",

# "How to detect face?",
# "Use Haar cascades or DeepFace for face detection.",

# "How to compare faces?",
# "DeepFace can compare two face images and check similarity.",

# "What is DeepFace?",
# "A Python library for face recognition and verification.",

# "How to extract text from images?",
# "Use Tesseract OCR to extract text from images.",

# "How to make chatbot talk?",
# "Use pyttsx3 or gTTS to convert text to speech.",

# "Can you understand voice?",
# "Yes! With AssemblyAI or Speech Recognition we can transcribe voice.",

# "How to send WhatsApp messages?",
# "Use WhatsApp Cloud API or Twilio API to send messages.",

# "Can you send images on WhatsApp?",
# "Yes! Upload the image and send using API.",

# "Do you know Twilio?",
# "Yes! Twilio helps in sending messages, calls, and WebSockets.",

# "What is WebSocket?",
# "A WebSocket allows real-time communication between client and server.",

# "Can you show live camera in web app?",
# "Yes! Using OpenCV and Flask, you can stream camera to browser.",

# "How to save image captured?",
# "Use cv2.imwrite() to save captured images.",

# "How to detect motion?",
# "Compare frames with cv2.absdiff() to detect movement.",

# "Can you make charts?",
# "Yes! Use Chart.js or Python libraries like matplotlib.",

# "Can you send email?",
# "Yes! Use SMTP or services like SendGrid.",

# "How to make chatbot smart?",
# "Train it with lots of Q-A pairs.",

# "What is a Q-A pair?",
# "It's a question and answer that the bot learns from.",

# "Can you remember things?",
# "Yes! I can remember previous messages in session.",

# "How to reset chatbot memory?",
# "Just restart the bot or clear the session.",

# "Can you answer general questions?",
# "Yes! Ask me anything.",

# "Who is Elon Musk?",
# "He is the CEO of SpaceX and Tesla.",

# "What is AI?",
# "Artificial Intelligence – machines that can think or learn.",

# "What is machine learning?",
# "A subset of AI where machines learn from data.",

# "What is deep learning?",
# "Neural networks with multiple layers learning from data.",

# "Do you know Flask routing?",
# "Yes! Use @app.route('/path') to define routes.",

# "Do you know Django views?",
# "Yes! Django views handle HTTP requests and responses.",

# "How to run Flask server?",
# "Use app.run() in your Python script.",

# "How to run Django server?",
# "Use python manage.py runserver.",

# "How to create templates?",
# "Use HTML files with Jinja2 syntax in Flask.",

# "How to create forms in Django?",
# "Use Django forms or ModelForms.",

# "How to handle POST request?",
# "Access form data with request.form in Flask or request.POST in Django.",

# "How to validate input?",
# "Check values and use regex or form validators.",

# "How to show alert in HTML?",
# "Use Bootstrap alert classes.",

# "How to make button click?",
# "Use <button> and attach JS function to onclick.",

# "How to show loading spinner?",
# "Use Bootstrap spinner or custom CSS animation.",

# "How to make website responsive?",
# "Use CSS flex, media queries, or Bootstrap grid.",

# "How to handle errors?",
# "Use try-except in Python and error pages in web app.",

# "How to create admin panel?",
# "Create separate routes or pages for admin access only.",

# "How to restrict users?",
# "Use login system and role check.",

# "How to login user?",
# "Authenticate username and password and create session.",

# "How to logout user?",
# "Clear session or token.",

# "How to store password securely?",
# "Use hashing like hashlib or passlib.",

# "What is session?",
# "A session keeps user data while logged in.",

# "How to fetch data from MongoDB?",
# "Use collection.find() to get records.",

# "How to insert data in MongoDB?",
# "Use collection.insert_one() or insert_many().",

# "How to update data in MongoDB?",
# "Use collection.update_one() with filter and update.",

# "How to delete data in MongoDB?",
# "Use collection.delete_one() or delete_many().",

# "How to sort data?",
# "Use sort() method in MongoDB or Python list.",

# "How to filter data?",
# "Use find() with conditions or Python filters.",

# "How to create index?",
# "Use create_index() for faster searches in MongoDB.",

# "How to handle large data?",
# "Use pagination or limit queries.",

# "How to schedule tasks?",
# "Use Python sched, APScheduler, or cron jobs.",

# "How to backup database?",
# "Use mongodump for MongoDB.",

# "How to restore database?",
# "Use mongorestore for MongoDB.",

# "How to capture photo on button click?",
# "Send POST request to Flask route that saves camera frame.",

# "How to compare face with stored image?",
# "Use DeepFace.verify(live_image, stored_image).",

# "How to prevent duplicates?",
# "Check existing records before insert.",

# "How to calculate date difference?",
# "Use datetime module in Python.",

# "How to sort table in HTML?",
# "Use JavaScript or backend sorting.",

# "How to search table?",
# "Use JavaScript filter or backend query.",

# "How to add pagination?",
# "Split results into pages using backend or JS.",

# "How to upload file?",
# "Use <input type='file'> and request.files in Flask.",

# "How to validate file type?",
# "Check extension and MIME type.",

# "How to limit file size?",
# "Check file.size in JS or server-side.",

# "How to convert image to base64?",
# "Use base64.b64encode() in Python or JS.",

# "How to display image in HTML?",
# "Use <img src='data:image/jpeg;base64,...'>.",

# "How to remove background?",
# "Use OpenCV segmentation or thresholding.",

# "How to detect edges?",
# "Use cv2.Canny() in OpenCV.",

# "How to resize image?",
# "Use cv2.resize() to adjust dimensions.",

# "How to rotate image?",
# "Use cv2.getRotationMatrix2D() and cv2.warpAffine().",

# "How to draw rectangle?",
# "Use cv2.rectangle() with coordinates.",

# "How to draw text?",
# "Use cv2.putText() on image.",

# "How to measure FPS?",
# "Calculate time per frame using time module.",

# "How to handle multiple users?",
# "Create separate sessions or identify by user id.",

# "How to send JSON response?",
# "Use jsonify() in Flask or return JsonResponse in Django.",

# "How to read JSON request?",
# "Use request.get_json() in Flask.",

# "How to detect face in real-time?",
# "Use OpenCV video capture with face cascade or DeepFace detector.",

# "How to check similarity between faces?",
# "DeepFace gives distance and confidence score.",

# "How to use regex in Python?",
# "Use re module to search, match, or find patterns.",

# "How to remove special characters?",
# "Use regex substitution re.sub().",

# "How to convert string to int?",
# "Use int(string).",

# "How to convert int to string?",
# "Use str(number).",

# "How to split text?",
# "Use text.split(' ') or any delimiter.",

# "How to join list to string?",
# "Use 'separator'.join(list).",

# "How to sort list?",
# "Use sorted(list) or list.sort().",

# "How to remove duplicates from list?",
# "Use set(list) or dict.fromkeys(list).",

# "How to reverse list?",
# "Use list[::-1] or reversed(list).",

# "How to check if item exists?",
# "Use 'item in list'.",

# "How to get length?",
# "Use len(list) or len(string).",

# "How to create dictionary?",
# "Use dict = {'key':'value'}.",

# "How to access dictionary value?",
# "Use dict['key'].",

# "How to update dictionary?",
# "Use dict['key'] = new_value.",

# "How to delete dictionary key?",
# "Use del dict['key'].",

# "How to iterate dictionary?",
# "Use for key, value in dict.items():",

# "How to handle exceptions?",
# "Use try-except blocks.",

# "How to raise exception?",
# "Use raise Exception('message').",

# "How to write function?",
# "Use def function_name(parameters):",

# "How to return from function?",
# "Use return value.",

# "How to import module?",
# "Use import module_name.",

# "How to install module?",
# "Use pip install module_name.",

# "How to create class?",
# "Use class ClassName: and define methods.",

# "How to create object?",
# "obj = ClassName().",

# "How to access object method?",
# "obj.method_name().",

# "How to inherit class?",
# "Use class Child(Parent):",

# "How to override method?",
# "Define method in child class with same name.",

# "How to use super()?",
# "Call super().method() to access parent method.",

# "How to use loops?",
# "Use for or while loops in Python.",

# "How to break loop?",
# "Use break statement.",

# "How to continue loop?",
# "Use continue statement.",

# "How to use if condition?",
# "Use if, elif, else blocks.",

# "How to use logical operators?",
# "Use and, or, not in conditions.",

# "How to compare values?",
# "Use ==, !=, >, <, >=, <=.",

# "How to create list of numbers?",
# "Use list(range(start, end)).",

# "How to create set?",
# "Use set([items]).",

# "How to add to set?",
# "Use set.add(item).",

# "How to remove from set?",
# "Use set.remove(item).",

# "How to check in set?",
# "Use item in set.",

# "How to merge sets?",
# "Use set1.union(set2).",

# "How to create tuple?",
# "Use tuple([items]) or (a, b, c).",

# "How to access tuple?",
# "Use tuple[index].",

# "How to slice tuple?",
# "Use tuple[start:end].",

# "How to count elements?",
# "Use list.count(item) or tuple.count(item).",

# "How to find index?",
# "Use list.index(item).",

# "How to convert tuple to list?",
# "Use list(tuple).",

# "How to convert list to tuple?",
# "Use tuple(list)."

# ])


