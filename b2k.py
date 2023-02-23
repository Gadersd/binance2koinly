import csv
import sys

# Define the categories that are supported
SUPPORTED_CATEGORIES = ['Deposit', 'Buy', 'Sell', 'Withdrawal', 'Distribution', 'Convert']


def convert_csv(old_file, new_file):
    # Open the old and new CSV files
    with open(old_file, 'r') as csv_file, open(new_file, 'w', newline='') as new_csv_file:
        reader = csv.DictReader(csv_file)
        writer = csv.writer(new_csv_file)
        
        # Write the headers for the new CSV file
        writer.writerow(['Date', 'Sent Amount', 'Sent Currency', 'Received Amount', 'Received Currency', 'Fee Amount', 'Fee Currency', 'Net Worth Amount', 'Net Worth Currency', 'Label', 'Description', 'TxHash'])
        
        # Loop through each row in the old CSV file
        for row in reader:
            # Check if the category is supported
            if row['Category'] not in SUPPORTED_CATEGORIES:
                raise ValueError(f"Unsupported category encountered: {row['Category']}")

            # Determine the sent amount and currency
            if row['Category'] in ['Buy', 'Sell', 'Convert']:
                sent_amount = row['Realized_Amount_For_Base_Asset']
                sent_currency = row['Base_Asset']
            elif row['Category'] == 'Withdrawal':
                sent_amount = row['Realized_Amount_For_Primary_Asset']
                sent_currency = row['Primary_Asset']
            else:
                sent_amount = ''
                sent_currency = ''

            # Determine the received amount and currency
            if row['Category'] in ['Buy', 'Sell', 'Convert']:
                received_amount = row['Realized_Amount_For_Quote_Asset']
                received_currency = row['Quote_Asset']
            elif row['Category'] in ['Deposit', 'Distribution']:
                received_amount = row['Realized_Amount_For_Primary_Asset']
                received_currency = row['Primary_Asset']
            else:
                received_amount = ''
                received_currency = ''

            # Determine the label
            if row['Category'] == 'Distribution':
                label = 'reward'
            else:
                label = ''

            # Determine the values for the new CSV file
            new_row = [
                row['Time'],
                sent_amount,
                sent_currency,
                received_amount,
                received_currency,
                row['Realized_Amount_For_Fee_Asset'],
                row['Fee_Asset'],
                '',
                '',
                label,
                row['Operation'],
                row['Order_Id']
            ]

            # Write the row to the new CSV file
            writer.writerow(new_row)

    print(f"Conversion complete. New file saved as {new_file}.")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python converter.py [old_file] [new_file]")
        sys.exit(1)

    convert_csv(sys.argv[1], sys.argv[2])
