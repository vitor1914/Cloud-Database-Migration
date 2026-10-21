from database import (
    get_source_connection,
    get_destination_connection,
    create_destination_schema,
)

TABLES = {
    "clientes": """
        INSERT INTO clientes (id, nome, email, cidade)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            nome = EXCLUDED.nome,
            email = EXCLUDED.email,
            cidade = EXCLUDED.cidade
    """,
    "produtos": """
        INSERT INTO produtos (id, nome, preco, estoque)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            nome = EXCLUDED.nome,
            preco = EXCLUDED.preco,
            estoque = EXCLUDED.estoque
    """,
    "vendas": """
        INSERT INTO vendas (
            id, cliente_id, produto_id, quantidade, data_venda
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            cliente_id = EXCLUDED.cliente_id,
            produto_id = EXCLUDED.produto_id,
            quantidade = EXCLUDED.quantidade,
            data_venda = EXCLUDED.data_venda
    """,
}


def migrate_all():
    create_destination_schema()

    with get_source_connection() as source:
        with get_destination_connection() as destination:
            with destination.cursor() as cursor:
                for table, sql in TABLES.items():
                    rows = source.execute(
                        f"SELECT * FROM {table} ORDER BY id"
                    ).fetchall()

                    for row in rows:
                        cursor.execute(sql, tuple(row))

                    print(
                        f"{table}: {len(rows)} registro(s) processado(s)."
                    )

    print("Migração concluída.")


if __name__ == "__main__":
    migrate_all()