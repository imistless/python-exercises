class Pub:
    
    def pub_age_control():
            
        def enter_permission():
            name = input("Inform your name:")
            sex = input("Inform your sex: ")
            age = int(input("Inform your age: "))
            
            if age >= 18:
                age_condition = "You're of age. You can come in."
            else: 
                age_condition = "You're a minor. You can't come in."
        
            return name, sex, age, age_condition
        
        def entry():
            name, sex, age, age_condition = enter_permission()
            print("Name: " + str(name) + ", Sex: " + str(sex) + ", Age: " + str(age) + "\nPermission: " + str(age_condition))
        
        entry()
        answer = True
        while answer == True:
            answer2 = input("Add more?(Y/N):")
            if answer2 in ['y', 'Y']:
                answer = True
                entry()
            else: 
                answer = False
                print('You are welcome.')
                
            
    '''
    i=0
    limit = int(input("limit: "))
    for i in range (limit):
        entry()
    '''

