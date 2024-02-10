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

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)

llm = LlamaCPP(
    # You can pass in the URL to a GGML model to download it automatically
    model_url=None,
    # optionally, you can set the path to a pre-downloaded model instead of model_url
    model_path="/content/models/LLaMA-2-7B-32K-Q6_K.gguf",
    temperature=0.1,
   
    max_new_tokens=324,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=4096,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 32},
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
def get_file_metadata(filename):
  return {"filename": filename}

file_metadata = get_file_metadata
reader = SimpleDirectoryReader(directory_path, file_metadata=file_metadata)
    
documents = reader.load_data()
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)
print(type(documents))
for d in documents:
    index.insert(document = d, service_context = service_context)
query_engine = index.as_query_engine()
response = query_engine.query("Could you make a summary from the given context? Return your response which covers the key points of the text and do not miss anything important, please.")
print(response)



