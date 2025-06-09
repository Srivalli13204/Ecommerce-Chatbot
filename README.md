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
- Home Page: http://127.0.0.1:8000/ ![Welcome Page](https://github.com/user-attachments/assets/9751afbc-a104-414f-9344-0cdd29a6e877)
- Chatbot: http://127.0.0.1:8000/chatbot/ ![Chatbot Page](https://github.com/user-attachments/assets/20929ef2-fca0-4d85-a1b1-2af25d16943b)
- Login: http://127.0.0.1:8000/accounts/login/ ![Login Page](https://github.com/user-attachments/assets/2997ea95-7cfd-4bce-adf4-1df6527903c5)
- Register: http://127.0.0.1:8000/accounts/register/ ![Register Page](https://github.com/user-attachments/assets/29dc6139-a516-4360-b38c-a189926bf7fd)

## Technology Stack
| Layer           | Tools & Frameworks                        |
|-----------------|-------------------------------------------|
| Frontend        | HTML, CSS, JavaScript                     |
| Backend         | Python, Django                            |
| API Framework	  | Django REST Framework (DRF)               |
| Auth System     |	Django Auth + JWT (SimpleJWT)             |
| Database	      | SQLite (pre-populated with mock products) |
| Deployment	    | Local (can be extended to Render/Heroku)  |

## Project Architecture

| ecommerce_bot/

├── chatbot/                → Main app for chatbot logic and views

│   ├── templates/          → HTML templates for chatbot & UI

│   ├── static/             → CSS/JS assets

│   ├── views.py            → Frontend/backend view logic

│   ├── urls.py             → Chatbot-specific routes

│   ├── models.py           → Product database model

│   └── serializers.py      → DRF serializers for API responses

├── accounts/               → Handles login and registration

├── ecommerce_bot/          → Project configuration and routing

├── db.sqlite3              → Mock database

└── manage.py               → Django command-line tool

## Sample Queries
- "Show me mobile phones"
- "Looking for headphones"
- "Do you have books?"
- "I want to buy shoes"

The chatbot uses basic keyword detection (e.g., 'laptop', 'shirt') to filter and display matching products.![Result](https://github.com/user-attachments/assets/9034663d-6227-4a62-ba73-fc0fc8bdb5af)


## Key features
- Secure login and registration
- Friendly chatbot interface with real-time responses
- Over 100 preloaded mock products
- Responsive UI across devices
- Search with partial keywords

## Challenges and Solutions
| Challenge                           | Solution Implemented                               |
|-------------------------------------|----------------------------------------------------|
| Handling unauthenticated access     | Used @login_required decorator for sensitive views |
| Managing static files and templates | Separated concerns into dedicated folders          |
| Styling user vs bot messages        | Used dynamic CSS classes for distinct visual representation |

## Future Scope
- Use NLP or LLM (like GPT) for semantic search
- Enable add-to-cart and checkout functionality
- Connect to a real-time product database
- Deploy on cloud hosting platforms

## Author
- Name: Pichika Parimala Durga Srivalli
- GitHub: Srivalli13204
- Email: isiri1320@gmail.com
