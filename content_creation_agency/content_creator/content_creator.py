from agency_swarm import Agent

class ContentCreator(Agent):
    def __init__(self):
        super().__init__(
            name="ContentCreator",
            description="Creates and manages social media content",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.7,
            max_prompt_tokens=25000,
        ) 