# Real-Time-Feed-Subscription-System
# Overview
This Django project implements a real-time feed subscription system using Django Rest Framework, Django Channels, and the Binance WebSocket API. Users can register, log in, subscribe to a live feed channel, and receive real-time updates through WebSocket connections.

# Features
User registration and login
Channel subscription for live feed updates
Real-time WebSocket integration with Binance API
Scalable design for handling concurrent users
User logout with token blacklisting
Live feed data retrieval and display
# Technologies Used
Python
Django
Django Rest Framework
Django Channels
Binance WebSocket API
Websockets library
Django Rest Framework SimpleJWT
# Project Structure
plaintext
Copy code
django_assignment/
|-- feeds/
|   |-- migrations/
|   |-- static/
|   |-- templates/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- consumers.py
|   |-- models.py
|   |-- routing.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- django_assignment/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- .gitignore
|-- manage.py
|-- requirements.txt
|-- README.md
# Installation
# Clone the repository:
git clone https://github.com/staufique/Real-Time-Feed-Subscription-System.git
cd django_assignment

# Create a virtual environment:
python -m venv venv
Activate the virtual environment:

# Windows:
venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt

# Apply migrations:
python manage.py makemigrations
python manage.py migrate

# Run the development server:
python manage.py runserver
The project will be accessible at http://localhost:8000/.


# to get live on rest api first connect to websocket 
ws://localhost:8000/ws/live-feed/


# Usage
Register a new user at http://localhost:8000/register/.
Log in with the registered user credentials at http://localhost:8000/login/.
Subscribe to the live feeds channel at http://localhost:8000/channel-subscription/.
Access real-time live feed updates at http://localhost:8000/live-feed/.
Logout with the given token at http://localhost:8000/logout/.
Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Follow the project's coding standards and guidelines.

License
This project is licensed under the MIT License.

Replace your_project and your_username with your actual project and GitHub username. Adjust the sections as needed, and provide more detailed instructions if necessary. Don't forget to include a LICENSE file if you haven't already.
