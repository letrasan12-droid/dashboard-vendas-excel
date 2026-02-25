import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook

# Generate sample sales data for 3 months
months = ['January', 'February', 'March']
sales_data = {
    'Product A': [250, 300, 200],
    'Product B': [150, 100, 250],
    'Product C': [300, 200, 400]
}

# Convert to DataFrame
sales_df = pd.DataFrame(sales_data, index=months)

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = 'Sales Dashboard'

# Write sales data to the Excel file
for r_idx, row in enumerate(sales_df.itertuples(), 1):
    for c_idx, value in enumerate(row[1:], 1):
        ws.cell(row=r_idx, column=c_idx, value=value)

# Create a chart
chart = plt.figure()
plt.plot(months, sales_df['Product A'], label='Product A')
plt.plot(months, sales_df['Product B'], label='Product B')
plt.plot(months, sales_df['Product C'], label='Product C')
plt.title('Sales Data Overview')
plt.xlabel('Months')
plt.ylabel('Sales Units')
plt.legend()
plt.savefig('sales_dashboard.png')
plt.close(chart)

# Save chart image to the workbook
ws.add_image('sales_dashboard.png', 'E5')

# Save the workbook
wb.save('Sales_Dashboard.xlsx')
