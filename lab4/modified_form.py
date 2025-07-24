max_tries = 5
def valid_email(email):
    try:
        email_parts = email.split("@")
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise ValueError("Invalid email format")
        domain = email_parts[1].split(".")
        if len(domain) < 2 or not all(domain):
            raise ValueError("Invalid domain")
        return True
    except Exception as e:
        return False

def main():
    for i in range(max_tries):
        name = input("Enter your name: ")
        if name.strip().isalpha():
            break
        else:
            print("Please enter a valid name")
    else:
        raise ValueError("Too many invalid name attempts.") 

    for i in range(max_tries):
        email = input("Enter your email: ").strip()

        if valid_email(email):
            print("Logged in Successfully")
            break
        else:
            print("Please enter a valid email")
    else:
        raise ValueError("Too many invalid email attempts.")

if __name__ == "__main__":
    main()
