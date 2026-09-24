def greet(name):
    return f"Hello, {name}"
result = greet("Kris")
print(result)

#result2 = greet()
#print(result2)

def create_user (name,role="user"):
    return {"name": name,
            "role": role
            }
print(create_user("Alex"))
print(create_user("Kristina", "admin"))

print()

def cal_discount(price,percent=20):
    return price - (price*percent/100)

print(cal_discount(2000))
print(cal_discount(2000,25))

def foo(a=2,b=3):
    return a+b
print(foo(8)) # если только 1 параметр - присваивает первому аргументу

def add_tests(name,results =[]):
    results.append(name)
    return results

print(add_tests("test_registration"))
print(add_tests("test_login"))

"""
def add_tests(name, results=None):
    if results is None:
        results = []
    results.append(name)
    return results
    но так не сохраняет предыдущие
"""

def create_user2(username,email,role):
    return f"{username} {email} - {role}"
print(create_user2("Kris", "test@gmail.com", "team lead"))

print(create_user2(role="Project",username="Alex",email="test2@gm.com"))

print(create_user2("Kristina", role="QA", email="qa@gmail.com"))
