import argparse


def get_parser() -> argparse.ArgumentParser:
    """Returns CLI arguments parser"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "ticket_name", type=str, help="Jira Ticket Number (e.g., BASE-12345)"
    )
    parser.add_argument(
        "--open", action="store_true", help="Run `open` command instead"
    )
    return parser
