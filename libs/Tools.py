import json
import requests
from langchain.tools import tool
from crewai import Agent, Task , Crew
import http.client
from libs.llm import llm
import os
from dotenv import load_dotenv
key = os.getenv("GEMINI_API_KEY")
serper_key = "" #your serper api key .
browser_key = "" #Your Scraping Ant api key
llm = llm.Gemini #GPU intensive task

class SearchTools():

  @tool("Search internet")
  def search_internet(query):
    """Useful to search the internet about a given topic and return relevant
    results."""
    return SearchTools.search(query)


  def search(query, n_results=5):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': serper_key,
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    stirng = []
    for result in results[:n_results]:
      try:
        stirng.append('\n'.join([
            f"Title: {result['title']}", f"Link: {result['link']}",
            f"Snippet: {result['snippet']}", "\n-----------------"
        ]))
      except KeyError:
        next

    content = '\n'.join(stirng)
    return f"\nSearch result: {content}\n"
  


class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content, just pass a string with
    only the full url, no need for a final slash `/`, eg: https://google.com or https://clearbit.com/about-us"""
    conn = http.client.HTTPSConnection("api.scrapingant.com")
    key = browser_key
    conn.request("GET", f"/v2/extract?url={website}&x-api-key={key}&extract_properties=title%2C%20content")
    res = conn.getresponse()
    data = res.read()
    chunk = data.decode("utf-8")
    agent = Agent(
        role='Senior Researcher',
        goal=
        'Do amazing researches and summaries based on the content you are working with and find out useful functions and their uses for the coders to use',
        backstory=
        "You're a senior researcher at a big company and you need to research new functions , libraries and their uses based on the content you're provided with",
        llm=llm,
        allow_delegation=False)
    task = Task(
        agent=agent,
        description=
        f'Analyze and make a LONG summary the content bellow, make sure to include the ALL relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}',
        expected_output="Detailed functions and their uses from the scraped url"
      )
    summary = task.execute()
    content = "".join(summary)
    return f'\nScrapped Content: {content}\n'
