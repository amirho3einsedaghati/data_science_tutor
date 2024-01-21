# Import Dependencies
from openai import OpenAI
import os 



moderation_model = 'text-moderation-latest'
client = OpenAI(
    # Read the OpenAI API key from the environment variable
    api_key = os.environ.get('OPENAI_API_KEY')
)


# Check content for violations of OpenAI's usage policies.
def moderator(prompt:str):
    response = client.moderations.create(
        input= prompt,
        model= moderation_model,
    )

    return response.results[0].flagged
