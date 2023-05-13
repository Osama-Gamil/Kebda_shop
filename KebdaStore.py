'''"#Welcome to ITI Kebda Shop

Select Mode For customer press 1 , for owner press two , to exist press 0  :  

- Customer
    - To show our products press 1         ---> products & cost
    - To Buy from our products press 2     ---> Able to buy
    - to print the bill press 3
- to exist press 0
- ITI OWNER
    - Add new products       press 1
    - Show Products          press 1
    - Add Cost
    - Change cost
- to exist press 0
 

Notes :
 Delivery will be through github  
        Sha5bat bra7tak n3a git  "'''
	
#list that has the all messages for the program 

message_list = [ 'Welcome to the Kebda Shop ', 'For Customer mode		press 1 \nand 2 for Owner mode 		press 2 \n' ,'to exist 			press 0\n'
,'Thanks for using our shop ']
Customer_Message_list = ['To show our products 		press 1']	
Owner_message_list = ['1- Add new products ', '2- Show Products ' ]

#list of product 
#using list
#shop_products = ("apple", "Orange ", "cherry","ice ","soap ")
thisdict = [
   "1-apple  		   10 " ,
   "2-Orange	           5  ",
   "3-cherry         	   5  ",
   "4-soap           	   2  "
 ]
 
 #lists for the customer data 
Customer_Mony = []
Customer_Prud = []
pill =0 

#printing the Hello msg 
print(message_list[0])
OnCust_mode_select = int(input(message_list[1]+message_list[2]))

#check wither customer mode or owner mode 
if OnCust_mode_select == 0 :
	print(message_list[3])
elif OnCust_mode_select == 1 : 
	x = range(0,1,1)
	for i in x :
		print(Customer_Message_list[i])
	print(message_list[2])	
#to check the customer number that he enter
	Cust_mode = int(input("you chose : "))
	if Cust_mode == 0 :	
		print(message_list[3])
	elif Cust_mode == 1	:
		x = range(0,4,1)
		for i in x : 
			print(thisdict[i])
		#check the user if he want to buy any thing and take from it the number of product and how many 
		checkExit = int(input("if you want to buy enter 1 for exit press 0 "))
		if checkExit == 0 :
			print(message_list[3])
		elif checkExit == 1 :	
			x = True
			while x : 
				product_number = int(input("prudct numer "))
				if(product_number > 4) :
					print("invalid number ")
				else :	
					Customer_Prud.append(product_number)
					product_quntity = int(input("prudct qutity "))
					Customer_Mony.append(product_quntity)
					chekContinue = int(input("for exit press 0 for print list 1 for continue 2 for print the pill 3 "))
					if chekContinue == 0 :
						x = False 
					elif chekContinue == 1 :
						x = range(1)
						for i in x : 
							print(Customer_Prud)
							
					elif chekContinue == 3 :
						y = range(1)
						for i in y : 
							if Customer_Prud[i] == 1:
								pill = 10 * Customer_Mony[i]
							elif Customer_Prud[i] == 2 : 	
								pill = 5 * Customer_Mony[i]
							elif Customer_Prud[i] == 3 	:
								pill = 5 * Customer_Mony[i]
							elif Customer_Prud[i] == 4 	:
								pill = 5 * Customer_Mony[i]	
						print("your pill ", pill)		
elif OnCust_mode_select == 2 : 	
	print("0-for exit")	
	x = range(0,2,1)
	for i in x :
		print(Owner_message_list[i])
	x = True 
	while x :  
		OwnChe = int(input(" you chose : "))
		if 	OwnChe == 0 :
			x = False 	
		elif OwnChe == 1 :
			new_item = input("please enter the product and the price ")
			thisdict.insert(5,new_item)
		elif OwnChe == 2 :	
			k = range(0,4,1)
		for i in k : 
			print(thisdict[k])
		Che = int(input(" 0 for exit 1 for repet the list "))
		if Che == 0:
			x = False 	
print(message_list[3])
			