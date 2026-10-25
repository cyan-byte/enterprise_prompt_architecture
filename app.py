# This script is a synchronus API request loop
import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

# 1. Automatically load variables from your local .env file
_ = load_dotenv(find_dotenv())

# 2. Grab the API key securely
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("Missing GROQ_API_KEY in your .env file!")

# 3. Initialize the OFFICIAL Groq native developer client
client = Groq(api_key=api_key)

# 4. Use the active production-grade model identifier string
def get_completion(prompt, model="qwen/qwen3.8-27b"):
    messages = [{"role": "user", "content": prompt}]
    
    # Direct native execution pass
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    # Parse the data payload using the native Groq SDK structural path
    return response.choices[0].message.content

# --- TEST THE PIPELINE ---
lamp_review = """
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!!
"""

prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

print("Connecting to Groq Cloud using Native Production SDK...")
print("\nAI Response:")

try:
    print(get_completion(prompt))
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
