import os
from openai import OpenAI

# Groq uses the OpenAI library format via their free endpoint
client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
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

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are an expert DevOps engineer."},
        {"role": "user", "content": prompt},
    ],
    temperature=0.2,
)

review = response.choices[0].message.content

with open("ai-review.md", "w") as f:
  f.write("# 🤖 AI DevOps Review\n\n")
  f.write(review)
