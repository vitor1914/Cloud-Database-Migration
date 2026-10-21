import json
from datetime import datetime
from pathlib import Path

from database import (
    ROOT,
    get_source_connection,
    get_destination_connection,
)

TABLES = ("clientes", "produtos", "vendas")


def validate_counts():
    results = {}

    with get_source_connection() as source:
        with get_destination_connection() as destination:
            with destination.cursor() as cursor:
                for table in TABLES:
                    source_count = source.execute(
                        f"SELECT COUNT(*) FROM {table}"
                    ).fetchone()[0]

                    cursor.execute(
                        f"SELECT COUNT(*) FROM {table}"
                    )
                    destination_count = cursor.fetchone()[0]

                    results[table] = {
                        "origem": source_count,
                        "destino": destination_count,
                        "aprovado": source_count == destination_count,
                    }

    return results


def main():
    results = validate_counts()

    for table, result in results.items():
        status = "OK" if result["aprovado"] else "DIVERGÊNCIA"
        print(
            f"{table}: origem={result['origem']} | "
            f"destino={result['destino']} | {status}"
        )

    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)

    report = {
        "data_validacao": datetime.now().astimezone().isoformat(),
        "resultados": results,
        "aprovado": all(
            item["aprovado"] for item in results.values()
        ),
    }

    report_path = report_dir / "validation_report.json"
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Relatório salvo em: {report_path}")

    if not report["aprovado"]:
        raise SystemExit("A validação encontrou divergências.")

    print("Todas as contagens foram validadas.")


if __name__ == "__main__":
    main()