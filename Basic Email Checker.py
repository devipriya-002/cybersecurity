text = input("Enter the email text: ").lower()
risky_words = ["urgent", "verify", "password", "bank", "click"]
found = False
for word in risky_words:
    if word in text:
        found = True
        break
if found:
    print("Warning: This email may be risky")
else:
    print("This email looks safe")
