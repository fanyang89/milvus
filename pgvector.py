import fire
import random
import psycopg
import numpy as np

from tqdm import tqdm
from pgvector.psycopg import register_vector


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


class PgvectorCli:
    def create_vectors(self, dsn: str = "dbname=test user=postgres"):
        with psycopg.connect(dsn) as conn:
            conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
            register_vector(conn)
            conn.execute(
                "CREATE TABLE vectors (id bigserial PRIMARY KEY, embedding vector(3))"
            )
            embedding = np.array([1, 2, 3])
            conn.execute("INSERT INTO items (embedding) VALUES (%s)", (embedding,))


if __name__ == "__main__":
    fire.Fire(PgvectorCli)
