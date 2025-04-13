from django.shortcuts import render,redirect,HttpResponse
from scraper.scraper import BBCScraper,ScrapURLContent
from .models import Headlines
from django.core.paginator import Paginator
import csv
from django.utils.timezone import now
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    scraped_data = scrape_news()
    for data in scraped_data:
        title = data[0]
        url = data[1]
        if not Headlines.objects.filter(title=title).exists():
            Headlines.objects.create(
                user = request.user,
                title=title,
                url = url,
                scraped_at = datetime.datetime.now()

            )
    return render(request,"index.html",{
        'newsheadlines':scraped_data
    })

@login_required
def search_content(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        content = url_content(url)
        print(content)
        request.session['scraped_content'] = content
        return redirect('content')
    return render(request,"searchNews.html")

@login_required
def show_content(request):
    content = request.session.get('scraped_content','No content found')
    return render(request,"content.html",
                  {
                      'content':content
                  })
@login_required
def dashboard(request):
    all_jobs = Headlines.objects.filter(user=request.user).order_by("-scraped_at")
    paginator = Paginator(all_jobs,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total = all_jobs.count()
    last_run = all_jobs.latest('scraped_at') if total > 0 else None
    context = {
        "jobs" : page_obj,
        "total" : total,
        "last_run" : last_run
    }
    return render(request,'dashboard.html',context)


@login_required
def export_csv(request):
    headlines = Headlines.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="scraping_history.csv'
    writer = csv.writer(response)
    writer.writerow(['Title','Link','Scraped_at'])
    for headline in headlines:
        writer.writerow([headline.title,headline.url,headline.scraped_at])
    return response

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username = email,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Invalid credentials")
    return render(request,"login.html")

def signup_user(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname') or ""
        last_name = request.POST.get('lastname') or ""
        email = request.POST.get('email')
        if User.objects.filter(username=email).exists():
            return HttpResponse("User with this email already exist.")
        password = request.POST.get('password')
        confirmPassword = request.POST.get("confirmPassword")
        if password != confirmPassword:
            return HttpResponse("<h1>Password not match with confirm Password.</h1>")
        user = User.objects.create_user(username=email,first_name=firstname,last_name=last_name,email=email,password=password)
        user.save()
        return redirect('login')
    return render(request,"signup.html")

def logout_user(request):
    logout(request)
    return redirect('login')
def scrape_news():
    news = BBCScraper()
    news.fetch_data()
    news.scrape_headlines()
    return news.all_links

def url_content(url):
    article = ScrapURLContent(url)
    article.fetch_data()
    article.scrap_url_content()
    return article.all_content
