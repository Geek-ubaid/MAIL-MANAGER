def pretty_format(file):
    import pandas as pd
    import sqlite3
    import numpy as np
    file['Snippet'] = file['Snippet'].str[:30]
    file['From'] = file['Sender'].str.split("<").str[-1].str.replace('>','')
    file['TO'] = file['To'].str.split("<").str[-1].str.replace('>','')
    file['To_name'] = file['To'].str.split("<").str[0]
    file['From_Name']  = file['Sender'].str.split("<").str[0]
    file['From_Name'] = file['From_Name'].str.replace('"','')
    file['Status'] = np.where(file['Label'].str.contains("UNREAD", case=False, na=False), '1', '0')
    file['Label1'] = file['Label'].str.replace("UNREAD","").str.split(" ").str[-1]
    del file['To']
    del file['Sender']
    del file['Label']
    del file['Unnamed: 0']
    return file.drop_duplicates(keep='first')
