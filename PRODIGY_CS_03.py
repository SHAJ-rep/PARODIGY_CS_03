import string  

def chkpassword_complexity(password):

    chk_uppercase = any(char in string.ascii_uppercase for char in password)  # Check if password has uppercase letters
    chk_lowercase = any(char in string.ascii_lowercase for char in password)  # Check if password has lowercase letters
    chk_digit = any(char.isdigit() for char in password)  # Check if password has digits
    chk_symbol = any(char in string.punctuation for char in password)  # Check if password has symbols

    # Determine which requirements are missing
    missing_req = []
    if not chk_uppercase:
        missing_req.append("Missing A-Z")  # Add message if uppercase letters are missing
    if not chk_lowercase:
        missing_req.append("Missing a-z")  # Add message if lowercase letters are missing
    if not chk_digit:
        missing_req.append("Missing 0-9")  # Add message if digits are missing
    if not chk_symbol:
        missing_req.append("Missing @*$% symbols")  # Add message if symbols are missing

    # Provide feedback to the user based on the missing requirements
    if missing_req:
        print("Password not valid!")  # Inform user that password is not valid
        for req in missing_req:
            print(f"- {req}")  # Print each missing requirement
        password_again = input("Enter your password Again: ")  # Prompt user to enter password again
        chkpassword_complexity(password_again)  # Recursively check complexity of new password
    else:
        print("Valid Password")  # Inform user that password is valid

# Example usage:
if __name__ == "__main__":
    password = input("Enter your password: ")  # Prompt user to enter a password
    chkpassword_complexity(password)  # Call the function to check password complexity
