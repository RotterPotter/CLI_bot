from openai import OpenAI


def gpt_check(sentense:str) -> str: 
  client = OpenAI()
  completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[{"role": 'user', "content": f"You are an English teacher. You need to check this sentense: '{sentense}'"}]
  )
  return completion.choices[0].message.content


