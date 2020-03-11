from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=D:\\Anuraj\\selenium profile\\Profile 1")

def takeCommand():
    str = input()
    return str
count = 0
def speak(str):
    print(str)
query = takeCommand()
if 'whatsapp' in query or 'send a message to' in query:
    try:
        query = query.replace("whatsapp ", "")
    except:
        pass
    try:
        query = query.replace("whatsapp")
    except:
        pass
    try:
        query = query.replace("send a message to ", "")
    except:
        pass
    
    if len(query) == 0:
        speak("To whom sir?")
        query = takeCommand()

    if count == 0:
        driver = webdriver.Chrome(options = chrome_options)
        count = 1
    if 'WhatsApp' not in driver.title:
        driver.get('https://web.whatsapp.com')
        speak("sir please scan the Qr code, if already scanned just say ok ")

    while True:
        check = takeCommand()
        if 'proceed' in check or 'done' in check or 'ok' in check:
            token = 1
            break
        elif 'quit' in check or 'exit' in check:
            driver.quit()
            token = 0
            break
    else:
        token = 1
    if token == 1:
        speak("sir message please")
        msg = takeCommand()
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(query.title()))
        user.click()
        string = " 'This message is send by my virtual assistance' **"
        msg_box = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[2]/div[1]/div[2]")
        msg_box.send_keys('*' + msg + string)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()

