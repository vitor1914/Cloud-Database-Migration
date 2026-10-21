# Cloud Database Migration | Migração de Banco de Dados para a Nuvem

🇧🇷 Português | 🇺🇸 English

## 🇧🇷 Português

### Sobre o projeto

Projeto de Engenharia de Dados que demonstra a migração de um banco de dados SQLite local para PostgreSQL hospedado na nuvem por meio do Neon.

O processo inclui criação das tabelas de destino, transferência de dados relacionais, tratamento de conflitos de chave primária e validação da quantidade de registros.

### Tecnologias

- Python
- SQLite
- PostgreSQL
- Neon
- SQL
- psycopg
- python-dotenv

### Estrutura

- `main.py`: ponto de entrada opcional para orquestração.
- `database.py`: conexões e criação do esquema.
- `init_source_db.py`: criação dos dados de demonstração.
- `migrate.py`: transferência dos dados.
- `validate.py`: validação e relatório.
- `data/origem.db`: banco de origem.
- `.env.example`: modelo de configuração.

### Execução

1. Crie um ambiente virtual Python.
2. Instale as dependências de `requirements.txt`.
3. Execute `python init_source_db.py`.
4. Configure a variável `DATABASE_URL` em `.env` com os dados do Neon.
5. Execute `python migrate.py`.
6. Execute `python validate.py`.

### Resultados esperados

| Tabela | Registros |
|---|---:|
| Clientes | 3 |
| Produtos | 3 |
| Vendas | 5 |

Os resultados devem ser confirmados por meio da execução e do relatório de validação.

### Segurança

Credenciais, senhas e strings privadas de conexão não devem ser publicadas no repositório. O arquivo `.env` deve permanecer protegido e fora do controle de versão.

### Aprendizados

- Migração de bancos relacionais.
- Conexões com PostgreSQL na nuvem.
- Integridade referencial.
- Cargas idempotentes.
- Validação de dados.
- Boas práticas de segurança.

### Autor

Projeto prático de estudos em Engenharia de Dados, SQL, Python e Computação em Nuvem.

---

## 🇺🇸 English

### About the project

A Data Engineering project demonstrating the migration of a local SQLite database to cloud-hosted PostgreSQL using Neon.

The workflow includes destination schema creation, relational data transfer, primary-key conflict handling, and record-count validation.

### Technologies

- Python
- SQLite
- PostgreSQL
- Neon
- SQL
- psycopg
- python-dotenv

### Project structure

- `main.py`: optional entry point for orchestration.
- `database.py`: database connections and schema creation.
- `init_source_db.py`: creates demonstration data.
- `migrate.py`: transfers database records.
- `validate.py`: validates counts and generates a report.
- `data/origem.db`: source database.
- `.env.example`: configuration template.

### How to run

1. Create a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run `python init_source_db.py`.
4. Set the Neon connection string in `DATABASE_URL` inside `.env`.
5. Run `python migrate.py`.
6. Run `python validate.py`.

### Expected results

| Table | Records |
|---|---:|
| Customers | 3 |
| Products | 3 |
| Sales | 5 |

The results must be confirmed by running the migration and reviewing the validation report.

### Security

Database credentials, passwords, and private connection strings must never be published. Keep `.env` protected and excluded from version control.

### Key learnings

- Relational database migration.
- Cloud PostgreSQL connectivity.
- Referential integrity.
- Idempotent data loading.
- Data validation.
- Security best practices.

### Author

A hands-on learning project focused on Data Engineering, SQL, Python, and Cloud Computing.