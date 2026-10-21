import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "origem.db"


def main():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        conn.executescript("""
        DROP TABLE IF EXISTS vendas;
        DROP TABLE IF EXISTS produtos;
        DROP TABLE IF EXISTS clientes;

        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            cidade TEXT NOT NULL
        );

        CREATE TABLE produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco NUMERIC NOT NULL CHECK (preco >= 0),
            estoque INTEGER NOT NULL CHECK (estoque >= 0)
        );

        CREATE TABLE vendas (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL REFERENCES clientes(id),
            produto_id INTEGER NOT NULL REFERENCES produtos(id),
            quantidade INTEGER NOT NULL CHECK (quantidade > 0),
            data_venda TEXT NOT NULL
        );
        """)

        conn.executemany(
            "INSERT INTO clientes VALUES (?, ?, ?, ?)",
            [
                (1, "Ana Souza", "ana.souza@example.com", "Brasília"),
                (2, "Bruno Lima", "bruno.lima@example.com", "Goiânia"),
                (3, "Carla Mendes", "carla.mendes@example.com", "Anápolis"),
            ],
        )

        conn.executemany(
            "INSERT INTO produtos VALUES (?, ?, ?, ?)",
            [
                (1, "Teclado", 120.00, 18),
                (2, "Mouse", 65.50, 30),
                (3, "Monitor", 899.90, 7),
            ],
        )

        conn.executemany(
            "INSERT INTO vendas VALUES (?, ?, ?, ?, ?)",
            [
                (1, 1, 1, 2, "2026-10-01"),
                (2, 2, 2, 1, "2026-10-03"),
                (3, 3, 3, 1, "2026-10-05"),
                (4, 1, 2, 3, "2026-10-07"),
                (5, 2, 1, 1, "2026-10-09"),
            ],
        )

    print(f"Banco de origem criado em: {DB_PATH}")


if __name__ == "__main__":
    main()