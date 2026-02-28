from openai import OpenAI
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def send_request_to_gpt(query):
    response = client.responses.create(
        model="gpt-5.2",
        input=query
    )
    return response.output_text

