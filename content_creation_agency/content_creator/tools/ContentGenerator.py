from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ContentGenerator(BaseTool):
    """
    A tool for generating content using OpenAI's GPT-4 model based on trends and insights.
    """
    
    content_type: str = Field(
        ..., 
        description="Type of content to generate: 'caption', 'hashtags', or 'ideas'"
    )
    
    insights: str = Field(
        ..., 
        description="Insights and trends to base the content on"
    )
    
    tone: str = Field(
        default="professional",
        description="Desired tone of the content"
    )

    def run(self):
        """
        Generates content using GPT-4 based on provided insights
        """
        prompt_templates = {
            'caption': """Based on these insights and trends:
                {insights}
                Generate an engaging Instagram caption with a {tone} tone.
                Include emojis where appropriate.""",
            'hashtags': """Based on these insights and trends:
                {insights}
                Generate a list of 15-20 relevant hashtags for Instagram.
                Mix popular and niche hashtags for better reach.""",
            'ideas': """Based on these insights and trends:
                {insights}
                Generate 5 content ideas for Instagram posts.
                Include visual suggestions and caption themes."""
        }
        
        prompt = prompt_templates[self.content_type].format(
            insights=self.insights,
            tone=self.tone
        )
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional social media content creator."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content

if __name__ == "__main__":
    generator = ContentGenerator(
        content_type="caption",
        insights="Digital marketing posts with carousel formats get 3x more engagement. Top trending topics: AI tools, productivity hacks.",
        tone="professional"
    )
    print(generator.run()) 