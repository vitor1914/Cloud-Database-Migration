import os
import sqlite3
from pathlib import Path

import psycopg
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent
SOURCE_DB = Path(os.getenv("SOURCE_DB", str(ROOT / "data" / "origem.db")))
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def get_source_connection():
    if not SOURCE_DB.exists():
        raise FileNotFoundError(
            "Banco SQLite não encontrado. Execute "
            "'python init_source_db.py' primeiro."
        )

    conn = sqlite3.connect(SOURCE_DB)
    conn.row_factory = sqlite3.Row
    return conn


def get_destination_connection():
    if not DATABASE_URL:
        raise RuntimeError(
            "Configure DATABASE_URL no arquivo .env."
        )

    return psycopg.connect(
        DATABASE_URL,
        connect_timeout=15
    )


def create_destination_schema():
    statements = [
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            cidade TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco NUMERIC(12, 2) NOT NULL CHECK (preco >= 0),
            estoque INTEGER NOT NULL CHECK (estoque >= 0)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL REFERENCES clientes(id),
            produto_id INTEGER NOT NULL REFERENCES produtos(id),
            quantidade INTEGER NOT NULL CHECK (quantidade > 0),
            data_venda DATE NOT NULL
        )
        """,
    ]

    with get_destination_connection() as conn:
        with conn.cursor() as cur:
            for statement in statements:
                cur.execute(statement)

    print("Estrutura PostgreSQL criada ou já existente.")