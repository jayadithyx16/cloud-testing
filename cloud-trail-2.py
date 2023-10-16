from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# with open("session_cookies.pkl", "rb") as file:
#     session_cookies = pickle.load(file)

driver=webdriver.Chrome()
driver.implicitly_wait(10)
# city=input("Enter your city: ")
city = "chennai"
selected_theatres=["Devi Cineplex, Anna Salai","INOX Chandra Metro Mall, Virugambakkam","PVR Palazzo-The Nexus Vijaya Mall","PVR VR Mall, Anna Nagar","PVR Sathyam Royapettah"]
# selected_theatres=["PVR Palazzo-The Nexus Vijaya Mall"]

ticketwebsite = f"https://ticketnew.com/movies/{city}"
driver.get(ticketwebsite)
login_button=driver.find_element(By.CSS_SELECTOR,".DesktopHeaderTPMC_loginBtn__P457U > span:nth-child(1)")
login_button.click()
time.sleep(3)
iframe = driver.find_element(By.ID, "oauth-iframe")
driver.switch_to.frame(iframe)
phoneno_section = driver.find_element(By.ID, 'email_mobile_login')  #
phoneno_section.send_keys("7448389337")
phoneno_section.send_keys(Keys.ENTER)

otp=input("Enter the otp:")
otp_section=driver.find_element(By.ID,'otp_login')
otp_section.send_keys(otp)
# otp_section.send_keys(Keys.ENTER)
driver.switch_to.default_content()

selected_screens=["4K DOLB...","PXL LAS...","4K ATMO...","DOLBY 7.1","PARADISE","IMAX"]
#selected_screens=["4K DOLB..."]

# for cookie in session_cookies:The Exorcist: Believer
#     driver.add_cookie(cookie)
# linkt="The Exorcist: Believer"
linkt="Chithha"

driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
movie_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, linkt)))
if movie_link:
    print("movies found")
    movie_link.click()
    # lang_select=driver.find_element(By.CSS_SELECTOR,"div.LanguageSelectionDialog_radio__EwBMZ:nth-child(4) > label:nth-child(3)")
    # lang_select.click()
    # proceed_btn=driver.find_element(By.CSS_SELECTOR,".Button_btn__NHo2w")
    # proceed_btn.click()
    dateremove=driver.find_element(By.CSS_SELECTOR,"a.DatesDesktop_cinemaDates__LTuKu:nth-child(2) > div:nth-child(1)")
    dateremove.click()
    # datechange=driver.find_element(By.CSS_SELECTOR,"a.DatesDesktop_cinemaDates__LTuKu:nth-child(3) > div:nth-child(1) > div:nth-child(1)")
    # datechange.click()
    time.sleep(5)
    while True:
        try:
            for i in range(1,50):
                theatre=driver.find_element(By.CSS_SELECTOR,f"div.MovieSessionsListingDesktop_movieSessions__YBUAu:nth-child({i}) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)")
                theatre_name=theatre.text
                print(theatre_name)
                movie_index=i
                print(movie_index)
                condition=16
                if theatre_name not in selected_theatres:
                    continue
                elif i==condition:
                    print('thats good')
                    time.sleep(1.5)
                    driver.refresh()
                elif theatre_name in selected_theatres:

                    for i in range(1,11):
                        oktime=False
                        okscreen=False
                        screen_name = None
                        try:
                            showtime=driver.find_element(By.CSS_SELECTOR,
                                                f"div.MovieSessionsListingDesktop_movieSessions__YBUAu:nth-child({movie_index}) > div:nth-child(3) > div:nth-child({i}) > div:nth-child(2)")
                            time_text = showtime.text
                            print(time_text)
                            if theatre_name=="INOX Chandra Metro Mall, Virugambakkam":
                                okscreen = True
                            elif theatre_name!="INOX Chandra Metro Mall, Virugambakkam":

                                try:
                                    screen = driver.find_element(By.CSS_SELECTOR,
                                                                 f"div.MovieSessionsListingDesktop_movieSessions__YBUAu:nth-child({movie_index}) > div:nth-child(3) > div:nth-child({i}) > span:nth-child(3)")
                                    # buy_button.click()
                                    screen_name = screen.text
                                    print(screen_name)
                                    if screen_name in selected_screens:
                                        okscreen=True

                                except:
                                    pass
                                finally:
                                    pass


                        except:
                            pass

                        if any(time_str in time_text for time_str in
                               ['04:30 PM','01:25 PM','11:55 AM','03:00 PM','03:00 PM','12:20 PM','03:05 PM','11:30 AM','12:35 PM','11:45 AM','04:50 PM','12:25 PM','12:50 PM','03:45 PM','03:55 PM','02:15 PM','11:55 AM','01:20 PM','03:30 PM','03:20 PM','12:05 AM','03:30 PM','04:10 PM','09:00 AM','09:30 AM','09:40 AM','09:45 AM','11:50 AM', '11:35 AM','11:00 AM', '12:15 PM','12:00 PM', '01:00 PM', '02:00 PM', '03:10 PM','03:25 PM','03:45 PM','03:00 PM','12:45 PM','04:00 PM','10:00 AM','10:25 AM','11:05 AM','12:40 PM','04:00 PM','04:05 PM','03:40 PM','10:30 PM']):
                            oktime=True
                        if oktime and okscreen:
                            import asyncio
                            from telegram import Bot

                            bot = Bot(token='6612388626:AAFL2n50i-vV9lFxr6ThC9pv1L0VSfh1HIQ')
                            channel_chat_id = '-1001920200362'

                            message = f"{theatre_name} bookinngs opened."


                            async def send_message():
                                await bot.send_message(chat_id=channel_chat_id, text=message)


                            loop = asyncio.get_event_loop()
                            loop.run_until_complete(send_message())


                            print('working')
                            newmethod=False
                            newmethod2=False
                            showtime.click()
                            # proceed_btn1=driver.find_element(By.CSS_SELECTOR,"button.Button_btn__NHo2w:nth-child(2)")
                            # proceed_btn1.click()
                            if theatre_name=="INOX Chandra Metro Mall, Virugambakkam":
                                try:
                                    element = driver.find_element(By.CSS_SELECTOR,
                                                                  "div.FixedSeatingDesktop_layoutCon__HvWWe:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(2) > div:nth-child(26) > span:nth-child(1)")


                                    newmethod2=True
                                except:
                                    pass
                                rowno = 3
                                elitestartseat=1
                                eliteendseat=24
                                elitestartseatbig = 9
                                eliteendseatbig = 27
                                elitetrialrowstartbig = 4
                                elitetrialrowendbig = 6
                                elitetrialrowstart=4
                                elitetrialrowend=6
                                step=1
                                eliteskipper = [10,11,12,13]
                                eliteskipperbig = [21,22]
                            elif theatre_name=="PVR Sathyam Royapettah":
                                if screen_name=="4K DOLB...":
                                    rowno=5
                                    elitestartseat=6
                                    eliteendseat=22
                                    step=1
                                    eliteskipper=[17,18]
                                    elitetrialrowstart=6
                                    elitetrialrowend=8

                                elif screen_name=="4K ATMO...":
                                    rowno = 3
                                    elitestartseat = 1
                                    eliteendseat = 23
                                    step = 1
                                    eliteskipper = [11, 12]
                                    elitetrialrowstart = 4
                                    elitetrialrowend = 6

                            elif theatre_name=="Devi Cineplex, Anna Salai":
                                rowno=3
                                elitestartseat = 13
                                eliteendseat = 32
                                step=1
                                eliteskipper=[11,29,30]
                                elitetrialrowstart= 4
                                elitetrialrowend= 6
                            elif theatre_name == "PVR VR Mall, Anna Nagar":
                                if screen_name == "PXL LAS...":
                                    rowno = 7
                                    elitestartseat = 11
                                    eliteendseat = 36
                                    step = 1
                                    eliteskipper = [28, 29]
                                    elitetrialrowstart = 8
                                    elitetrialrowend = 10
                                elif screen_name == "4K ATMO...":
                                    rowno = 4
                                    elitestartseat = 8
                                    eliteendseat = 32
                                    step = 1
                                    eliteskipper = [22]
                                    elitetrialrowstart = 5
                                    elitetrialrowend = 7

                                elif screen_name == "4K DOLB...":
                                    rowno = 7
                                    elitestartseat = 11
                                    eliteendseat = 32
                                    step = 1
                                    eliteskipper = [23,24,25]
                                    elitetrialrowstart = 8
                                    elitetrialrowend = 10

                            elif theatre_name == "PVR Palazzo-The Nexus Vijaya Mall":
                                if screen_name=="IMAX":
                                    newmethod=True
                                    rowno = 4
                                    startseat = 14
                                    endseat = 30
                                    step = 1
                                    trialstart = 5
                                    trialend = 7
                                elif screen_name == "4K ATMO...":
                                    rowno = 4
                                    elitestartseat = 13
                                    eliteendseat = 32
                                    step = 1
                                    eliteskipper = [21,22]
                                    elitetrialrowstart = 5
                                    elitetrialrowend = 7

                                elif screen_name == "4K DOLB...":
                                    rowno = 4
                                    elitestartseat = 10
                                    eliteendseat = 25
                                    step = 1
                                    eliteskipper = [17,18]
                                    elitetrialrowstart = 5
                                    elitetrialrowend = 7


                            if newmethod:
                                for i in range(startseat,endseat,step):
                                    if i == 24 or i==25:
                                        continue
                                    select_seats = driver.find_element(By.CSS_SELECTOR,
                                                                       f".FixedSeatingDesktop_rightRow__xV2q1 > ul:nth-child(1) > li:nth-child({rowno}) > div:nth-child(2) > div:nth-child({i}) > span:nth-child(1)")
                                    try:
                                        select_seats.click()
                                    except:
                                        continue
                                total_tickets = driver.find_element(By.CSS_SELECTOR,
                                                                    ".SeatLayoutFooterDesktop_ticketCount__egpht")


                                parts = total_tickets.text.split('X', 1)  # Split at the first occurrence of 'X'
                                result = parts[0].strip()  # Remove leading and trailing spaces
                                print(result)

                                if result!="Tickets 10":
                                    for i in range(startseat, endseat):
                                        for trial in range(trialstart, trialend):
                                            select_seats = driver.find_element(By.CSS_SELECTOR,
                                                                               f".FixedSeatingDesktop_rightRow__xV2q1 > ul:nth-child(1) > li:nth-child({trial}) > div:nth-child(2) > div:nth-child({i}) > span:nth-child(1)")
                                            try:
                                                select_seats.click()
                                            except:
                                                continue
                                        total_tickets = driver.find_element(By.CSS_SELECTOR,
                                                                            ".SeatLayoutFooterDesktop_ticketCount__egpht")
                                        if result=="Tickets 10":
                                            break
                                elif result == "Tickets 10":
                                    book_ticket = driver.find_element(By.CSS_SELECTOR, ".Button_btn__NHo2w")
                                    if book_ticket:
                                        print('bt1')
                                        book_ticket.click()
                                    proceed = driver.find_element(By.CSS_SELECTOR, ".Button_is-capsulePrimary__l86Jm")
                                    if proceed:
                                        print('bt2')
                                        proceed.click()
                                    try:
                                        closead = driver.find_element(By.CSS_SELECTOR, ".closeModal")
                                        if closead:
                                            print('bt3')
                                            closead.click()
                                    except:
                                        pass
                                    proceed_to_pay = driver.find_element(By.CSS_SELECTOR, ".Button_btn__NHo2w")
                                    if proceed_to_pay:
                                        print('bt4')
                                        proceed_to_pay.click()
                                    paytm_payment = driver.find_element(By.CSS_SELECTOR, ".ptm-custom-btn")
                                    if paytm_payment:
                                        print('bt5')
                                        paytm_payment.click()
                                        time.sleep(660)

                            elif not newmethod and not newmethod2:
                                print('tryying selecting seats')
                                for i in range(elitestartseat,eliteendseat,step):
                                    # for trial in range(trialstart,trialend):
                                    if i in eliteskipper:
                                        continue
                                    select_seats=driver.find_element(By.CSS_SELECTOR,f"div.FixedSeatingDesktop_layoutCon__HvWWe:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({rowno}) > div:nth-child(2) > div:nth-child({i}) > span:nth-child(1)")
                                    try:
                                        select_seats.click()
                                    except:
                                        continue
                                try:

                                    print('checking for total tickets')
                                    total_tickets=driver.find_element(By.CSS_SELECTOR,".SeatLayoutFooterDesktop_ticketCount__egpht")
                                    parts = total_tickets.text.split('X', 1)  # Split at the first occurrence of 'X'
                                    result = parts[0].strip()  # Remove leading and trailing spaces
                                    print(result)
                                except:
                                    result="Tickets 0"

                                if result != "Tickets 10":
                                    print('didnt get 10 tickets yet')
                                    for trial in range(elitetrialrowstart, elitetrialrowend):
                                        for i in range(elitestartseat, eliteendseat):
                                            if i in eliteskipper:
                                                continue

                                            select_seats = driver.find_element(By.CSS_SELECTOR,
                                                                               f"div.FixedSeatingDesktop_layoutCon__HvWWe:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({trial}) > div:nth-child(2) > div:nth-child({i}) > span:nth-child(1)")
                                            print(select_seats)
                                            try:
                                                select_seats.click()
                                            except:
                                                continue
                                        try:
                                            total_tickets = driver.find_element(By.CSS_SELECTOR,
                                                                            ".SeatLayoutFooterDesktop_ticketCount__egpht")
                                            parts = total_tickets.text.split('X',
                                                                             1)  # Split at the first occurrence of 'X'
                                            result = parts[0].strip()  # Remove leading and trailing spaces
                                            print(result)
                                        except:
                                            result="Tickets 0"
                                        if result == "Tickets 10":
                                            break
                                elif result=="Tickets 10":
                                    print('clicked 10 tickets')
                                    book_ticket=driver.find_element(By.CSS_SELECTOR,".Button_btn__NHo2w")
                                    if book_ticket:
                                        print('bt1')
                                        book_ticket.click()

                                    proceed=driver.find_element(By.CSS_SELECTOR,".Button_is-capsulePrimary__l86Jm")
                                    if proceed:
                                        print('bt2')
                                        proceed.click()
                                    try:
                                        closead=driver.find_element(By.CSS_SELECTOR,".closeModal")
                                        if closead:
                                            print('bt3')
                                            closead.click()
                                    except:
                                        pass
                                    proceed_to_pay=driver.find_element(By.CSS_SELECTOR,".Button_btn__NHo2w")
                                    if proceed_to_pay:
                                        print('bt4')
                                        proceed_to_pay.click()
                                    paytm_payment=driver.find_element(By.CSS_SELECTOR,".ptm-custom-btn")
                                    if paytm_payment:
                                        print('bt5')
                                        paytm_payment.click()
                                        time.sleep(660)
                            elif newmethod2:
                                print('tryying selecting seats')
                                for i in range(elitestartseatbig, eliteendseatbig, step):
                                    # for trial in range(trialstart,trialend):
                                    if i in eliteskipperbig:
                                        continue
                                    select_seats = driver.find_element(By.CSS_SELECTOR,
                                                                       f"div.FixedSeatingDesktop_layoutCon__HvWWe:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({rowno}) > div:nth-child(2) > div:nth-child({i}) > span:nth-child(1)")
                                    try:
                                        select_seats.click()
                                    except:
                                        continue
                                try:

                                    print('checking for total tickets')
                                    total_tickets = driver.find_element(By.CSS_SELECTOR,
                                                                        ".SeatLayoutFooterDesktop_ticketCount__egpht")
                                    parts = total_tickets.text.split('X', 1)  # Split at the first occurrence of 'X'
                                    result = parts[0].strip()  # Remove leading and trailing spaces
                                    print(result)
                                except:
                                    result = "Tickets 0"

                                if result != "Tickets 10":
                                    print('didnt get 10 tickets yet')
                                    for trial in range(elitetrialrowstartbig, elitetrialrowendbig):
                                        for i in range(elitestartseatbig, eliteendseatbig):
                                            if i in eliteskipperbig:
                                                continue

                                            select_seats = driver.find_element(By.CSS_SELECTOR,
                                                                               f"div.FixedSeatingDesktop_layoutCon__HvWWe:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({trial}) > div:nth-child(2) > div:nth-child({i}) > span:nth-child(1)")
                                            print(select_seats)
                                            try:
                                                select_seats.click()
                                            except:
                                                continue
                                        try:
                                            total_tickets = driver.find_element(By.CSS_SELECTOR,
                                                                                ".SeatLayoutFooterDesktop_ticketCount__egpht")
                                            parts = total_tickets.text.split('X',
                                                                             1)  # Split at the first occurrence of 'X'
                                            result = parts[0].strip()  # Remove leading and trailing spaces
                                            print(result)
                                        except:
                                            result = "Tickets 0"
                                        if result == "Tickets 10":
                                            break
                                elif result == "Tickets 10":
                                    print('clicked 10 tickets')
                                    book_ticket = driver.find_element(By.CSS_SELECTOR, ".Button_btn__NHo2w")
                                    if book_ticket:
                                        print('bt1')
                                        book_ticket.click()

                                    proceed = driver.find_element(By.CSS_SELECTOR, ".Button_is-capsulePrimary__l86Jm")
                                    if proceed:
                                        print('bt2')
                                        proceed.click()
                                    try:
                                        closead = driver.find_element(By.CSS_SELECTOR, ".closeModal")
                                        if closead:
                                            print('bt3')
                                            closead.click()
                                    except:
                                        pass
                                    proceed_to_pay = driver.find_element(By.CSS_SELECTOR, ".Button_btn__NHo2w")
                                    if proceed_to_pay:
                                        print('bt4')
                                        proceed_to_pay.click()
                                    paytm_payment = driver.find_element(By.CSS_SELECTOR, ".ptm-custom-btn")
                                    if paytm_payment:
                                        print('bt5')
                                        paytm_payment.click()
                                        time.sleep(660)

        except:
            pass
        finally:
            pass
        time.sleep(1.5)
        driver.refresh()
