from duckduckgo_search import DDGS
import shutil
import os
from trafilatura import fetch_url, extract
if os.path.exists('/content/docs'):
    shutil.rmtree('/content/docs')
os.mkdir('/content/docs')
with DDGS() as ddgs:
    keywords = 'Ukraine'
    ddgs_news_gen = ddgs.news(
      keywords,
      region="wt-wt",
      safesearch="off",
      timelimit="m",
      max_results=5
    )
    for r in ddgs_news_gen:
        if r['title'] is not None:
          title = r['title']
        else: 
          title = 'NoTitle'
        url = r['url']
        downloaded = fetch_url(url)
        if downloaded is not None:
          result = extract(downloaded)
          if result is not None:
          
            fname = title.replace('.',' ').replace(' ','_')
            print(fname)
            with(open('/content/docs/'+fname+'.txt','w')) as f:
              f.write(result)