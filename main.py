
from database import create_destination_schema
from migrate import migrate_all
from validate import validate_counts


def main():
    print("Iniciando migracao para o Neon...")

    try:
        print("\n1. Criando estrutura no PostgreSQL...")
        create_destination_schema()

        print("\n2. Migrando dados do SQLite para o Neon...")
        migrate_all()

        print("\n3. Validando os registros...")
        validate_counts()

        print("\nProcesso finalizado!")

    except Exception as error:
        print(f"\nErro durante o processo: {error}")
        raise


if __name__ == "__main__":
    main()
