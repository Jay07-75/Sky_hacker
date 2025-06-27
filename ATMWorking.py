

pin=1234
cb=5000
for i in range(3):
    p=int(input("Enter your pin :"))
    if p==pin:
        print("✅ Correct Pin")
        wb=int(input("Enter amount to send :"))
        if cb>=wb:
            cb=cb-wb
            print("Money Sent.")
            print(" ✅ Transaction Successful.")
            print(" 💰 your current balance is", cb ) 
            break
        else:
            print("Insufficient Balance.")
            print("Transaction ❌ unsuccessful.")
    else:
        print(p," 🚫 Your pin is incorrect.")   
        if i<2:
          print("please enter your pin again.")
        else:
            print("you use your limit of pin 3 times 🚫.")   
else:
    print("Your Card is 🔒 Blocked.")
# End of the PROGRAM 

