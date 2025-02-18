from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd
from pandasai import SmartDataframe
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv

load_dotenv()

PANDAS_AI_API_KEY = os.getenv("PANDAS_AI_API_KEY")

class TrendAnalyzer(BaseTool):
    """
    A tool for analyzing Instagram data using PandasAI to extract insights and trends.
    """
    
    dataframe: pd.DataFrame = Field(
        ..., 
        description="The pandas DataFrame containing Instagram data to analyze"
    )
    
    analysis_query: str = Field(
        ..., 
        description="Natural language query describing the analysis to perform"
    )

    def run(self):
        """
        Analyzes the data using PandasAI and returns insights
        """
        # Initialize PandasAI with SmartDataframe
        smart_df = SmartDataframe(self.dataframe, config={"api_key": PANDAS_AI_API_KEY})
        
        # Run analysis
        result = smart_df.chat(self.analysis_query)
        
        return str(result)

if __name__ == "__main__":
    # Create sample DataFrame
    data = {
        'likes': [100, 200, 300],
        'comments': [10, 20, 30],
        'timestamp': ['2023-01-01', '2023-01-02', '2023-01-03']
    }
    df = pd.dataframe(data)
    
    analyzer = TrendAnalyzer(
        dataframe=df,
        analysis_query="What is the average number of likes and comments?"
    )
    print(analyzer.run()) 