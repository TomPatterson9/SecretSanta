from random import shuffle
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def secretSanta():
    print("Enter the amount of Secret Santa's that you want.")
    x = input()
    print("Enter the emails you want to send the numbers too.")

    i= 0
    santaArray = [None] * x #create 3 arrays 
    santaArrayTwo = [None] *x
    emailArray = ['']*x
    
    for i in range (x): #creaate an incrementing array of tuples 
        santaArray [i] = (i+1,i+1)

    for i in range(x):
        emailArray[i] = raw_input() #add the emails to the array
        print("Enter the next email.")

    print(emailArray)

    shuffle(santaArray) #use random to shuffle the array 

    i =0

    for i in range(len(santaArray)): # loop through the array
        element = santaArray[i]
        elementItem = element[1]

        if i == (len(santaArray)-1): #a base case for the last element
            firstElement = santaArray[i-1]
            firstItem = firstElement[1]
            
            santaArrayTwo[i] = (firstItem, elementItem) # shift the first element to the last one 
            
        elif i == 0: # a base case for the first element 
            lastElement = santaArray[x-1] 
            lastItem = lastElement[1]

            santaArrayTwo[i] =(lastItem, elementItem)
        else:
            nextElement =santaArray[i-1]
            nextItem = nextElement[1]

            santaArrayTwo[i] =(nextItem, elementItem)

            


    email(x, santaArrayTwo, emailArray)


def email(x, santaArrayTwo, emailArray):

    
    for i in range (x):

        yourNumber = santaArrayTwo [i]
        yourItem = yourNumber[0]
        yourItem1 = yourNumber[1]

        fromaddr = "" #insert your email address
        toaddr = emailArray[i]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Secret Santa has arrived"
        body ="Your number is: " + str(yourItem) +"\nYou are buying for: " + str(yourItem1)
        msg.attach(MIMEText(body,'plain'))
            
        server = smtplib.SMTP(host='smtp.gmail.com', port=587) # change to your wanted mail server
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("email", "password")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
    
secretSanta()
