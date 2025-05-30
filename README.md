### Lollapalloza-Ticket-Watcher
A python file usings bs4 and selenium to fetch the lowest price of a 4-day GA ticket on Lollapalooza's officla ticket resale website. The script is also configured to send notifications to your mobile device via Pushover.

## Setup

# Step 1
Make sure to have selenium, bs4 and requests installed.
If you do not have these libraries installed open command prompt and run:
```
pip install requests beautifulsoup4 selenium
```
# Step 2
Go to [https://googlechromelabs.github.io/chrome-for-testing/](url) and download the stable version for your system.
Extract the .zip file and place it in the same location as the watch_lolla_tickets.py file.

# Step 3
Once you have completed the previous steps open command prompt and cd to where the file is located. Once there run:
```
python watch_lolla_tickets.py
```

## Push Notifications
If you want to recieve push notification to your mobile device then sign up for an account on [https://pushover.net/](url) and edit the code to include your user key and api token. You will find your api token when you create an application on the website. Then download the mobile app and sign in under your same account. After that go back to [https://pushover.net/](url) and check that your device is connected. 

## Conclusion
This simple python script only took me an afternoon to make but saved me hundreds of dollars so id call it a success. Good luck to everyone who tries it out!

