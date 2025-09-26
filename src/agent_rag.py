import numpy as np
from loguru import logger

# 💡 关键更改: 从新的 'langchain_ollama' 包中导入 OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from sentence_transformers.util import cos_sim

# --- 配置 Ollama Embedding ---
# 确保这个模型名称与你在 Ollama 中安装的完全一致
OLLAMA_MODEL_NAME = "ryanshillington/Qwen3-Embedding-4B:latest"
OLLAMA_BASE_URL = "http://localhost:11434"

# 初始化 Ollama Embedding 客户端
# 警告已消除
ollama_embeddings = OllamaEmbeddings(model=OLLAMA_MODEL_NAME, base_url=OLLAMA_BASE_URL)

# --- 准备数据 ---
queries = [
    "What is the capital of China?",
    "Explain gravity",
]
documents = [
    "The capital of China is Beijing.",
    "Beijing is the capital of China.",
    "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun.",
]

# --- 编码 (Encode) ---
print(f"Encoding queries with Ollama model: {OLLAMA_MODEL_NAME}...")

# 获取 query 向量 (使用 embed_documents 或 embed_query 都可以，取决于你的实际数据格式)
query_embeddings = np.array(ollama_embeddings.embed_documents(queries))
logger.info(query_embeddings)
logger.info(query_embeddings.shape)
# 获取 document 向量
document_embeddings = np.array(ollama_embeddings.embed_documents(documents))
logger.info(document_embeddings)
logger.info(document_embeddings.shape)
# --- 计算相似度 (Similarity) ---
similarity = cos_sim(query_embeddings, document_embeddings)
print("\n--- 相似度结果 ---")
print(similarity)
