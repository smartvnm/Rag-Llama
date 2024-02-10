from duckduckgo_search import DDGS
import shutil
import os
from trafilatura import fetch_url, extract
if os.path.exists('/content/docs'):
    shutil.rmtree('/content/docs')
os.mkdir('/content/docs')
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
        if downloaded is not None:
          result = extract(downloaded)
          print(title)
          
          with(open('/content/docs/'+title+'.txt','w')) as f:
            f.write(result)