
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'AC84393935d48f1ee510aa169e3bbc78ef'
auth_token = '36c7c1c98479471bcfe5a7ac2472ce1b'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+9170123344444",
    from_="+14195044686",
    body="Hello there!")
