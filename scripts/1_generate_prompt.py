import ollama
import os
from dotenv import load_dotenv
from datetime import datetime

# 1. Define the message to the local model
load_dotenv()
messages  = [
    {"role": "system", "content": "You are a creative AI that generates lo-fi music concepts."},
    {"role":"user", "content": "Give me a unique, atmospheric lo-fi music theme."}
]

#2. Call Ollama's local model
response = ollama.chat(model = 'mistral', messages = messages)

#3. Extract and display the prompt
prompt = response['message']['content'].strip()
print("Generated prompt:", prompt)

#4. Save to latest.txt (overwrite)
os.makedirs("prompts", exist_ok = True)
with open("C:/Users/Nikhil Kapoor/lofi-ai-youtube/prompts/latest.txt", "w") as f:
    f.write(prompt)
print("Saved to prompts/latest.txt")

#5. Append to archive.txt with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("C:/Users/Nikhil Kapoor/lofi-ai-youtube/prompts/archive.txt", "a") as f:
    f.write(f"[{timestamp}] {prompt}\n")
print("Appended to prompts/archive.txt")