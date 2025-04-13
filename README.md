# 📊 Google Drive Template Automation

A Python automation tool that copies a monthly Google Sheets template into a year-based folder structure within your Google Drive. It intelligently creates the folder for the year (if it doesn't exist), copies the template, renames it based on the previous month (e.g., `01`, `02`, ...), and cleans up unnecessary rows.

---

## ✨ Description

This tool automates the monthly creation of Google Sheets based on a reusable `Template` file stored in your Google Drive. On execution, it:

- Finds or creates a folder named after the **previous month's year** (e.g., `2024`).
- Copies the `Template` file from the **parent directory**.
- Renames the new file with the **previous month number** (e.g., `03` for March).
- Deletes:
  - Rows 1–6 on the first sheet
  - Row 1 on the second sheet

This is perfect for recurring reports, logs, or budgeting workflows.

---

## ⚙️ Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/google-drive-template-automation.git
   cd google-drive-template-automation
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Enable Google Drive & Sheets API:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project and enable:
     - Google Drive API
     - Google Sheets API
   - Create **OAuth 2.0 client credentials**
   - Download `credentials.json` and place it in the root of this project

4. **Make sure your account is added as a test user** in the OAuth Consent screen

---

## 🚀 Run

Execute the automation script:

```bash
python run.py
```

- The script will open a browser window to authenticate with your Google account (on first run).
- A `token.pickle` file will be saved for reuse of credentials.
- Output will confirm creation or skipping of the monthly file.

---

## 👤 Authors

**Joshua Phillips**  
[github.com/joshua-phillips](https://github.com/joshua-phillips)

Contributions welcome — feel free to submit a PR or open an issue!

---

