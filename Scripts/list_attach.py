def read_message():
    from apiclient import discovery
    from apiclient import errors
    from httplib2 import Http
    from oauth2client import file, client, tools
    import base64
    from bs4 import BeautifulSoup
    import re
    import time
    import dateutil.parser as parser
    from datetime import datetime
    import datetime
    import csv
    import email

    # Creating a storage.JSON file with authentication details
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly' # we are using modify and not readonly, as we will be marking the messages Read
    store = file.Storage('storage.json') 
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    user_id =  'me'
    unread_msgs = GMAIL.users().messages().list(userId='me',maxResults=100).execute()
    mssg_list = unread_msgs['messages']
    for msg in mssg_list:
        m_id = msg['id']
        try:
            message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute()
            try:
                parts = message['payload']['parts']
                for part in message['payload']['parts']:
                    newvar = part['body']
                    if 'attachmentId' in newvar:
                        att_id = newvar['attachmentId']
                        att = GMAIL.users().messages().attachments().get(userId=user_id, messageId=m_id, id=att_id).execute()
                        data = att['data']
                        print(data['size'])
                        file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                        path = ''.join(["attach", part['filename']])
                        print(path)
            except:
                pass
        except errors.HttpError:
            print ('An error occurred: %s')

if __name__ == "__main__":
    read_message()