# pip install twilio  => To download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb91d8ab47615c5427a16e779d255b831"
auth_token = "c7a2db5d5b744c030c5f56439539a52e"
client = Client(account_sid, auth_token)

message = client.messages.create(
    "+919703471377",
    body="Hello from team Pyders. Explore EPAM Career opportunities",
    from_="+12244343756 ",
    media_url="http://www.example.com/hearts.png"
)

print(message.sid)
'''
sample response
{
    "sid": "SMdae4d74ca6944fc8918cd3e01ed2327d",
    "date_created": "Mon, 25 Sep 2017 17:39:06 +0000",
    "date_updated": "Mon, 25 Sep 2017 17:39:06 +0000",
    "date_sent": null,
    "account_sid": "ACb91d8ab47615c5427a16e779d255b831",
    "to": "+919703471377",
    "from": "+12244343756",
    "messaging_service_sid": null,
    "body": "Sent from your Twilio trial account - Hi messgae from Pyders. Explore EPAM Career opportunities",
    "status": "queued",
    "num_segments": "1",
    "num_media": "0",
    "direction": "outbound-api",
    "api_version": "2010-04-01",
    "price": null,
    "price_unit": "USD",
    "error_code": null,
    "error_message": null,
    "uri": "/2010-04-01/Accounts/ACb91d8ab47615c5427a16e779d255b831/Messages/SMdae4d74ca6944fc8918cd3e01ed2327d.json",
    "subresource_uris": {
        "media": "/2010-04-01/Accounts/ACb91d8ab47615c5427a16e779d255b831/Messages/SMdae4d74ca6944fc8918cd3e01ed2327d/Media.json"
    }
}
'''