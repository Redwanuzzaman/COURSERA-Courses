# ======== 1 =======

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append("{}@{}".format(user, domain))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# ========= 2 ===========

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for value in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


# ========== 3 =========

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group in group_dictionary.keys():
		# Now go through the users in the group
		for users in group_dictionary[group]:
		  lst = []
		  for group in group_dictionary.keys():
		    if users in group_dictionary[group] and users not in lst:
		      lst.append(group)
		  user_groups[users] = lst
	return user_groups
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary


print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
