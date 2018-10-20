from subprocess import call
import sys
from .text import normalize_ticket, build_browse_url, build_branch_name
from .jira import get_ticket_info

from .cliparser import get_parser


def run(ticket_name: str, _open=False) -> None:
    ticketname = normalize_ticket(ticket_name)

    if _open:
        # open
        browse_url = build_browse_url(ticketname)
        call(["open", browse_url])
        sys.exit(0)

    ticket_info = get_ticket_info(ticketname)
    branch_name = build_branch_name(ticket_info)
    print(branch_name)


def main() -> None:
    parser = get_parser()
    flags = parser.parse_args()
    run(flags.ticket_name, flags.open)
