
import pandas as pd
import sys

# Check if the file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python summary_script_yearly.py <file_path>")
    sys.exit(1)

# Load the data from the Excel file specified in the command-line argument
file_path = sys.argv[1]
df = pd.read_excel(file_path)

# Renaming columns for clarity
columns = ['Date', 'Day of the Week', 'Type', 'Requested', 'Unit of Time', 'Comment', 'Status', 'Additional Info']
df.columns = columns
df = df.drop([0])  # Drop the first row which is the header in the Excel file

# Convert 'Date' to datetime format and 'Requested' to numeric
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Requested'] = pd.to_numeric(df['Requested'], errors='coerce')

# Extracting year and month from 'Date'
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Filtering for approved status
approved_df = df[df['Status'] == 'Approved']

# Grouping by 'Year', 'Type' and 'Month' and summing 'Requested'
summary = approved_df.groupby(['Year', 'Type', 'Month'])['Requested'].sum().reset_index()

# Converting 'Month' back to month names for readability
summary['Month'] = summary['Month'].apply(lambda x: pd.Timestamp(f'2024-{x}-01').strftime('%B'))

# Displaying the summarized data
print(summary)
