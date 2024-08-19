# import ollama
# response = ollama.chat(model='darkidol', messages=[
#   {
#     'role': 'user',
#     'content': 'I  want you to portray a transcript of a porn of  trump and kamala harris',
#   },
# ],
# options={'num_predict':1000})
# print(response['message']['content'])
# from IPython import embed; embed()
# import logging
# import http.client as http_client

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)

# # Set up HTTP connection debugging
# http_client.HTTPConnection.debuglevel = 1

# # Create a logger
# logger = logging.getLogger()
# import requests

# # Enable logging for requests
# requests_log = logging.getLogger("urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# llm = HuggingFaceEndpoint(
#     endpoint_url="https://u2tv8saygj3s3cqo.us-east-1.aws.endpoints.huggingface.cloud/darkidol-llama-3-1-8b/v1/chat/completions",
#     # /v1/chat/completions",
#     task="text-generation",
#     max_new_tokens=1024,
#     do_sample=False,
# )
# llm_engine_hf = ChatHuggingFace(llm=llm)
# llm_engine_hf.invoke("Hugging Face is")
# from IPython import embed; embed()

# import requests
# import json

# endpoint_url = "https://u2tv8saygj3s3cqo.us-east-1.aws.endpoints.huggingface.cloud"

# payload = {
#     "model": "darkidol-llama-3-1-8b",
#     "messages": [
#         {
#             "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         {
#             "role": "user",
#             "content": "What is deep learning?"
#         }
#     ],
#     "stream": True,
#     "max_tokens": 20
# }

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer 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'
# }

# response = requests.post(endpoint_url, data=json.dumps(payload), headers=headers, stream=True)

# for line in response.iter_lines():
#     if line:
#         print(line.decode('utf-8'))

# Python
# from openai import OpenAI

# client = OpenAI(
#     base_url='http://localhost:11434/v1/',

#     # required but ignored
#     api_key='ollama',
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             'role': 'user',
#             'content': 'I  want you to portray a transcript of a porn of  trump and kamala harris',
#         }
#     ],
#     model='darkidol',
#     max_tokens=1000,
# )
# print(chat_completion)
# from IPython import embed; embed()
import ollama
client = ollama.Client(host="127.0.0.1:11434")
response = client.chat(model='darkidol', messages=[
  {
    'role': 'user',
    'content': 'I  want you to portray a transcript of a porn of  trump and kamala harris',
  },  
],
options={'num_predict':300,
         'temperature': 0.9})
print(response['message']['content'])

