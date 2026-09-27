import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
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

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

review = response.output_text

with open("ai-review.md", "w") as f:
    f.write("# AI DevOps Review for CI CD\n\n")
    f.write(review)