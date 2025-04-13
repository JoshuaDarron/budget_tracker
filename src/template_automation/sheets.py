from .auth import get_sheets_service

def delete_sheet_rows(spreadsheet_id):
    sheets_service = get_sheets_service()
    spreadsheet = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = spreadsheet.get("sheets", [])

    requests = []

    if len(sheets) >= 1:
        sheet_id_1 = sheets[0]['properties']['sheetId']
        requests.append({
            "deleteDimension": {
                "range": {
                    "sheetId": sheet_id_1,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 6
                }
            }
        })

    if len(sheets) >= 2:
        sheet_id_2 = sheets[1]['properties']['sheetId']
        requests.append({
            "deleteDimension": {
                "range": {
                    "sheetId": sheet_id_2,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 1
                }
            }
        })

    if requests:
        body = {"requests": requests}
        sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()
        print("🧹 Deleted rows from the new sheet.")

