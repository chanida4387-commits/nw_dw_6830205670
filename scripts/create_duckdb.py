import duckdb

from data_extract import ROOT_DIR


DATABASE_PATH = ROOT_DIR / "warehouse.duckdb"


def main() -> None:
    with duckdb.connect(str(DATABASE_PATH)):
        pass
    print(f"DuckDB database ready: {DATABASE_PATH}")


if __name__ == "__main__":
    main()
