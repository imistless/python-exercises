#Estrutura de Decisão

class DecisionExercises: 
    
    #1
    def numbers_comparator(): 
        number1 = int(input("Inform a number: "))
        number2 = int(input("Inform a number: "))
        
        if number1 > number2:
            print(number1)
        else: 
            print(number2)
    
    #2
    def positive_negative(): 
        number = int(input("Inform a number: "))
        
        if number < 0:
            print("This is a negative number.")
        else: 
            print("This is a positive number.")
    
    #3 
    def feminine_masculine(): 
        gender = input("Inform your gender(F/M): ") 
        
        if(gender == 'F'):
            print("Gender: F - Feminino")
        elif(gender == 'M'): 
            print("M - Masculino")
        else: 
            print("Sexo Inválido.")
    
    #4
    def vowel_consonant(): 
        letter = input("Inform a letter: ").upper()
        
        if (letter in ['A', 'E', 'I', 'O', 'U']):
            print("It's a vowel")
        else: 
            print("It's a consonant")
    
    #5        
    def grades_student(): 
        grade1 = float(input("inform a grade: "))
        grade2 = float(input("Inform another grade: "))
        
        average = (grade1 + grade2)/2
        
        if(average >= 7):
            print("Aprovado! Média: " + str(average))
        elif (average < 7):
            print("Reprovado! Média: " + str(average))
        else:
            print("Aprovado com Distinção! Média: " + str(average))
            
    #6
    def great_number(): 
        
        number1 = int(input("Inform a number: ")) 
        number2 = int(input("Inform a number: ")) 
        number3 = int(input("Inform a number: ")) 
        bigger = number1

        if (bigger < number2):
            bigger = number2
        elif (bigger < number3):
            bigger = number3
        else: 
            bigger = bigger
            
        print(bigger)
        
    #7 
    def great_minor(): 
        
        number1 = int(input("Inform a number: "))
        number2 = int(input("Inform a number: "))
        number3 = int(input("Inform a number: "))
        bigger = number1
        minor = number1
        
        if (number2 > number1 and number2 > number3):
            bigger = number2
        if (number3 > number1 and number3 > number2):
            bigger = number3
        if(number2 < number1 and number2 < number3): 
            minor = number2
        if(number3 < number1 and number3 < number2): 
            minor = number3
            
        print ("Maior: " + str(bigger) + "\nMenor: " + str(minor))
        
    #8 
    def minor_price(): 
         
        number1 = float(input("Inform price: "))
        number2 = float(input("Inform price: "))
        number3 = float(input("Inform price: "))
        minor = number1
        
        if(number2 < minor and number2 < number3): 
            minor = number2
        if(number3 < minor and number3 < number2): 
            minor = number3
        
        print ("Menor: " + str(minor))
                     
    #9 
    def desc(): 
        number1 = int(input("Inform number: "))
        number2 = int(input("Inform number: "))
        number3 = int(input("Inform number: "))
        
        first = number1
        second = number1
        third = number1
        
        if (number2 < first and number2 < number3):
            first = number2
        if (number3 < number2 and number3 < first):
            first = number3
        
        if (number2 > first and number2 > number3):
            third = number2
        if (number3 > first and number3 > number2):
            third = number3
        
        if (number2 > primeiro and number2 < terceiro):
            segundo = number2
        if (number3 > primeiro and number3 < terceiro):
            segundo = number3
       
        print(primeiro, segundo, terceiro)
        
    #10 
    def period(): 
        shift = input("Inform your shift (M-matutino ou V-Vespertino ou N- Noturno): ") 
        
        if (shift == 'M'):
            print("Bunã dimineaţa!")
        elif(shift == 'V'):
            print("Bunã seara!")
        elif(shift == 'N'):
            print("Noapte Bunã!")
        else:
            print("Valor Inválido!")
        
        
    #11
    def 
        
        
        
