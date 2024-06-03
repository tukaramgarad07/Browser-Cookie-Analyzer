import os
import platform
import sqlite3
import xlsxwriter # type: ignore
import datetime
import pytz # type: ignore

def get_browser_cookie_path(browser_name):
    # Dictionary mapping browser names to their cookie file paths
    cookie_paths = {
        'Chrome': {
            'Linux': os.path.expanduser('/home/tuka/.config/google-chrome/Default/Cookies'),
        },
        # Add more browsers and their paths as needed
         'Firefox': {
        	'Linux': os.path.expanduser('/home/tuka/snap/firefox/common/.mozilla/firefox/0nal4u8a.default/cookies.sqlite'),
         },
    }

    # Check if the specified browser and operating system are supported
    if browser_name in cookie_paths:
        if platform.system() in cookie_paths[browser_name]:
            return cookie_paths[browser_name][platform.system()]

    print("Unsupported browser or operating system")
    return None


def convert_unix_timestamp(timestamp_microseconds):
    timestamp_seconds = timestamp_microseconds // 1000000  # Convert microseconds to seconds
    dt = datetime.datetime.fromtimestamp(timestamp_seconds, datetime.timezone.utc)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def analyze_browser_cookies(browser_name):
    # Get the cookie file path for the specified browser
    cookie_path = get_browser_cookie_path(browser_name)
    if not cookie_path:
        return

    # Check if the database file exists
    if not os.path.exists(cookie_path):
        print("Database file not found:", cookie_path)
        return

    # Connect to the SQLite database
    try:
        conn = sqlite3.connect(cookie_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return

    # Query to select cookies from the database (modify as needed for different browsers)
    query = "SELECT name, value, host_key, path, expires_utc, is_secure FROM cookies"

    # Execute the query and fetch the results
    try:
        cursor.execute(query)
        cookies = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error executing the query:", e)
        conn.close()
        return

    # Create an Excel workbook and worksheet
    #workbook = xlsxwriter.Workbook('E:\projects\gtihub up\cookies analyzer\Report.xlsx')
    workbook = xlsxwriter.Workbook(f'E:\projects\gtihub up\cookies analyzer\Report_{browser_name}.xlsx')
    worksheet = workbook.add_worksheet()

    # Write headers to the worksheet
    headers = ['Name', 'Value', 'Host', 'Path', 'Expires', 'Secure']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write cookie data to the worksheet
    for row, cookie in enumerate(cookies, start=1):
        for col, data in enumerate(cookie):
            for col, data in enumerate(cookie):
                if col == 4:  # Convert Unix timestamp to human-readable format for 'expires_utc' column
                    worksheet.write(row, col, convert_unix_timestamp(data))
                else:
                    worksheet.write(row, col, str(data))

    # Close the workbook
    workbook.close()

    #print("Cookie data exported to 'Report.xlsx'")
    print(f"Cookie data for {browser_name} exported to 'Report_{browser_name}.xlsx'")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    print("Starting browser cookie analysis tool...")
    #analyze_browser_cookies(browser_name)
    #browser_name = input("Enter the name of the browser (e.g., Firefox, Chrome): ").strip()
    browsers = input("Enter the names of the browsers separated by commas (e.g., Firefox, Chrome): ").strip().split(',')
    for browser in browsers:
        analyze_browser_cookies(browser.strip())
