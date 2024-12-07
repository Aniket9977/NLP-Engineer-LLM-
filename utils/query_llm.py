from google.cloud import aiplatform

def query_llm(prompt, file_data):
    # Initialize Vertex AI client
    aiplatform.init(project="your-gcp-project-id", location="us-central1")

    # Combine prompt with extracted text and tables
    full_prompt = f"{prompt}\n\nExtracted Content:\nText:\n{file_data.get('text', '')}\nTables:\n{file_data.get('tables', [])}"

    # Predict using the GenAI model
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        instances=[{"content": full_prompt}],
        parameters={"temperature": 0.7, "max_output_tokens": 512},
    )

    return response.predictions[0]["content"]
