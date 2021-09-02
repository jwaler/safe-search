import os

root = "https://"

def query():
    q = input("## Search : \n")
    fq = q.replace(" ", "+")
    return fq

def openup(brow, opt1, url):
    qf = query()
    print("## Opening " + root + url + qf + " ...")
    os.system(brow + opt1 + root + url + qf)
    main()

def website(browser, window):
    if window.upper() in ("Y", "YES"):
        opt1 = "-private-window "
    elif window.upper() in ("N", "NO"):
        opt1 = ""
    print("1. Bing (if no VPN)\n2. Google")
    val2 = int(input(""))
    if val2 == 1:  
        url = "bing.com/search?q="
    elif val2 == 2:
        url = "google.com/search?q="
    else:
        main()
    openup(browser, opt1, url)

def options():
    print("Private? (y/n)")
    looping = True
    message = "## "
    while looping:
        setwin = str(input(message))
        if setwin.upper() in ("N", "NO", "Y", "YES"):
            looping = False
        else:
            looping = True
            message = "## Again? "
    return setwin


def browser(choice):
    if choice == 0:
        quit()
    elif choice == 1:
        val = ("google-chrome ")
        win = "n" #private window by default
    elif choice == 2:
        val = ("firefox ")
        win = options()
    else:
        main()
    website(val, win)

def main():
    intro()
    print("1. Google Chome\n2. Firefox\n3. Stealth mode (VPN)\n4. Stealth mode")
    chc = int(input(""))
    if (type(chc) != int):
        main()
    elif chc == 1 or chc == 2:
        browser(chc)
    elif chc == 3:
        openup("firefox ", "-private-window ", "bing.com/search?q=")
    elif chc == 4:
        openup("firefox ", "-private-window ", "google.com/search?q=")
    else:
        main()
        
def intro():
    print("##############################")
    print("#                            #")
    print("##     SAFE SEARCH V1.0     ##")
    print("#                            #")
    print("##############################")
    print("\n")

main()
