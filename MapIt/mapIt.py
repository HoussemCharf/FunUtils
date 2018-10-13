import webbrowser, sys, pyperclip

sys.argv # ['mapIt.py', '450', 'Serra', 'Mall']

#check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapIt.py', '450', 'Serra', 'Mall']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
