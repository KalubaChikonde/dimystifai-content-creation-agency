from agency_swarm import Agency
from content_creator.content_creator import ContentCreator
from researcher.researcher import Researcher

content_creator = ContentCreator()
researcher = Researcher()

agency = Agency(
    [
        content_creator,  # Content Creator will be the entry point
        [content_creator, researcher],  # Content Creator can communicate with Researcher
    ],
    shared_instructions="agency_manifesto.md",
    temperature=0.7,
    max_prompt_tokens=25000
)

if __name__ == "__main__":
    agency.run_demo() 