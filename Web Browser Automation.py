import webbrowser

links = [
    "web.whatsapp.com/",
    "mail.protonmail.com/inbox"
    ]
links_length = len(links)

firefox = "C:/Program Files/Mozilla Firefox/firefox.exe %s --private"
#google = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"

for links_length in links:
    webbrowser.get( firefox ).open_new( links_length )
    #webbrowser.get( google ).open_new( links_length )
