import os
from datetime import datetime, timedelta
import zipfile

# Get today's date
today = datetime.today()

# Calculate yesterday's date
yesterday = today - timedelta(days=1)

# Format the date in the required format (YYYY-MM-DD)
yesterday_str = yesterday.strftime('%Y-%m-%d')

# Construct filenames
log_filename = f'LOG{yesterday_str}.txt'
zip_filename = f'LOG{yesterday_str}.zip'

# Check if the log file exists
if os.path.exists(log_filename):
    # Compress the log file into a zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(log_filename)

    # Delete the original log file
    os.remove(log_filename)

    print(f'{log_filename} has been compressed to {zip_filename} and the original file has been deleted.')
else:
    print(f'{log_filename} does not exist.')

