# E-Commerce Sales Chatbot

An intelligent chatbot system designed to enhance customer interaction in an e-commerce environment. Built using **Django**, **Django REST Framework**, and **HTML/CSS/JavaScript**, this chatbot simulates a conversational assistant that helps users search and explore products effectively.

---

## Project Summary

This chatbot allows users to:
- Authenticate via a secure login/register system
- Interact with a chatbot UI that accepts text queries
- Receive keyword-based product suggestions
- Explore product details and simulated search results

It mimics a real-world e-commerce assistant that helps streamline product discovery using a conversational interface.

---

## Objectives

- Create an intuitive chatbot interface for product exploration
- Integrate with a backend system that returns relevant product data from a mock inventory
- Maintain user session and interaction history

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Ecommerce-Chatbot.git
cd ecommerce_bot
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Access the app
- Home Page: http://127.0.0.1:8000/
- Chatbot: http://127.0.0.1:8000/chatbot/
- Login: http://127.0.0.1:8000/accounts/login/
- Register: http://127.0.0.1:8000/accounts/register/

## Technology Stack
| Layer           | Tools & Frameworks                        |
|-----------------|-------------------------------------------|
| Frontend        | HTML, CSS, JavaScript                     |
| Backend         | Python, Django                            |
| API Framework	  | Django REST Framework (DRF)               |
| Auth System     |	Django Auth + JWT (SimpleJWT)             |
| Database	      | SQLite (pre-populated with mock products) |
| Deployment	    | Local (can be extended to Render/Heroku)  |
