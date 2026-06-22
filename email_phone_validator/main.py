from validator import validate_email, validate_phone

email = input("Enter Email: ").strip()
phone = input("Enter Phone Number: ").strip()

if validate_email(email):
    print("✅ Valid Email")
else:
    print("❌ Invalid Email")

if validate_phone(phone):
    print("✅ Valid Phone Number")
else:
    print("❌ Invalid Phone Number")