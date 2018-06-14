from intercom.client import Client
import pyodbc
import os

def TakeCareOfQuote(input):
    return str(input).replace("'", "''")


intercom = Client(personal_access_token=os.environ.get('intercom_personal_access_token'))

# Find user by email
# user = intercom.users.find(email="s.lagousis@sieben.gr")
# print(user.id)

converations = intercom.conversations.find_all()

server = 'tcp:rnd-101'
database = 'Conversations'
username = 'sa'
password = '77java&&'

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

i = 0

cursor.execute('delete from Conversations')
cursor.execute('delete from ConversationParts')
cnxn.commit()

for convo in converations:
    # Get full conversation
    print(i)
    conversation = intercom.conversations.find(id=convo.id)
    sqlcommand = 'insert into Conversations (ConversationID, CreatedAt) values (\'{0}\', \'{1}\')'.format(convo.id,
                                                                                                          conversation.created_at)
    # print(sqlcommand)
    cursor.execute(sqlcommand)

    partnumber = 1

    for part in conversation.conversation_parts:
        sqlcommand = 'insert into ConversationParts (ConversationPartID, ConversationID, PartNumber, CreatedAt, Body, Type, Author) values (\'{0}\', \'{1}\', {2}, \'{3}\', \'{4}\', \'{5}\', \'{6}\')'. \
            format(part.id, convo.id,
                   partnumber,
                   part.created_at,
                   TakeCareOfQuote(part.body),
                   part.part_type,
                   part.author.__class__.__name__)

        print(sqlcommand)
        partnumber += 1
        cursor.execute(sqlcommand)

    i = i + 1
    if i > 30:
        break
    if i % 10 == 0:
        cnxn.commit()

cnxn.commit()
print('Got {0} conversations from Intercom'.format(i))