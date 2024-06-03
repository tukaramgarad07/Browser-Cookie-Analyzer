# Browser Cookie Analyzer

## Overview

The **Browser Cookie Analyzer** is a powerful Python script developed to facilitate the analysis and reporting of browser cookies from popular web browsers such as Chrome and Firefox. This tool extracts detailed cookie data from the browser's database files and exports it to Excel for comprehensive analysis. It is an invaluable resource for developers, data analysts, and security professionals, providing insights into web tracking, security, and user behavior.

## Features

### Multi-Browser Support
- **Browsers Supported**: 
  - Chrome
  - Firefox
- **Easily Extendable**: The script can be adapted to support additional browsers in the future.

### Session Coverage
- **Regular Sessions**: Analyzes cookies stored during standard browsing sessions.
- **Incognito/Private Sessions**: Extracts cookies from incognito or private browsing sessions for a comprehensive analysis.

### Detailed Cookie Data Extraction
- **Attributes Captured**:
  - **Name**: The name of the cookie.
  - **Value**: The value of the cookie.
  - **Host**: The domain that set the cookie.
  - **Path**: The path within the domain that the cookie is valid for.
  - **Expiration Date**: When the cookie expires.
  - **Secure**: Indicates if the cookie is transmitted over HTTPS only.
- **Granular Analysis**: Provides detailed insights into each cookie's attributes.

### Excel Export
- **Output Format**: Exports data to Excel files for easy review and sharing.
- **Naming Convention**: Files are named `Report_Browser_Profile.xlsx`, reflecting the browser and profile analyzed.

### User-Friendly Interface
- **Command-Line Prompts**: Simple, intuitive prompts guide users through the analysis process.
- **Minimal Setup**: Clear installation and usage instructions for ease of use.

## Installation

### Prerequisites
- **Python**: Ensure Python is installed on your machine.
- **pip**: Python package installer should be available.

### Steps
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/shreyas0201/cookie-analyzer.git
    ```
2. **Install Required Python Packages**:
    ```sh
    pip install xlsxwriter==1.4.5 pytz==2022.1
    ```

## Usage

1. **Run the Script**:
    ```sh
    python script.py
    ```
2. **Follow Prompts**:
    - **Browsers**: Enter the names of the browsers you wish to analyze, separated by commas (e.g., Chrome, Firefox).
    - **Profiles**: Enter the profile names for each browser when prompted.

3. **View Results**:
    - The script generates Excel files named `Report_Browser_Profile.xlsx`, containing the analyzed cookie data for each specified browser and profile.

### Example

```sh
python script.py
Starting browser cookie analysis tool...
Enter the names of the browsers separated by commas (e.g., Firefox, Chrome): Chrome, Firefox
Enter the profile names for Chrome separated by commas (e.g., Default, Profile 1): Default
Enter the profile names for Firefox separated by commas (e.g., Default, Profile 1): Default
Cookie data for Chrome (Default) exported to 'Report_Chrome_Default.xlsx'
Cookie data for Firefox (Default) exported to 'Report_Firefox_Default.xlsx'
