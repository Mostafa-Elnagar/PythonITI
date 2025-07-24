def check_user(users):
    user = input("Enter your name: ")
    return user in users.keys(), user

def check_pass(user, users):
    password = input("Enter your password: ")
    return users[user] == password


def main(users):
    
    user_exists, user = check_user(users)
    if user_exists:
        for i in range(3):
            right_pass = check_pass(user, users)
            if right_pass:
                print("Logged IN Successfully...")
                return
            else:
                print("Incorrect Password.")
                print(f"{2-i} {'retry' if i == 1 else 'retries'} left.")
    else:
        print(f"User doesn't exist")


if __name__ == "__main__":
    users = [
        {"name": "omar", "pass": "123"},
        {"name": "ahmed", "pass": "123"},
    ]
    main(users)
