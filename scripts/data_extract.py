"""
E + L ของ ELT: อ่านไฟล์ CSV ของ Northwind จาก 2 ระบบ แล้วโหลดเข้า DuckDB

ผลลัพธ์: ไฟล์ northwind.duckdb ที่มี schema ชื่อ raw และตาราง 9 ตาราง
รันซ้ำได้ด้วย CREATE OR REPLACE
"""
import sys
from pathlib import Path

import duckdb

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
ROOT_DIR = ROOT
DATA_DIR = ROOT / "raw_data"
DB_PATH = ROOT / "northwind.duckdb"

SOURCES = {
    # แหล่ง A: ระบบขายปัจจุบัน
    "customer": "raw/customer.csv",
    "employees": "raw/employees.csv",
    "order_details": "raw/order_details.csv",
    "orders": "raw/orders.csv",
    "products": "raw/products.csv",
    "shippers": "raw/shippers.csv",
    "suppliers": "raw/suppliers.csv",
    # แหล่ง B: ระบบขายเดิม
    "legacy_orders": "legacy/orders.csv",
    "legacy_order_details": "legacy/order_details.csv",
}


def main() -> None:
    my_dict = {"name": "JEEN", "secondname": "Dora"}
    print(f"My name is {my_dict['name']}")

    with duckdb.connect(str(DB_PATH)) as connection:
        connection.execute("CREATE SCHEMA IF NOT EXISTS raw")

        print(f"โหลดข้อมูลเข้า {DB_PATH.name}")
        for table, relative_path in SOURCES.items():
            csv_path = DATA_DIR / relative_path
            if not csv_path.is_file():
                raise FileNotFoundError(f"ไม่พบไฟล์ {csv_path}")

            connection.execute(
                f"CREATE OR REPLACE TABLE raw.{table} "
                "AS SELECT * FROM read_csv_auto(?)",
                [str(csv_path)],
            )
            row_count = connection.execute(
                f"SELECT COUNT(*) FROM raw.{table}"
            ).fetchone()[0]
            print(
                f" raw.{table:<22} {row_count:>6,} แถว "
                
            )

    print("เสร็จแล้ว — ขั้นต่อไป: dbt run")


if __name__ == "__main__":
    main()

   