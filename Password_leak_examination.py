import hashlib
import requests

def leaked_password(pw):
  link = f"https://api.pwnedpasswords.com/range/{pw}"
  response = requests.get(link)
  if response.status_code !=200:
    raise RuntimeError("There is an error in fetching data from HIBP API")
  return response.text.splitlines()

def password_analysis(passwordinfo):
  processing = hashlib.sha1(passwordinfo.encode()).hexdigest().upper()
  A = processing[:5]
  B = processing[5:]
  varities = leaked_password(A)
  for var in varities:
    leakedpass, passwOrd = var.split(':')
    if leakedpass == B:
      return f"The password is found in: {passwOrd} = leaks. You should consider changing the password."
  return f"The password {passwordinfo} is not found in the breaches database."

passwordinfo1 = input("Please type the first password for processing:")
passwordinfo2 = input("Please type the second password for processing:")
reportA = password_analysis(passwordinfo1)
reportB = password_analysis(passwordinfo2)
print(reportA)
print()
print(reportB)
