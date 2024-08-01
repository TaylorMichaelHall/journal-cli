import argparse
from .database import create_table
from .commands import add_entry, show_entries, edit_entry, delete_entry

def main():
    parser = argparse.ArgumentParser(description="Simple Journal CLI")
    subparsers = parser.add_subparsers(dest='action', required=True)

    # Add entry
    add_parser = subparsers.add_parser('add', help='Add a new journal entry')
    add_parser.add_argument('entry', nargs='+', help="Journal entry text")

    # Show entries
    show_parser = subparsers.add_parser('show', help='Show journal entries')
    show_parser.add_argument('-i', '--id', action='store_true', help="Show entry IDs")
    show_parser.add_argument('-t', '--timestamps', action='store_true', help="Show timestamps")

    # Edit entry
    edit_parser = subparsers.add_parser('edit', help='Edit a journal entry')
    edit_parser.add_argument('id', help="ID of the entry to edit")
    edit_parser.add_argument('entry', nargs='+', help="New text for the entry")

    # Delete entry
    delete_parser = subparsers.add_parser('delete', help='Delete a journal entry')
    delete_parser.add_argument('id', help="ID of the entry to delete")

    args = parser.parse_args()

    create_table()

    if args.action == 'add':
        entry_text = ' '.join(args.entry)
        add_entry(entry_text)
    elif args.action == 'show':
        show_entries(args.id, args.timestamps)
    elif args.action == 'edit':
        entry_text = ' '.join(args.entry)
        edit_entry(args.id, entry_text)
    elif args.action == 'delete':
        delete_entry(args.id)

if __name__ == "__main__":
    main()