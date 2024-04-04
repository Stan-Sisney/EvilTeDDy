import ollama
ollama.pull('phi')
stream = ollama.chat(
    model='phi',
    messages=[{'role': 'user', 'content': 'do yhou like Mozart?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)