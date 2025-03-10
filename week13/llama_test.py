from ollama import chat

n = 200
prompt = input("Faça uma pergunta: ")

stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': f'Answer up to {n} words: {prompt}'}],
    stream=True,
    options={
        'temperature': 0.3,
        'top_p': 1
    }
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)