from scraper.views import scrape_news
from django.core.management.base import BaseCommand
from scraper.models import Headlines
import datetime
class Command(BaseCommand):
    help = "Scrapes headlines from BBC and saves to DB"
    def handle(self,*args,**kwargs):
        self.stdout.write("Scraping Start headlines from BBC")
        scraped_data = scrape_news()

        for data in scraped_data:
            title = data[0]
            url = data[1]
            if not Headlines.objects.filter(title=title).exists():
                Headlines.objects.create(
                    title=title,
                    url = url,
                    scraped_at = datetime.datetime.now())
            else:
                self.stdout.write("Headline already exists")
        self.stdout.write("Scraping Complete")
