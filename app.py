import streamlit as st
from llama_cpp import Llama
llm = Llama(
      model_path="./models/7B/llama-model.gguf",
       n_gpu_layers=-1, 
      seed=1337,
      n_ctx=2048, 
)