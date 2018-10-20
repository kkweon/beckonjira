import argparse


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("ticket_name", help="Jira Ticket Number (e.g., BASE-12345)")
    parser.add_argument(
        "--open", action="store_true", help="Run `open` command instead"
    )
    return parser
