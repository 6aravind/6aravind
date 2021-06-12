# Import libraries
import feedparser
import pandas as pd
from bs4 import BeautifulSoup
import unicodedata

# Config
MEDIUM_RSS = 'https://medium.com/feed/@6aravind'
INFO_REQ = ['title', 'link', 'tags', 'published', 'content']
MEDIUM_ENTRIES = 'entries'
DATA_FILE = 'all_posts.csv'


# Extract only the require data from the feed
def parse_post():
   # Parse the RSS Feed
   feed = feedparser.parse(MEDIUM_RSS)
   posts = feed.get(MEDIUM_ENTRIES)
   
   nrOfPosts = len(posts)
   details = [None] * nrOfPosts

   for index, post in enumerate(posts):
      details[index] = {} 
      for key in INFO_REQ:
         if key == 'tags':
            details[index][key] = ",".join(list(map(lambda x: x['term'], post[key])))
         elif key == 'content':
            soup = BeautifulSoup(post[key][0]['value'], 'html.parser')
            details[index]['intro'] = unicodedata.normalize("NFKD", soup.find_all('h4')[0].get_text(strip=True))
            details[index]['image'] = soup.find_all('img')[0]['src']
         else:
               details[index][key] = post[key]
   return details



if __name__ == "__main__":
   # Add the new data to the old one
   details = parse_post() 
   new_df = pd.DataFrame(details)

   # Read existing posts
   df = pd.read_csv(DATA_FILE)
   final_df = pd.concat([new_df, df], ignore_index=True).drop_duplicates().reset_index(drop=True)

   # Write to file
   print(f'Nr of posts: {len(final_df)}')
   final_df.to_csv(DATA_FILE, index=False)