
# How to Run the Script

This document provides instructions on how to run the `summary_script_yearly_cmd.py` Python script. This script processes data from an Excel file and generates a summary report based on yearly data.

## Prerequisites

Before running the script, ensure you have the following:

1. Python 3 installed on your machine. You can download Python 3 from [the official Python website](https://www.python.org/downloads/).

2. The `summary_script_yearly_cmd.py` script file located in your working directory.

3. The `workday_extract.xlsx` Excel file that contains the data you want to analyze. Place this file in a known directory.

## Dependencies Installation

Before running the script, you need to install the required Python libraries. The script requires the following dependencies:

- `openpyxl`: A library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
- `pandas`: A fast, powerful, flexible and easy to use open source data analysis and manipulation tool.

You can install these dependencies using pip by running the following command in your terminal:

```bash
pip install openpyxl pandas
```

Ensure these libraries are installed before proceeding with running the script.


## Extracting Workday Absences to Excel

Before running the script, you need to extract your absence records from Workday into an Excel file. Follow these steps to perform the extraction:

1. Log in to your Workday account.

2. Go to **View all Apps**. This can typically be found on your Workday dashboard or home page.

3. Select **Absence** from the list of applications.

4. Inside the Absence application, navigate to **View** > **My Absence** to view your absence records.

5. To export your absences, look for the export icon (![export icon](icon_extract_xls.png)) typically located at the top right corner or near your absence summary. Click on this icon to download your absence records in Excel format.

6. Save the downloaded Excel file in a known directory, as you will need to specify its path when running the script.

Proceed to the "Running the Script" section after you have successfully exported and saved your absence records.


## Running the Script

Follow these steps to run the script:

1. Open a terminal window (Command Prompt, PowerShell, or a Unix-based terminal).

2. Navigate to the directory where `summary_script_yearly_cmd.py` is located using the `cd` command. For example:

    ```bash
    cd path/to/script/directory
    ```

3. Run the script by typing the following command:

    ```bash
    python3 summary_script_yearly_cmd.py ../workday_extract.xlsx
    ```

    In this command:
    - `python3` is the command to run Python scripts.
    - `summary_script_yearly_cmd.py` is the name of the script file.
    - `../workday_extract.xlsx` is the path to the Excel file with the data. The `../` prefix means that the Excel file is located one directory above the script's directory. Adjust the path according to where your Excel file is located.

## What to Expect

After running the script, it will process the data from the `workday_extract.xlsx` file and generate a summary report. The specifics of the output will depend on how `summary_script_yearly_cmd.py` is programmed.

If the script runs successfully, you should see output messages in the terminal indicating the progress and completion of the data processing. If there are any errors, they will be displayed in the terminal as well.


## Example of Script Output

Below is an example of the output you might see after running the script. This is a pandas DataFrame showing the summary of leave requests by year, type, and month:

```plaintext
    Year                      Type      Month  Requested
0   2022     Annual Leave Acquired       June        1.0
1   2022     Annual Leave Acquired     August        4.0
2   2022  Annual Leave In Progress    October        1.0
3   2022  Annual Leave In Progress   December        3.5
4   2022             RH France RTT       July        0.5
5   2022             RH France RTT     August        4.0
6   2022             RH France RTT   December        1.5
7   2022           Unpaid Time Off       June        0.0
8   2022           Unpaid Time Off     August        0.0
9   2023     Annual Leave Acquired     August       13.0
10  2023     Annual Leave Acquired  September        1.0
11  2023             RH France RTT       June        1.0
12  2023             RH France RTT   December        4.0
13  2024             RH France RTT    January        4.0
```

This output is a simplified example and may vary depending on your specific data and script configurations.


## Troubleshooting

- If you encounter a `python3: command not found` error, ensure that Python 3 is installed correctly and that the installation directory is included in your system's PATH environment variable.

- If you receive file not found errors, check that the path to the `workday_extract.xlsx` file is correct and that the file exists in the specified location.

For more detailed information or assistance, refer to the script documentation or contact the script developer.
