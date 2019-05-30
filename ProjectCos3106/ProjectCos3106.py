import imaplib, email, os

user = 'pathip9@gmail.com'
password = 'pokkakungru2559'
imap_url = 'imap.gmail.com'
attachment_dir = 'C:/Users/USER/Documents/Code'

def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con
def get_body(msg):
    if msg.is_multipart():return get_body(msg.get_payload(0))
    else: return msg.get_payload(None,True)
def search(key,value,con):
    tmp, data = con.search(None,key,"'{}'".format(value))
    return data
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs
def get_attachments(msg,email_id):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = '{} '.format(email_id)+part.get_filename()
        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))

con = auth(user,password,imap_url)
inbox_size = int(con.select('INBOX')[1][0])

for email_id in range((inbox_size-5),inbox_size):
    tmp, data = con.fetch(str(email_id).encode(), '(RFC822)')
    raw = data[0][1].decode('utf-8')
    message = email.message_from_string(raw)
    email_id = email.message_from_string(raw)
    message['To']
    message['From']
    message['Subject']
    get_attachments(message,email_id)
    print(message)
    print("---------------------------------------------------------------------------")
con.logout()


