#pip install openai
import openai
openai.api_key = "your secret api key"
while True:
    model_engine = "text-davinci-003"
    prompt = input('Enter new prompt: ')
    if 'x' in prompt: # Exit condition
        break
    # Generate a response
    completion = openai.Completion.create( # Create completion object
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    response = completion.choices[0].text # Get response
    print(response)
