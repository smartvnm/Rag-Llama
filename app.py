import streamlit as st
from llama_cpp import Llama
llm = Llama(
  model_path = "/content/modemistral-7b-instruct-v0.1.Q6_K.gguf",
  n_gpu_layers=-1,
  seed = 1337,
  n_ctx = 2048,
)