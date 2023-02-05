import pandas
import json
import os 
# Read excel document
# iterate through csv_files with a for loop
# and read each file with pandas.read_csv()

def start():
    files = os.listdir('./csv_files')
    thislist = []
    # print(files)
    for file in files:
        excel_data_df = pandas.read_excel('./csv_files/' + file)

        # Convert excel to string 
        # (define orientation of document in this case from up to down)
        thisisjson = excel_data_df.to_dict(orient='tight')
        thislist.append(thisisjson)
        # Print out the result
    print(thislist)
start()

    