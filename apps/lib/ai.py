import os
import openai
openai.api_key = "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"


class OpenAIClient:
    def __init__(self, model="gpt-3.5-turbo"): 
        self.model = model 

    def _request(self, message, role="user"):
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": role, "content": message}
            ]
        )
        return completion.choices[0].message

    def vacation_recommendation(self, location, start_date, end_date, interests): 

        message = f"""I would like travel recomenations. I 
        am visiting {location} from {start_date} to {end_date}. 
        Some of my interests are {interests.join(', ')}. What should I do"""

        return self._request(message)


 

