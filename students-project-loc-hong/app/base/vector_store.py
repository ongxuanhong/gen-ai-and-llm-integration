from abc import ABC, abstractmethod

import numpy as np
from langchain_community.vectorstores import FAISS


class VectorStore(ABC):
    @abstractmethod
    def init_db():
        pass

    def create_index(self):
        pass

    def from_documents(self, documents, embeddings):
        pass

    def similarity_search(self, query: str, topk: int):
        pass

    def similarity_search_by_vector(self, vector: np.array, topk: int):
        pass

    def as_retriever(self):
        pass


class FaissVectorStore(VectorStore):
    def __init__(self, index_path: str) -> None:
        super().__init__()
        self.index_path = index_path
        self.init_db()

    def init_db(self):
        pass

    def create_index(self):
        pass

    def from_documents(self, documents, embeddings):
        self.db = FAISS.from_documents(documents, embeddings)

    def similarity_search(self, query: str, topk: int):
        return self.db.similarity_search(query, topk)

    def similarity_search_by_vector(self, vector: np.array, topk: int):
        return self.db.similarity_search_by_vector(vector, topk)

    def as_retriever(self, **kwargs):
        return self.db.as_retriever(**kwargs)

    def invoke(self, **kwargs):
        return self.db.invoke(**kwargs)
