
from openai import OpenAI


client = OpenAI(
    api_key='API_KEY'
)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Show me a description to seel the car {} {} {} in just 250 characters. 
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-4.1-nano'
    )

    return response.choices[0].message.content