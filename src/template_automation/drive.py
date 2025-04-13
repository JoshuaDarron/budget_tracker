import datetime
from .auth import get_drive_service
from .sheets import delete_sheet_rows

def copy_template_if_needed(parent_folder_id):
    drive_service = get_drive_service()

    now = datetime.datetime.now()
    previous_month = now.month - 1 if now.month > 1 else 12
    filename = f"{previous_month:02d}"

    # Check if file already exists
    query = f"'{parent_folder_id}' in parents and name = '{filename}' and trashed = false"
    result = drive_service.files().list(q=query, fields="files(id, name)").execute()
    if result.get('files'):
        print(f"✅ File '{filename}' already exists.")
        return

    # Find the Template
    template_query = f"'{parent_folder_id}' in parents and name = 'Template' and trashed = false"
    result = drive_service.files().list(q=template_query, fields="files(id, name)").execute()
    template_files = result.get('files', [])
    if not template_files:
        print(f"❌ No 'Template' file found in folder {parent_folder_id}.")
        return

    template_id = template_files[0]['id']

    # Determine year folder for the previous month
    year = now.year if now.month > 1 else now.year - 1
    year_folder_query = (
        f"'{parent_folder_id}' in parents and name = '{year}' and "
        f"mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    )
    year_folder_result = drive_service.files().list(q=year_folder_query, fields="files(id, name)").execute()
    year_folders = year_folder_result.get('files', [])

    if year_folders:
        year_folder_id = year_folders[0]['id']
    else:
        year_folder_metadata = {
            'name': str(year),
            'parents': [parent_folder_id],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        year_folder = drive_service.files().create(body=year_folder_metadata, fields='id').execute()
        year_folder_id = year_folder['id']
        print(f"📁 Created year folder '{year}'")

    # Copy and rename
    new_file_metadata = {
        'name': filename,
        'parents': [year_folder_id]
    }

    copied = drive_service.files().copy(fileId=template_id, body=new_file_metadata, fields="id").execute()
    copied_file_id = copied['id']
    print(f"✅ Copied 'Template' to '{filename}' (ID: {copied_file_id}).")

    delete_sheet_rows(copied_file_id)

