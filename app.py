import os
from openai import OpenAI

# 1. Initialize the client pointing to the free OpenCode inference server
client = OpenAI(
    base_url="https://opencode.ai/inference/v1",
    api_key="NOT_NEEDED_FOR_FREE_TIER"  # OpenCode allows free models without an explicit key local call
)

def get_completion(prompt, model="open/deepseek-v4.1-flash-free"):
    # 2. Package the message using standard roles
    messages = [{"role": "user", "content": prompt}]
    
    # 3. Fire the request out to the open-weights server
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# --- TEST THE PIPELINE ---
text = f"""
Clear and specific instructions give better outputs. \
Longer prompts provide more clarity and context. \
Do not confuse a clear prompt with a short prompt.
"""

prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""

print("Sending data to DeepSeek Free Tier...")
print(get_completion(prompt))
