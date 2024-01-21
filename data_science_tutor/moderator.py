from openai import OpenAI



moderation_model = 'text-moderation-latest'
client = OpenAI(
    # Read the OpenAI API key from the environment variable
    # api_key = os.environ.get('OPENAI_API_KEY')
    api_key="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"
)


def moderator(prompt:str):
    response = client.moderations.create(
        input= prompt,
        model= moderation_model,
    )

    return response.results[0].flagged
