InstagramBot Clever_unsubscribe

A bot for clever unsubscribe on Instagram. Written in Python, using the Selenium library.

The program makes a list of users who are subscribed to your account, but who are not subscribed to you in return. It unsubscribes your account from each of the users on the list. Before it does this, it asks if you want to make an exception.

Works correctly on Windows and with Google Chrome version 106.0.5249



How do I launch this program?

1. Launch start.bat file.
2. It will ask you for username and password from your account, pass them over.
3. the bot will display a list of everyone you're subscribed to but they're not subscribed to in return. Then it will ask if you want to make an exception (who not to unsubscribe from)
4. The bot will unsubscribe from all the accounts on the list and tell you if it's successful
5. The program asks if you want to do clever unsubscribe for another account
6. The cycle will start over or the process will end




Why doesn't it work?

1. Most likely, Instagram has changed its website structure (the code runs on the Selenium library and searches for elements in the HTML code of the page. If the element you are searching for is not present, an error is generated and the program closes).
2. You could have sent incorrect data (login, password, exclusion list). 3.
3. The accounts you are subscribed to, but they don't exist anymore, could cause an error in your code.
4. Necessary files for work have been deleted.
5. The program works correctly with Windows OS and Google Chrome browser. If your computer has a different operating system, missing or too old version of Google Chrome, it may cause an error in the code.
