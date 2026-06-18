from flask import Flask, request, render_template
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

app = Flask(**name**)

PROJECT_ENDPOINT = "https://pcitassist.services.ai.azure.com/api/projects/pcitassist-proj"
AGENT_NAME = "PrimeCloudara-IT-Assist"
AGENT_VERSION = "4"

@app.route("/", methods=["GET", "POST"])
def home():

```
answer = ""
question = ""

if request.method == "POST":

    question = request.form.get("question", "")

    try:
        project_client = AIProjectClient(
            endpoint=PROJECT_ENDPOINT,
            credential=DefaultAzureCredential(),
        )

        openai_client = project_client.get_openai_client()

        response = openai_client.responses.create(
            input=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            extra_body={
                "agent_reference": {
                    "name": AGENT_NAME,
                    "version": AGENT_VERSION,
                    "type": "agent_reference"
                }
            }
        )

        answer = response.output_text

    except Exception as ex:
        answer = f"Error: {str(ex)}"

return render_template(
    "index.html",
    response=answer,
    question=question
)
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=8000)
