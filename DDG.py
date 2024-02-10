from duckduckgo_search import DDGS
import shutil
from trafilatura import fetch_url, extract

shut
with DDGS() as ddgs:
    keywords = 'artificial intelligence'
    ddgs_news_gen = ddgs.news(
      keywords,
      region="wt-wt",
      safesearch="off",
      timelimit="m",
      max_results=20
    )
    for r in ddgs_news_gen:
        title = r['title']
        url = r['url']
        downloaded = fetch_url(url)
        result = extract(downloaded)
        print(title)
        print(result)