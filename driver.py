import users
import owner

print("-------------Welcome to the restaurant-----------")
print("1.Customer")
print("2.Owner\n")

ch=input("Enter choice:")
users.login(ch)
owner.owner(ch)
