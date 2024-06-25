import os
import cohere

os.environ["COHERE_API_KEY"] = "QaJSGNQPoXnHLnTFOWDAsPvtGCNlq1ViKLOvkst5"

cohere_api_key = os.getenv('COHERE_API_KEY')
cohere_client = cohere.Client(api_key=cohere_api_key)

system_message = "You are Michael Jordan."
human_message = "Which shoe manufacturer are you associated with?"

prompt = f"{system_message}\nHuman: {human_message}\nAI:"

response = cohere_client.generate(
    model='command-xlarge-nightly',
    prompt=prompt,
    max_tokens=500,
    stop_sequences=["Human:", "AI:"]
)

print(response.generations[0].text.strip())