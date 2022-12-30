email=input("enter your email:").strip()
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print("email: ",email)
print("username:",username,"and","domain:",domain.upper())