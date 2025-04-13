import os
from dotenv import load_dotenv
from .drive import copy_template_if_needed

def run():
    load_dotenv()
    parent_folder_id = os.getenv("PARENT_FOLDER_ID")
    if not parent_folder_id:
        raise ValueError("❌ Missing PARENT_FOLDER_ID in .env file")
    copy_template_if_needed(parent_folder_id)

