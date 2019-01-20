import webbrowser, sys, pyperclip

#if there is any arguments passed
if len(sys.argv) > 1:
    #join all the elements passed in the command line, stripping out the actual script name
    address = ' '.join(sys.argv[1:])
#This assumes there is an arguement waiting in the user's clipboard
else:
    address = pyperclip.paste()

#This will bring up a web browser and navigate to the google maps entry of the address given
webbrowser.open('http://www.google.com/maps/place/' + address)
