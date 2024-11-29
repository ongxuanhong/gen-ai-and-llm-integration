from typing import Iterator

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PatchedPDFLoader(PyPDFLoader):

    def __init__(self, file_path: str, start_page_num: int = 0, **kwargs) -> None:
        super().__init__(file_path, **kwargs)
        self.start_page_num = start_page_num

    def lazy_load(
        self,
    ) -> Iterator[Document]:
        for d in super().lazy_load():
            page = d.metadata.get("page")
            if page is not None:
                d.metadata["page"] = str(int(page) + self.start_page_num)
            yield d
