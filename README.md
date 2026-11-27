# nw_dw_6830205670

## Load raw CSV data

Install project dependencies, then run from the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/load_raw.py
```

The loader reads CSV files from `raw_data/raw` and `raw_data/legacy`, and
replaces the corresponding tables in the `raw` schema of `northwind.duckdb`.
Current-system tables retain their filenames; legacy tables use the
`legacy_` prefix. Running the command again produces the same tables and data.