# 📰 Django News Scraper

This is a web-based news scraping application built with Django. Each registered user can scrape news headlines, view their own scraping history, and export the results to a CSV file.

## 🚀 Features

- User authentication (Login & Signup)
- Scrape news headlines from BBC
- Track scraping history per user
- Paginated dashboard
- Export data to CSV
- Django admin support

## 🛠️ Installation

1. **Clone the repository**  
```bash
git clone https://github.com/Talhazunair/django-news-scraper.git
cd django-news-scraper
```

2. **Create a virtual environment and activate it**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the app**
```
http://127.0.0.1:8000/
```

## 🧪 Scraping via Custom Command

You can scrape headlines manually using:

```bash
python scraper_scheduler.py
```

## 📟 Export Headlines to CSV

From the dashboard, users can download their scraping history as a CSV file.

## 📂 Folder Structure

```
├── scraper/            # Main Django app
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, etc.)
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 👨‍💻 Author

- **Talha Zunair**
- GitHub: [@Talhazunair](https://github.com/Talhazunair)

## 📃 License

This project is open-source and free to use.

---

Feel free to customize or expand it as your project grows!

