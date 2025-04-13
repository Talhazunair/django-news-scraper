import schedule
import time 
import os

def run_scraper():
    print("Running Scheduled Scraper...")
    os.system("python manage.py runscraper")

schedule.every(3).minutes.do(run_scraper)
print("Scheduler Started. Scraping every hour...")
while True:
    schedule.run_pending()
    time.sleep(1)
