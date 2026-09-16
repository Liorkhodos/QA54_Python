# 1
def clean_name (s: str):
    s = s.strip().title()
    return s

print(clean_name("  ADAm smiTH    "))

# 2
def normalize_email (email: str):
    normal_email = email.strip().lower()
    return normal_email

print(normalize_email("  ADAm.smiTH@gmail.com "))

# 3
def is_python_file (file_name: str):
    norm_file_name = file_name.lower()
    if norm_file_name.endswith(".py"):
        return True
    else:
        return False

print(is_python_file("text.txt"))
print(is_python_file("HOmeWORK.Py"))

# 4
def fix_message (msg: str):
    replaced = msg.replace("bad", "good")
    return replaced

message = "bad weather, bad day"
result = fix_message(message)
print(result)
print(message)

# 5
def count_letter(text: str, letter: str):
    norm_text = text.lower()
    norm_letter = letter.lower()
    result = norm_text.count(norm_letter)
    return result

print(count_letter("Mississippi", "i"))

# 6
def create_login(first_name: str, last_name:str):
    norm_first_name = first_name.strip().lower()
    norm_last_name = last_name.strip().lower()
    login = norm_first_name+"."+norm_last_name
    return login

print(create_login("  JOhn ", " sMITH "))

# Bonus 1
def split_name(full_name: str):
    norm_full_name = full_name.strip()
    res = norm_full_name.split()
    return res

print(split_name("  Anna   Smith  "))

# Bonus 2
def check_password(password: str):
    if len(password)>=8:
            if not password.isalpha():
                for char in password:
                    if char.isspace():
                        return False

                return True

    return False

print(check_password("python123"))
