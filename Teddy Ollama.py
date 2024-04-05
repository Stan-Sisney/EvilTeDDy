import ollama
ollama.pull('mistral')
stream = ollama.chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'do you like Mozart?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True) 