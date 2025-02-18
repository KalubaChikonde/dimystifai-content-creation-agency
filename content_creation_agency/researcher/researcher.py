from agency_swarm import Agent

class Researcher(Agent):
    def __init__(self):
        super().__init__(
            name="Researcher",
            description="Researches social media trends and provides insights",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=25000,
        ) 