from .database import add_entry_to_db, get_entries_from_db, edit_entry_in_db, delete_entry_from_db
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def add_entry(entry):
    entry_id = add_entry_to_db(entry)
    print(f"{Fore.GREEN}Entry added successfully. {Fore.YELLOW}ID: {entry_id}")

def show_entries(show_id=False, show_timestamps=False):
    entries = get_entries_from_db()

    current_date = None
    for entry in entries:
        id, added_at, updated_at, text = entry
        date = datetime.fromisoformat(added_at).date()
        
        if date != current_date:
            if current_date is not None:
                print()
            print(f"{Fore.CYAN}{Style.BRIGHT}{date}:")
            current_date = date
        
        if show_id and show_timestamps:
            print(f"{Fore.YELLOW}[{id}] - {Fore.MAGENTA}Added: {added_at}, Updated: {updated_at}")
            print(f"    {Style.BRIGHT}{text}")
        elif show_id:
            print(f"{Fore.YELLOW}[{id}] - {Style.BRIGHT}{text}")
        elif show_timestamps:
            print(f"{Fore.MAGENTA}Added: {added_at}, Updated: {updated_at}")
            print(f"    {Style.BRIGHT}{text}")
        else:
            print(f"{Fore.WHITE}- {Style.BRIGHT}{text}")

def edit_entry(id, new_entry):
    rows_affected = edit_entry_in_db(id, new_entry)
    if rows_affected == 0:
        print(f"{Fore.RED}No entry found with ID {id}")
    else:
        print(f"{Fore.GREEN}Entry updated successfully.")

def delete_entry(id):
    rows_affected = delete_entry_from_db(id)
    if rows_affected == 0:
        print(f"{Fore.RED}No entry found with ID {id}")
    else:
        print(f"{Fore.GREEN}Entry deleted successfully.")