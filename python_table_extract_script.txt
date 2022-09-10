# requires openpyxl version 2.4.0+

from openpyxl import load_workbook
wb = load_workbook(filename='input.xlsx')
ws = wb.get_active_sheet() # ws is now an IterableWorksheet

# iterate thru all cells and if hyperlink found attempt modification of cell
for row in ws.rows:
    for cell in row:
        try:
            if len(cell.hyperlink.target)  > 0:
                cell.value = "".join([cell.value,"|",cell.hyperlink.target])
                # Join cell.value and hyperlink target into string (optionally just assign the hyperlink.target to the cell.value
        except:
            pass

# save workbook to temp .xlsx (I could not manage to read from buffer...) .
wb.save("temp.xlsx")

# read with pandas 
data = pd.read_excel("temp.xlsx")

# take DataSeries and rsplit by "|" and expand to 2 columns
hyper = (data.MyLinks.str.rsplit("|", expand=True))

#set labels
hyper.columns=["Label","Hyperlink"]

# join them back to dataframe on index
data = data.join(hyper, how="left")

# done