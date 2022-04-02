from newsapi.newsapi_client import NewsApiClient
from inputcomm import inputCommand
from greeter import output


def news():
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    output("What topic you need the news about")
    topic = inputCommand()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    # count = len(newsData)
    n = 1
    for y in newsData:
        if n % 3 == 0:
            output("Do you want me to continue?")
            ans = inputCommand()
            if ans.lower() == 'no' or 'nope': 
                break
            else: 
                output(y["description"])
        output(y["description"])
        n+=1