from litellm import completion

# Set up the model configuration
model_name = "huggingface/darkidol-llama-3-1-8b"
api_base = "https://u2tv8saygj3s3cqo.us-east-1.aws.endpoints.huggingface.cloud"
api_key = "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"  # Replace with your actual API key

def query_model(prompt):
    try:
        response = completion(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            api_base=api_base,
            api_key=api_key
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
prompt = "I want you to behave like the worst version of a trump supporter and rant about white liberals"
result = query_model(prompt)
print(result)