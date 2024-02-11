import streamlit as st
from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)
from llama_index import set_global_tokenizer
from transformers import AutoTokenizer


# use Huggingface embeddings
from llama_index.embeddings import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)

llm = LlamaCPP(
    # You can pass in the URL to a GGML model to download it automatically
    model_url=None,
    # optionally, you can set the path to a pre-downloaded model instead of model_url
    model_path="/content/models/mistral-instruct-7b-2.43bpw.gguf",
    temperature=0.65,
   
    max_new_tokens=2024,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=2096,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 17},
    # transform inputs into Llama2 format
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)



# create vector store index

directory_path = '/content/docs'
documents = SimpleDirectoryReader(directory_path).load_data()
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)
query_engine = index.as_query_engine()
response = query_engine.query("Generate a detailed blog article from given context.")
print(response)

with(open('out.txt', 'w')) as f:
  f.write(response)

