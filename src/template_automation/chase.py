import datetime
import requests
import os

def get_previous_month_transactions():
    # Placeholder: Replace with actual Chase API auth & call
    # previous_month = (datetime.datetime.now().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")
    # 
    # response = requests.get("https://api.chase.com/transactions", params={
    #     "month": previous_month
    # }, headers={
    #     "Authorization": f"Bearer {os.getenv('CHASE_API_TOKEN')}"
    # })
    # response.raise_for_status()
    
    return [
        {
            "date": "2024-03-02",
            "amount": -45.12,
            "description": "Trader Joe's"
        },
        {
            "date": "2024-03-05",
            "amount": -80.00,
            "description": "Electric Company"
        }
    ]  # Replace with real parsed data

