from django.shortcuts import render
import requests

def get_html_content(request):
    recipe = request.GET.get('recipe')
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.allrecipes.com/recipe/{recipe}').text
    return html_content

def home(request):
    result = None
    if 'recipe' in request.GET:
        html_content = get_html_content(request)
        print(html_content)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
      
    return render(request, 'index.html', {'result': result})