from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[20:30, 17/8/2024] Aliyan: jo sunke coding ho sake?
[20:30, 17/8/2024] Hasnain: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 17/8/2024] Hasnain: ye
[20:30, 17/8/2024] Hasnain: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 17/8/2024] Aliyan: This is hindi
[20:31, 17/8/2024] Aliyan: send me some english songs
[20:31, 17/8/2024] Aliyan: but wait
[20:31, 17/8/2024] Aliyan: this song is amazing
[20:31, 17/8/2024] Aliyan: so I will stick to it
[20:31, 17/8/2024] Aliyan: send me some english song also
[20:31, 17/8/2024] Hasnain: hold on
[20:31, 17/8/2024] Aliyan: I know what you are about to send
[20:32, 17/8/2024] Aliyan: 😂😂
[20:32, 17/8/2024] Hasnain: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 17/8/2024] Aliyan: okok
[20:33, 17/8/2024] Hasnain: Haan
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named harry who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Harry"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)