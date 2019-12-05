import pandas as pd
import numpy as np
file = pd.read_excel("message.xlsx","Sheet1")
file['Snippet'] = file['Snippet'].str[:30]
file['From'] = file['Sender'].str.split("<").str[-1].str.replace('>','')
file['TO'] = file['To'].str.split("<").str[-1].str.replace('>','')
file['To_name'] = file['To'].str.split("<").str[0]
file['From_Name']  = file['Sender'].str.split("<").str[0]
file['Status'] = np.where(file['Label'].str.contains("UNREAD", case=False, na=False), '1', '0')
file['Label1'] = file['Label'].str.replace("UNREAD","").str.split(" ").str[-1]
del file['To']
del file['Sender']
del file['Label']
del file['Unnamed: 0']
column_to_explode = 'Attach_Name'
file = file.loc[:,['TO','Attach_Name']]
file['Attach_Name'] = file['Attach_Name'].tolist()
res = (file
       .set_index([x for x in file.columns if x != column_to_explode])[column_to_explode]
       .apply(pd.Series)
       .stack()
       .reset_index())
res = res.rename(columns={
          res.columns[-2]:'exploded_{}_index'.format(column_to_explode),
          res.columns[-1]: '{}_exploded'.format(column_to_explode)})
print(res.iloc[57,-1],res.iloc[57,-2])
