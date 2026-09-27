import os
from openai import OpenAI

# Initialize client pointing to xAI's API endpoint
client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1",
)

with open("changes.diff", "r") as f:
  changes = f.read()

prompt = f"""
You are a DevOps engineer performing a Pull Request review.

Review the following code changes specifically for:

1. CI/CD problems
2. Docker issues
3. Kubernetes issues
4. Security problems
5. Infrastructure-as-Code problems
6. DevOps best practices

Do NOT rewrite the entire code.

Return:
- Critical issues
- High-priority issues
- Recommendations
- Positive observations

Keep the review practical and concise.

CODE CHANGES:
{changes}
"""

# Call Grok using the Chat Completions endpoint
response = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {"role": "system", "content": "You are an expert DevOps engineer."},
        {"role": "user", "content": prompt},
    ],
    temperature=0.2,
)

review = response.choices[0].message.content

with open("ai-review.md", "w") as f:
  f.write("# AI DevOps Review (Grok)\n\n")
  f.write(review)