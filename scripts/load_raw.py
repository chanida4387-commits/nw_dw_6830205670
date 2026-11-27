try:
    from .data_extract import main
except ImportError:
    from data_extract import main


if __name__ == "__main__":
    main()
