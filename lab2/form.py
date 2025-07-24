

def valid_email(email):
    email_parts = email.split("@")
    if len(email_parts) == 2 and email_parts[0] and email_parts[1]:
            domain = email_parts[1].split(".")
            if len(domain) >= 2 and all(domain):
                return True

    return False

def main(max_tries):
    for i in range(max_tries):
        name = input("Enter your name: ")
        if name.strip().isalpha():
            break
        else:
            print("Please enter a valid name")
    else:
        exit()  

    for i in range(max_tries):
        email = input("Enter your email: ").strip()

        if valid_email(email):
            print("Logged in Successfully")
            break
        else:
            print("Please enter a valid email")
    else:
        exit()

if __name__ == "__main__":
    max_tries = 5
    main(max_tries)