from passlib.hash import argon2

password = input("Enter password to hash: ")
hash_value = argon2.hash(password)

print("\nArgon2 hash:")
print(hash_value)
