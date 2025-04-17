import os
import datetime
import requests

def get_previous_month_transactions():
    # Calculate the previous month in "YYYY-MM" format
    # previous_month = (datetime.datetime.now().replace(day=1) - datetime.timedelta(days=1)).strftime("%Y-%m")

    # Placeholder API call – replace URL and params with real Amex API
    # response = requests.get("https://api.amex.com/transactions", params={
    #     "month": previous_month
    # }, headers={
    #     "Authorization": f"Bearer {os.getenv('AMEX_API_TOKEN')}"
    # })
    # response.raise_for_status()

    # Example placeholder return format
    return [
        {
            "date": "2024-03-03",
            "amount": -29.99,
            "description": "Spotify"
        },
        {
            "date": "2024-03-10",
            "amount": -120.00,
            "description": "Flight Booking"
        }
    ]

