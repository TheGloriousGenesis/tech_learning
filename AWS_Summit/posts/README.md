# AWS Summit 2025

tags: genai, aws, deployment


## AWS - Transforming foundation models to domain models

> [!NOTE]
> Encoder / Decoder (takes words and predicts output most likely) (embeddings capture semantic meaning of text)

### Option 1: Continued pretraining

Continued pretraining is when llms learn domain specific topics. Foundational models are initially trained on non domain specific data 
and amazon bedrock allows customisation of many foundational models.

Pros:
- Takes all types of documentation. 
- Ingest huge data. 
- Data doesn't have to be labelled! Can be unlabelled data

Cons:
- Has high cost
- Needs 1000s/1000000s training data

### Option 2: Fine-tuning

Fine tuning: Tuning a model to specific style or tone by providing labelled data, prompt and completion pairs.

Pros:
- Less expensive than continued pretraining
- Uses less data to train compared with continued pretraining (think 100/1000s prompts and completions)

Cons:
- Training data needs to be labelled

### Option 3: Give tools!

Tools help the base model access areas of knowledge in a more streamlined manner. Then base model can then consolidate the information.

- Prompt engineering:
- RAG: take all docs, slice into chunks (sematic chunks/ fixed token), generate embeddings, store embeddings in vector database, view closest embeddings and return result to you.
- Knowledge graphs

> [!TIP]
> Personal note: Could we create knowledge graphs or RAG from fast api documents?

### Option 4: use agents!

Agents can help execute the more complex parts of the task the base model might not have the expertise to do! And consolidate information from different areas all together!

## AWS - Future of AI

High investments asking for GenAI but no producing workloads

Enterprises that are successfully are very successful

Mckinsey - The State of AI (review)


digital
Wavestone - Data and AI executive leadership
Gartner - prediction for future of generative ai

Cultural changes remain in blocker in AI and Data at scale

Lack of alignment between business and data.

Data policies often seen as blockers

Newer model types expect less explainability, inconsistence output

Consumers know more, data is a service, give data and service is returned. Two way communication is required

Regulation is highly turning to need explainable model decisions

Inconsistent global standards

Cross broader ai needs proactive risk

Augmented workforce through Agentic AI systems

Agents can solve problems not just answer questions

If using agents, deploy low risk versions, enable traceability, auditing, explainable

Align ai to business goal

Make it aligned to something you need to do better (agents/genai works better with things poorly done, not with experts)

Everything is becoming data products


## AWS - Hands on Labs:

### Building and deploying apps 
AWS Cloud9
- helps to build applications via amazons Code IDE environment

AWS Bedrock

AWS Nova
```python
def call_nova(
    model,
    messages,
    system_message="",
    streaming=False,
    max_tokens=512,
    temp=0.7,
    top_p=0.99,
    top_k=20,
    tools=None,
    verbose=False,
):
    client = boto3.client("bedrock-runtime")
    system_list = [{"text": system_message}]
    inf_params = {
        "max_new_tokens": max_tokens,
        "top_p": top_p,
        "top_k": top_k,
        "temperature": temp,
    }
    request_body = {
        "messages": messages,
        "system": system_list,
        "inferenceConfig": inf_params,
    }
    if tools is not None:
        tool_config = []
        for tool in tools:
            tool_config.append({"toolSpec": tool})
        request_body["toolConfig"] = {"tools": tool_config}
    if verbose:
        print("Request Body", request_body)
    if not streaming:
        response = client.invoke_model(modelId=model, body=json.dumps(request_body))
        model_response = json.loads(response["body"].read())
        return model_response, model_response["output"]["message"]["content"][0]["text"]
    else:
        response = client.invoke_model_with_response_stream(
            modelId=model, body=json.dumps(request_body)
        )
        return response["body"]

def get_base64_encoded_value(media_path):
    with open(media_path, "rb") as media_file:
        binary_data = media_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode("utf-8")
        return base64_string


def print_output(content_text):
    display(Markdown(content_text))
```

Example nova call
```python
system_message = "Act as a creative writing assistant. When the user provides you with a topic, write a LinkedIn Launch Post about that topic."
messages = [
    {
        "role": "user",
        "content": [
            {"text": "Amazon Launches its newest foundational model - Amazon Nova!"}
        ],
    }
]
stream = call_nova(
    MICRO_MODEL_ID, messages, system_message=system_message, streaming=True
)

chunk_count = 0
start_time = datetime.now()
time_to_first_token = None
if stream:
    for event in stream:
        chunk = event.get("chunk")
        if chunk:
            # Print the response chunk
            chunk_json = json.loads(chunk.get("bytes").decode())
            # Pretty print JSON
            # print(json.dumps(chunk_json, indent=2, ensure_ascii=False))
            content_block_delta = chunk_json.get("contentBlockDelta")
            if content_block_delta:
                if time_to_first_token is None:
                    time_to_first_token = datetime.now() - start_time
                    print(f"Time to first token: {time_to_first_token}")

                chunk_count += 1
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
                # print(f"{current_time} - ", end="")
                print(content_block_delta.get("delta").get("text"), end="")
    print(f"Total chunks: {chunk_count}")
else:
    print("No response stream received.")
```


extract nutrition data from image

```python
nutrition_tool = {
    "name": "print_nutrition_info",
    "description": "Extracts nutrition information from an image of a nutrition label",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "calories": {
                    "type": "integer",
                    "description": "The number of calories per serving",
                },
                "total_fat": {
                    "type": "integer",
                    "description": "The amount of total fat in grams per serving",
                },
                "cholesterol": {
                    "type": "integer",
                    "description": "The amount of cholesterol in milligrams per serving",
                },
                "total_carbs": {
                    "type": "integer",
                    "description": "The amount of total carbohydrates in grams per serving",
                },
                "protein": {
                    "type": "integer",
                    "description": "The amount of protein in grams per serving",
                },
            },
            "required": [
                "calories",
                "total_fat",
                "cholesterol",
                "total_carbs",
                "protein",
            ],
        }
    },
}

system_message = "You are a helpful assistant and provide real time information related to a user query."
messages = [
    {
        "role": "user",
        "content": [
            {
                "image": {
                    "format": "png",
                    "source": {
                        "bytes": get_base64_encoded_value(
                            "images/getting_started_imgs/nutritional_benifits.png"
                        )
                    },
                }
            },
            {
                "text": "Please print the nutrition information from this nutrition label image"
            },
        ],
    }
]
model_response, _ = call_nova(
    LITE_MODEL_ID,
    messages,
    system_message=system_message,
    max_tokens=300,
    tools=[nutrition_tool],
    top_p=1,
    top_k=1,
    temp=1,
)

next(
    block["toolUse"]
    for block in model_response["output"]["message"]["content"]
    if "toolUse" in block
)
```

### 
## Nvidia

Optimising generative ai workload

### Problem framing

When thinking of using generative AI, think of the following:
- Is the right fit for the job?
- Compare with alternative Sustainable solutions
- Choice of where you deploy model (choose low carbon region if possibly)
- Choice of managed cloud services (helps reduce overhead and cost from unskilled usage)

### Base model selection

After selecting that genai is the best solution, then think of the following:
- Which model?
- Define model requirements
- Use sagemaker/Bedrock to test with small sample to see if it does what you need
- Llm leaderboard metrics
- share prompts (reduce workload!)
- Think about parameter efficiency : inject parameters only when needed
- If deciding to train from scratch : use optimised frameworks for training, clean dataset so its in the right form to learn from

### Model deployment

You have selected which model to use and now can implement it. Think of the following when doing so:
- Use optimised infrastructure to deploy deep learning models
- use deep learning containers/libraries for llms
- asynchronous endpoints that can scale
- Think about batch vs real time analytics (maybe switching between the two when business doesn't require real time?)

### Monitoring

The model is now deployed. These are the following things that should be considered after deployment:
- How is the model performing?
- Have targets for optimisation, and test out experiments/hypothesis (e.g using A,B experimentation)





