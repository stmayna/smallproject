
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

# Apply taxes if desired
tax_rate = float(input("Enter the tax rate (0 for no tax): "))
tax_amount = total_bill * (tax_rate / 100)
total_bill_with_tax = total_bill + tax_amount

# Apply a discount if desired
discount = float(input("Enter a discount amount (0 for no discount): $"))
total_bill_with_discount = total_bill_with_tax - discount

# Divide the total bill with discount among all users
discount_per_user = total_bill_with_discount / num_users
for user in user_amounts:
    user_amounts[user] = (user_amounts[user] / total_bill) * total_bill_with_discount

# Display the results
print("\nTotal Bill before Tax and Discount: ${:.2f}".format(total_bill))
print("Total Bill with Tax and Discount: ${:.2f}".format(total_bill_with_discount))
print("Each User Should Pay (after Tax and Discount):")
for user, amount in user_amounts.items():
    print(f"{user}: ${amount:.2f}")


# Variabel dan List
name = input("Masukan nama anda: ")
personQty = int(input("Masukan jumlah orang: "))
inputMenu = 0
discount = 0
tax = 0
personNameList = []
personOrderList = []

# Opening
print(f"Halo, Selamat datang {name} dan {personQty - 1} orang lainnya!\n")

# Main Menu
while inputMenu != "3":
    print("=== TEMAN SPLIT BILL ===")
    print("1. Masukan Pesanan")
    print("2. Masukan Diskon dan Pajak")
    print("3. Split Bill Result")
    print("4. Keluar dari Aplikasi")
    inputMenu = input("Masukan menu yang ingin anda pilih: ")

    # Menu 1
    if inputMenu == "1":
        print("== Masukan Pesanan ==")
        for i in range(1, personQty + 1):
            personName = input(f"Masukan nama pemesan ke-{i}: ")
            personNameList.append(personName)
            orderQty = int(input(f"Masukkan jumlah pesanan {personName}: "))
            totalOrder = 0
            for j in range(1, orderQty + 1):
                personOrder = float(input(f"Masukkan harga pesanan ke-{j}: Rp"))
                totalOrder += personOrder

            personOrderList.append(totalOrder)

        print("Pesanan telah tersimpan!\n")

    elif inputMenu == "2":
        print("== Masukan Diskon dan Pajak ==")
        discount = float(input("Masukkan jumlah diskon (0 untuk tanpa diskon): Rp"))
        tax = float(input("Masukkan jumlah pajak (0 untuk tanpa pajak): Rp"))

        # Apply discount and tax to each person's order
        for i in range(len(personOrderList)):
            personOrderList[i] -= discount / personQty
            personOrderList[i] += tax / personQty

        print("Diskon dan pajak telah tersimpan!\n")

    elif inputMenu == "3":
        totalBillReal = sum(personOrderList)
        print("== Split Bill Result ==")
        print("Total pesanan: Rp{:.2f}".format(totalBillReal))
        print("Setiap orang harus membayar sebesar: ")
        for i in range(len(personNameList)):
            print(f"{personNameList[i]}: Rp{personOrderList[i]:.2f}")
        print(f"\nTerimakasih Telah Menggunakan Aplikasi ini, {name}!")

        print("ketik MENU untuk kembali ke menu")
        print("ketik EXIT untuk keluar dari aplikasi")
        closing = input("Masukkan pilihan anda: ").lower()
        if closing == "menu":
            continue
        elif closing == "exit":
            print(f"Selamat Tinggal, {name}!")
            break
    
    elif inputMenu == "4":
        print(f"Selamat Tinggal, {name}!")
        break





