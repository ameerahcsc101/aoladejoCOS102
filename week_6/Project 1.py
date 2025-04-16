def calculate_delivery_fee():
    print("Welcome to Simi Services Delivery Fee Checker!\n")

    print("Available Locations:")
    print("1. Ibeju-Lekki")
    print("2. Epe")

    location_input = input("Enter your delivery location: ").strip().lower()
    try:
        weight = float(input("Enter the package weight in kg: "))
    except ValueError:
        print("❌ Invalid weight. Please enter a number.")
        return

    # Normalize location
    if location_input in ["ibeju-lekki", "ibeju", "lekki"]:
        location = "Ibeju-Lekki"
        cost = 5000 if weight >= 10 else 3500
    elif location_input == "epe":
        location = "Epe"
        cost = 10000 if weight >= 10 else 5000
    else:
        print("❌ Invalid location. Please choose between Ibeju-Lekki or Epe.")
        return

    print(f"\n📦 Delivery to {location} for a {weight}kg package will cost: ₦{cost}")

hidden_credits = "This project was designed by Ameerah<3 - 💻💡"

# Run the program
calculate_delivery_fee()




