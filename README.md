# Python - Web Browser Automation
- This script was made to open web browser tabs in incognito/private mode.

## Requirements
- [Windows](https://www.microsoft.com/en-us/p/windows-10-home/d76qx4bznwk4?rtc=1&activetab=pivot%3aoverviewtab)
- [Python 2/3](https://www.python.org/) installed
- CMD or Terminal/[Powershell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1)/[Windows Powershell](https://docs.microsoft.com/en-us/windows/terminal/get-started)

## Instructions

1. Install dependencies.
2. Create the script.
3. Run and test.

### 1. Install dependencies.
- Navigate to folder location where the script will be held.  Here you can also navigate in your "File Explorer", right click, select "New" and click on "Text Document".  Rename the file anything you wish, but make sure to change the extention file to ".py".  In this tutorial we will call it "Web Browser Automation.py".
```PowerShell
PS > CD '.\Documents\Python\Web Browser\'
```

### 2. Create the script.
1. Import all dependencies that were installed in the beginning.
```python
import webbrowser
```

- We'll go ahead and start an array called "links" and with the variables of links we want to open up.
```python
links = [
	"web.whatsapp.com/",
	"mail.protonmail.com/inbox"
	]
```

- Here we will assign "links_length" to be the length of our "links" array to make it easier to add/delete links.
```python
links_length = len(links)
```

- The following is using FireFox and Google Chrome web browsers.  You can apply to any web browser by following the ".exe" file saved on your computer.  Please note that to open incognito/private tabs, you will have to include the end extention.  If you desire to open up normal tabs just get rid of anything after "--".
```python
firefox = "C:/Program Files/Mozilla Firefox/firefox.exe %s --private"
#google = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
```

- Below is the loop that grabs the aforementioned "links_length" and runs through the array called "links".  Lastly you get the web browser file and open up the links above.
```python
for links_length in links:
	webbrowser.get( firefox ).open_new( links_length )
	#webbrowser.get( google ).open_new( links_length )
```

- Full code.
```python
import webbrowser

links = [
	"web.whatsapp.com/",
	"mail.protonmail.com/inbox"
	]
links_length = len(links)

firefox = "C:/Program Files/Mozilla Firefox/firefox.exe %s --private"
#google = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"

for links_length in links:
	webbrowser.get( firefox ).open_new( links_length )
	#webbrowser.get( google ).open_new( links_length )
```

### 3. Run and test.
- Always want to test it to make sure it's in working order.
```PowerShell
PS > py '.\Web Browser Automation.py'
```