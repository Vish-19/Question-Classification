from googlesearch import search
import urllib
import bs4
import re
from summarizer import textSummarizer
def results(query):
    l = []
    for j in search(query, num=5, stop=10, pause=2):
        l.append(j)
    url = l[0]
    source = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(source, 'lxml')
    text = ""
    for words in soup.find_all('p'):
        text += words.text
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\([0-9]*[a-z][A-Z]*\)', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'[ \n]+', ' ', text)
    # summarizer = pipeline("summarization")
    # summarizer(text, max_length = 100, do_sample=False)
    text = textSummarizer(text, 0.1)
    return text
