from twilio.rest import Client

account_sid = 'AC35a43368114f115baac776029167317c'
auth_token = '8cfe654e7fa576d7961f8698f0b015fd'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+19284823038',
    body='Hello Saurabh, this is your bot JARVIS! Good Morning!',
    to='+919652723113'
    )

print(message.sid)

# ---------------Whatsapp_SMS----------------------
from twilio.rest import Client

account_sid = 'ACd14286b3a8d093f71f4ec72eb9143e1f'
auth_token = 'ad3a486ed06500c654d82028e56d34df'

client = Client(account_sid, auth_token)

message = client.messages.create(
         # media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',
         body="Hello Saurabh. This is your bot: JARVIS, reporting on duty!",
         to='whatsapp:+919652723113'
         )

print(message.sid)