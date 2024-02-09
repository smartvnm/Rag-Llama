import streamlit as st
from llama_cpp import Llama
llm = Llama(
  model_path = "/content/models/mistral-7b-instruct-v0.1.Q6_K.gguf",
  n_gpu_layers=-1,
  n_threads = 2
  n_ctx = 2048,
)