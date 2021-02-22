from selenium import webdriver
from requests_html import HTMLSession, AsyncHTMLSession
import time


#Python booth auto-buy

# For using Firefox
brower = webdriver. Firefox(executable_path='/home/coding-error/Program/geckodriver')

#URL of booth 湊あくあ 超BIGぬいぐるみ  "https://hololive.booth.pm/items/2419441"
#brower.get('https://hololive.booth.pm/items/2419441')
brower.get('https://hololive.booth.pm/items/2723533')

buyButton = False

while not buyButton:
    try:
        # If this works then the button is not pytopen
        addToCartBtn = addButton = brower.find_element_by_class_name('disabled')

        # Button isnt open restart the script
        print("Button isnt ready yet")

        # Refresh page after a delay
        time.sleep(1)
        brower.refresh()

    except:

        addToCartBtn = addButton = brower.find_element_by_class_name('add-cart')

        #click the button and end the script
        print('Button was clicked')
        addToCartBtn.click()
        buyButton = True


# SOLD OUT ELEMENT
#<button class="btn add-cart full-length disabled" type="button">
#   <span class="cmd-label">販売期間外です</span>
#</button>

