from bs4 import BeautifulSoup
import requests
#https://www.youtube.com/watch?v=tuI_Z6VolbE&t=1099s

url = input('digite a url: ')
def extract_title(content):
    soup = BeautifulSoup(content,"lxml")
    #pesquisa a primeira tag title que tenha um testo
    tag = soup.find("title",text=True)

    if not tag:
        return None

    return tag.string.strip()
#retona links http
def extract_links(content):
    soup = BeautifulSoup(content, "lxml")
    links = set()
    for tag in soup.find_all("a",href=True):
        if tag["href"].startswith("http"):
            links.add(tag["href"])
    return links    
#navega automaticamente pelas urls
def crawl (start_url):
    seen_urls = set([start_url])
    available_urls = set([start_url])
    numero = int(0)
    while available_urls:
        url = available_urls.pop()

        try:
            content=requests.get(url,timeout=3).text
        except Exception:
            continue

        title=extract_title(content)
        if title:
            print(title)
            print(url)
            numero = 1+ numero
            print('url acessadas ', numero)
            print()
        for link in extract_links(content):
            if link not in seen_urls:
                seen_urls.add(link)
                available_urls.add(link)
try: crawl(url)
except KeyboardInterrupt:
    print()
    print("Bye!")
#page = requests.get("https://www.python.org/")        
#title = extract_title("""
#links = extract_links(page.text)
#print('title:',title)
#for link in links:
#    print('link:',link)