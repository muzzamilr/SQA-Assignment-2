#install selenium
#install selenium-requests
from seleniumrequests import Chrome

# path of the 'chromedriver'
path = "C:\\Users\\Muzzamil Raza\\Downloads\\chromedriver.exe"
webdriver = Chrome(path)

response = webdriver.request('GET', 'https://api.themotivate365.com/stoic-quote')

print(response)
print(response.text)
