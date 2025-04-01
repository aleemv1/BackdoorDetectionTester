import subprocess
from openai import OpenAI
from google import genai
import concurrent.futures
from tqdm import tqdm
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env file

# API configurations
GPT_API_KEY = os.getenv('GPT_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GPT_API_KEY or not GEMINI_API_KEY:
    raise ValueError("API keys must be set in environment variables")

# Model clients
gpt_client = OpenAI(api_key=GPT_API_KEY)
gemini_client = genai.Client(api_key=GEMINI_API_KEY)


def process_vulnerabilities(model_type="gpt", files = []):
    with open('instructions.txt', 'r') as instructions_file:
        for [file, content] in files:
            if model_type == "gpt":
                messages = [
                    {"role": "system", "content": instructions_file.read()},
                    {"role": "user", "content": content}
                ]
                response = gpt_client.chat.completions.create(model="gpt-4", messages=messages)
                # Get the response content
                response_content = response.choices[0].message.content
                print(response_content)
            else:
                wait_time = 2
                time.sleep(wait_time)
                response = gemini_client.models.generate_content(model="gemini-1.5-flash", contents="Instructions: " + instructions_file.read() + "\n\n" + "Input: " + content)
                print("File Name ", file)
                print(response.text)
            

    
def read_files():
    # Get all files from Tests directory recursively
    count = 1
    for root, dirs, files in os.walk('Tests'):
        folder_contents = []
        for file in files:
            if file.endswith('.py'):
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        # Convert Python file to txt content
                        input = [file, f.read()]
                        folder_contents.append(input)
                        # Print the file name
                except Exception as e:
                    print(f"Error reading file {file}: {str(e)}")
                    continue
        if folder_contents != []:
            print("--------------------------------")
            print("Testing Folder name: ", root)
            process_vulnerabilities("gemini", folder_contents)
            print("--------------------------------")
        count += 1


if __name__ == "__main__":
    read_files()