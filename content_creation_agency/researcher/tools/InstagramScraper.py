from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
import requests
import pandas as pd
import json

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")

class InstagramScraper(BaseTool):
    """
    A tool for scraping Instagram data using Apify's Instagram Scraper actor.
    Can scrape hashtags, profiles, or search queries to gather engagement data and trends.
    """
    
    search_type: str = Field(
        ..., 
        description="Type of search to perform: 'hashtag', 'profile', or 'query'"
    )
    
    search_term: str = Field(
        ..., 
        description="The hashtag, profile name, or search query to scrape"
    )
    
    max_posts: int = Field(
        default=50,
        description="Maximum number of posts to scrape"
    )

    def run(self):
        """
        Runs the Instagram scraper and returns the data as a pandas DataFrame
        """
        # Prepare the actor input
        actor_input = {
            "searchType": self.search_type,
            "searchTerm": self.search_term,
            "resultsLimit": self.max_posts,
            "proxy": {
                "useApifyProxy": True
            }
        }
        
        # Call Apify API
        response = requests.post(
            'https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items',
            headers={'Authorization': f'Bearer {APIFY_API_TOKEN}'},
            json=actor_input
        )
        
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
            
        # Convert response to DataFrame
        data = response.json()
        df = pd.DataFrame(data)
        
        # Basic data cleaning and formatting
        if not df.empty:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values('timestamp', ascending=False)
            
        return df

if __name__ == "__main__":
    scraper = InstagramScraper(
        search_type="hashtag",
        search_term="artificialintelligence",
        max_posts=3
    )
    print(scraper.run()) 