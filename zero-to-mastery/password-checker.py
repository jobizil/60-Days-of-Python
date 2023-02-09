username = input('>>> Username: ')
password = str(input('>>> Password: '))

password_length = len(password)
hash_password = 10 * '*'

print(f'Dear {username.capitalize()}, your password {hash_password} is {password_length} letters long! ')
