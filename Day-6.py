'''
LOGIN SYSTEM
'''
username = input('Username > ')
password = input('Password > ')

if username == 'LilySparkle' and password == '1234':
    print('Greetings, LilySparkle!') 
    print('May your day be as bright and joyful as your sparkles!')
elif username == 'EthanExplorer' and password == 'qwerty':
    print('Hey there, EthanExplorer!')
    print('Wishing you exciting adventures and amazing discoveries!')
elif username == 'SarahSunshine' and password == 'password':
    print('Hello, SarahSunshine!')
    print('May your life be filled with warmth and positivity!')
else:
    print("There's no such user or the password is wrong. Try again.")