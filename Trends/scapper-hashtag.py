from snscrape.modules import twitter
import json


hashtag = [input('Quel hashtag voulez-vous scrapper ? : ')]
max_results = 50
def scrape_hashtag(hashtag):
    scraper = twitter.TwitterHashtagScraper(hashtag)
    return scraper


for query in hashtag:
    output_filename = query.replace(" ", "_") + ".txt"
    with open(output_filename, 'w') as f:
        scraper = scrape_hashtag(query)
        i = 0
        for i, tweet in enumerate(scraper.get_items(), start = 1):
            tweet_json = json.loads(tweet.json())
            print (f"\nScraped tweet: {tweet_json['content']}")
            f.write(tweet.json())
            f.write('\n')
            f.flush()
            if max_results and i > max_results:
                break

