import streamlit as st
from llama_cpp import Llama
llm = Llama(
  model_path = "/content/models/minicpm-2b-dpo-fp32.Q8_0.gguf",
  n_gpu_layers=-1,
  seed = 1337,
  n_ctx = 2048,
)