#  Event RSVP System with Ticketing & Payment Integration

Just a quick little project I made while practicing Django and backend development.
This is part of my journey as I learn and improve my skills.

---

##  Objective

Enhance the event system to support ticket booking, payment processing, and digital ticket generation.

---

##  What This Project Covers

-  Integrate a payment gateway (e.g., Stripe) for processing event ticket payments
-  Generate digital tickets with QR codes upon successful booking
-  Manage attendee lists and send email confirmations

---

##  Key Learnings

- Payment gateway integration (Stripe)
- Secure transaction handling
- QR code generation
- Asynchronous background processing (Celery)
- Real-world project architecture in Django

---

##  About the Project

This Event RSVP System lets users book event tickets, pay securely online, and receive digital tickets with QR codes. It manages attendee lists and sends email confirmations automatically. The project focuses on real-world skills like payment gateway integration, secure transactions, and dynamic ticket generation.

---

##  Features

-  Stripe integration for secure payment processing
-  Auto-generated digital QR code tickets after purchase
-  Manage RSVP attendee list per event
-  Send confirmation emails to users
-  Background task handling using Celery and Redis
-  Stripe webhook integration for live payment events

---

##  Technologies Used

- Python
- Django
- Celery
- Redis
- Stripe API
- HTML, CSS, JavaScript
- Bootstrap

---

##  About Me

Hi, I'm Ashkan — a junior Django developer who recently transitioned from teaching English as a second language to learning backend development.
I’m currently focused on improving my skills, building projects, and looking for opportunities to work as a backend developer.

- [My GitHub](https://github.com/AsHkAn-Django)
- [LinkedIn](https://www.linkedin.com/in/ashkan-ahrari-146080150)

---

##  How to Use

1. **Clone the repository**

```bash
git clone https://github.com/AsHkAn-Django/event-rsvp.git
cd event-rsvp
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Run initial setup**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Start the Django server**

```bash
python manage.py runserver
```

---

## 🧪 Tutorial: Stripe Webhook Setup

### For getting `STRIPE_WEBHOOK_SECRET`:

```bash
docker run --rm -it stripe/stripe-cli:latest login

docker run --rm -it --network host \
  -v $HOME/.stripe:/root/.config/stripe \
  stripe/stripe-cli:latest listen --forward-to localhost:8000/payment/webhook/
```

---

##  Running Services — Open 4 Terminals

### 1. Django server

```bash
python manage.py runserver
```

### 2. Redis server

```bash
redis-server
```

### 3. Celery worker

```bash
celery -A eventRsvpSystem worker --loglevel=info
```

### 4. Stripe webhook

```bash
docker run --rm -it --network host \
  -v $HOME/.stripe:/root/.config/stripe \
  stripe/stripe-cli:latest listen --forward-to localhost:8000/payment/webhook/
```

---

