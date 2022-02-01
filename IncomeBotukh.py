#This program calculate the person tax, based on their income, and number of dependends
import time
while True:
    name = input('\nPlease, enter your fullname (enter pause to stop): ') #Asking used to type their name
    if name == 'pause' or name == 'Pause':
        print ('\nThank you for using Tax Calculator') #Message that appears, if used type end to stop
        break
    try: # Expect the user to input something other than a number
        grossincome=float(input('\nPlease, enter your gross income: ')) #Asking for gross income
        dependents = float(input('\nPlease, enter the number of dependends: '))#Asking for number of dependends
    except:
        print ('\nPlease, input numbers only!')
        break
    #Calculation
    taxableincome = grossincome - 10000 - (3000 * dependents) 
    if grossincome < 10000:
        tax = grossincome * .10
    elif grossincome >=10001 and grossincome <=40000:
        tax = grossincome * .12
    elif grossincome >=40001 and grossincome <=86500:
        tax = grossincome * .22
    elif grossincome >=86501 and grossincome <=165000:
        tax = grossincome * .24
    elif grossincome >= 165001:
        tax = grossincome * .32
    #Output
    print(f"\nDear {name}. Your taxable income is: $ {taxableincome:.2f} .Amount of tax: $ {tax:.2f}")
    print('\nThank you for using Tax Calculator')
    time.sleep(5) #Time delay function to pass the output for 5 seconds


