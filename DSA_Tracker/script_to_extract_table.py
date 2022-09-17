# requires openpyxl version 2.4.0+

from openpyxl import load_workbook
import pandas as pd
wb = load_workbook(filename='DSA_TRACKER_QUESTIONS.xlsx')
ws = wb['Sheet1'] # ws is now an IterableWorksheet\

# iterate thru all cells and if hyperlink found attempt modification of cell
f = open('output.txt', 'w')
for row in ws.rows:
    for cell in row:
        try:
            if len(cell.hyperlink.target)  > 0:
                #"<tr><td><input type='checkbox' ></td><td><a href=" + str(cell.hyperlink.target) + " target='_blank'>"+str(cell.value)+"</a></td><td><input type='button' value=''></td><td><input type='button' value=''></td><td><input type='button' value=''></td></tr>"
                cell.value = "".join(["<tr><td><input type='checkbox' ></td><td><a href=" + str(cell.hyperlink.target) + " target='_blank'>"+str(cell.value)+"</a></td><td><input type='button' value=''></td><td><input type='button' value=''></td><td><input type='button' value=''></td></tr>"])
                # Join cell.value and hyperlink target into string (optionally just assign the hyperlink.target to the cell.value
                # print(cell.value)
                f.write(cell.value)
                f.write('\n')
        except:
            pass

# save workbook to temp .xlsx (I could not manage to read from buffer...) .
# wb.save("output.txt")

# # read with pandas 
# data = pd.read_excel("temp.xlsx")

# # take DataSeries and rsplit by "|" and expand to 2 columns
# hyper = (data.Problems.str.rsplit("|", expand=True))

# #set labels
# hyper.columns=["Label","Hyperlink"]

# # join them back to dataframe on index
# data = data.join(hyper, how="left")

# done