
def split_bill_with_discount():
    print("Welcome to the Split Bill Calculator!")


    # Get the number of users
    num_users = int(input("Enter the number of users: "))

    # Create a dictionary to store individual user amounts
    user_amounts = {}

    # Get the individual amounts for each user and associate them with a person
    for i in range(1, num_users + 1):
        person_name = input(f"Enter the name of User {i}: ")
        num_items = int(input(f"How many items for {person_name}? "))
        
        total_amount = 0

        for j in range(1, num_items + 1):
            item_amount = float(input(f"Enter the amount for item {j}: $"))
            total_amount += item_amount

        if person_name in user_amounts:
            user_amounts[person_name] += total_amount
        else:
            user_amounts[person_name] = total_amount

    # Calculate the total bill
    total_bill = sum(user_amounts.values())

    # Apply a discount if desired
    discount = float(input("Enter a discount amount (0 for no discount): $"))

    # Divide the discount equally among all users
    discount_per_user = discount / num_users
    for user in user_amounts:
        user_amounts[user] -= discount_per_user

    # Display the results
    print("\nTotal Bill: ${:.2f}".format(total_bill))
    print("Each User Should Pay:")
    for user, amount in user_amounts.items():
        print(f"{user}: ${amount:.2f}")

if __name__ == "__main__":
    split_bill_with_discount()

