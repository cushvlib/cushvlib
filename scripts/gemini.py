import os
import requests
import pysrt
import re

# Load subtitles
srt_directory = "/mnt/e/cushvlogs_srt"
srts = os.listdir(srt_directory)
srt_file = srts[0]

# Read and extract raw text from the SRT
subs = pysrt.open(os.path.join(srt_directory, srt_file))
srt_text = "\n".join(sub.text for sub in subs[:300])
print(srt_file)
# Gemini API settings
GEMINI_API_KEY = ""  # Replace with your actual API key
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

# Construct the request payload with full SRT text
data = {
    "contents": [{
        "parts": [{
            "text": f"""Reformat the following subtitle text into readable paragraphs. It should be styled like free-flowing prose or even poetry at times.
Do NOT remove any words, do NOT summarize, and do NOT change the order of the words. 
Simply break the text into paragraphs for easier reading. Prioritise SHORT, readable paragraphs.
Paragraphs should NOT be long.

Here is the subtitle text:

{srt_text}

Now, return the fully formatted text below:
"""
        }]
    }]
}

# Send the request
response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

# Parse response
if response.status_code == 200:
    output_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    print(output_text)
    
    # Save the formatted text for comparison
    with open("gemini_output.txt", "w", encoding="utf-8") as f:
        f.write(output_text)

else:
    print(f"Error: {response.status_code}, {response.text}")


import re

# Function to clean text (remove punctuation & normalize whitespace)
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
    return text

# Load the original SRT text
with open("gemini_output.txt", "r", encoding="utf-8") as f:
    formatted_text = f.read()

# Clean both the original & formatted text
original_words = clean_text(srt_text).split()
formatted_words = clean_text(formatted_text).split()
# Compare word order
if original_words == formatted_words:
    print("✅ The word order is preserved!")
else:
    print("❌ The word order has changed!")

# Debugging: Print differences if words are out of order
for i, (orig, formatted) in enumerate(zip(original_words, formatted_words)):
    if orig != formatted:
        print(f"Mismatch at word {i}: {orig} != {formatted}")
        break
