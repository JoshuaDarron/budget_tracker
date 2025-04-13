from .drive import copy_template_if_needed
from .chase import get_previous_month_transactions
from .sheets import write_transactions_to_sheet

def run():
    import os
    from dotenv import load_dotenv
    load_dotenv()

    parent_folder_id = os.getenv("PARENT_FOLDER_ID")
    if not parent_folder_id:
        raise ValueError("❌ Missing PARENT_FOLDER_ID in .env file")

    spreadsheet_id = copy_template_if_needed(parent_folder_id)
    transactions = get_previous_month_transactions()
    write_transactions_to_sheet(spreadsheet_id, transactions)

