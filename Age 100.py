def main():
    age = int(input('What is your age? '))
    name = input('What is your name? ')
    
    year = 2016
    
    while age < 100:
        age +=1
        year +=1
    
    howMany = int(input('How many times do you want the message? '))
    
    for i in range(howMany):
        print ('Hello',name,'you will be 100 in ',year,'.')
        print('')

main()
