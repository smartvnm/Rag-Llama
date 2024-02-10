from duckduckgo_search import DDGS
from trafilatura import fetch_url, extract

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
        print(r[title])