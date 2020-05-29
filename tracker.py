import requests
from bs4 import BeautifulSoup
import smtplib

URL=''#url of desired product

headers={
    "User-Agent":" " #Add user agent here....You can get it by typing "my user agent in google"
}

def checkPrice():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id='productTitle').get_text()
    price=soup.find(id='priceblock_ourprice').get_text()
    print(title.strip())
    print(price)
    converted_price=price[2:8]
    final_price=" "
    for x in converted_price:
        if x!=',':
            final_price=final_price+x
    eval_price=float(final_price)

    desired_price= '''enter your budget limit here ...int or float format only '''

    if eval_price < desired_price :
        sendEmail()
    
def sendEmail():
    
    #before sending email please allow less secure app in security section of the sender's email-id

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender email','sender email password')

    subject='Price fell down'
    body=f'Check the product link {URL}'
    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
         'sender email',
         'receiver email',
         msg
    )  
    print("Email sent succesfully")
    server.quit()  

if __name__ == "__main__":
    checkPrice()    