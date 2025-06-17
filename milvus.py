import fire
import random


from pymilvus import MilvusClient
from tqdm import tqdm


COLLECTION_NAME = "demo_collection"

DOCUMENTS = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]


def create_random_vector(l: int = 1024):
    return [random.uniform(-1, 1) for _ in range(l)]


def get_doc(i: int):
    return DOCUMENTS[i % len(DOCUMENTS)]


def create_client():
    return MilvusClient(uri="http://127.0.0.1:19530", token="root:Milvus")


class MilvusCli:
    def __init__(self):
        self.client = create_client()

    def status(self, name: str = COLLECTION_NAME):
        status = self.client.get_collection_stats(name)
        print(status)

    def clear(self, name: str = COLLECTION_NAME):
        if self.client.has_collection(collection_name=name):
            self.client.drop_collection(collection_name=name)

    def create_vectors(self, total: int = 1024, batch: int = 128):
        if not self.client.has_collection(collection_name=COLLECTION_NAME):
            self.client.create_collection(
                collection_name=COLLECTION_NAME, dimension=1024
            )

        with tqdm(total=total) as pbar:
            for i in range(0, total, batch):
                data = [
                    {
                        "id": i + j,
                        "text": get_doc(i + j),
                        "vector": create_random_vector(),
                    }
                    for j in range(batch)
                ]
                res = self.client.insert(collection_name=COLLECTION_NAME, data=data)
                assert res["insert_count"] == batch
                pbar.update(batch)

    def count(self, name: str = COLLECTION_NAME):
        c = self.client.query(collection_name=name, output_fields=["count(*)"])
        print(c)


if __name__ == "__main__":
    fire.Fire(MilvusCli)
