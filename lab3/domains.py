
def validate_email(email):
    email_parts = email.split("@")
    if len(email_parts) == 2 and email_parts[0] and email_parts[1]:
            domain = email_parts[1].split(".")
            if len(domain) >= 2 and all(domain):
                return True

    return False

def filter_emails(emails):
    return list(filter(validate_email, emails))

def extract_domains(emails):
    return list(map(lambda x: x.split("@")[1], emails))


def main():
   
    emails = [
        "example@gmail.com",
        "example@yahoo.com",
        "example@iti.gov.eg",
        "example@amazon.eg",
        "example@gmailddcom",
        "mostafa",
        "examp.le@gmailddcom",
        "@gmailddcom",
    ]  

    filtered_emails = filter_emails(emails)
    print("Filtered Emails: ", filtered_emails)
    domains = extract_domains(filtered_emails)
    print("Domains: ", domains)

main()