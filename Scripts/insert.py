def update():
    import pandas as pd
    import sqlite3
    import numpy as np
    db = sqlite3.connect('Mailing.db')
    c = db.cursor()
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
    new_file = file.drop_duplicates(keep='first')
    new_file.index = range(len(new_file))
    df = pd.read_sql_query("SELECT * FROM Message", db)
    df = df.drop_duplicates(keep='first')
    del df['index']
    print(new_file,df)

    update_db = new_file[~new_file.index.isin(df.index)]
##    c = new_file.index[new_file['MID']==df['MID']].tolist()
##    new_file = new_file.drop(new_file.index[c])
##   
    if not(update_db.empty):
        print(update_db)
        update_db.to_sql("Message",db,if_exists="append")


    ################Mail Datbase#####################################


    mail_db = update_db.loc[:,['MID','Subject','Snippet','Date']]

    if not(mail_db.empty):
        print(mail_db)
        mail_db.to_sql("MAIL",db,if_exists="append")
   

    ##print(c.execute('Select * from Attach').fetchall())

    ###########################FOlder Database####################################
    fol_file = file.drop_duplicates(keep='first')
    folder_db = fol_file.loc[:,['Label1','Size']]
    folder_db = folder_db.groupby(by='Label1').agg({'Size':'sum','Label1':'count'})
    folder_db.rename(columns={"Size":"Folder_Size","Label1":"Folder_count"},inplace=True)
    folder_db.reset_index(inplace=True)
    folder_db.rename(columns = {"Label1":"Folder_name"},inplace=True)
    if not(folder_db.empty):
        print(1)
        folder_db.to_sql("Folder",db,if_exists="replace")

    #######################Reciever Database##########################################
    reciever_db = update_db.loc[:,['From_Name','From','Date','MID']]
    if not(reciever_db.empty):
        print(reciever_db)
        reciever_db.to_sql("Reciever",db,if_exists="append")

    #####################User Database##############################################
    sent_file = update_db.loc[new_file['Label1'] == 'SENT']
    sent_file.reset_index(inplace=True)
    user_db = sent_file.loc[:,['TO','To_name','MID']]
    if not(user_db.empty):
        print(1)
        user_db.to_sql("User",db,if_exists="append")

    ####################Attach Database###############################################
    attach_file = update_db.loc[new_file['Attachment'] == 'Yes']
    attach_db = attach_file.loc[:,['Attach_ID','Attach_Name','Attach_file','Attach_size','MID']]
    
    attach_db.reset_index(inplace=True)
    if not(attach_db.empty):
        print(1)
        attach_db.to_sql("Attach",db,if_exists="append")
    db.commit()
    db.close()
    return update_db
