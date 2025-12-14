s = "A man, a plan, a canal: Panama"

clean = "".join(ch.lower() for ch in s if ch.isalnum())
a = clean[::-1]
print(a==clean)

