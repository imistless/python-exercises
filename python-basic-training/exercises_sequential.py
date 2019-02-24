#Estrutura Sequencial

class SequentialExercises: 
    
    #1
    def hello_world(): 
        print("hello, World")
    
    #2
    def ask_number():
        number = int(input("Inform a number: "))
        print("Number informed was " + str(number)) 
    
    #3
    def sum_numbers(): 
        number1 = int(input("Inform a number: "))
        number2 = int(input("Inform other number: "))
        print("The sum is " + str(number1 + number2))

    #4
    def grades_average(): 
        notas = []
        x = 0
        while (x < 4): 
            nota = float(input("Inform your grade: "))
            notas.append(nota)
            sum_grade = sum(notas)
            x += 1
        media = sum_grade/4
        print("Your average is " + str(media))
            
     
    #5      
    def meter_to_centimeter(): 
        meter = float(input("Inform a number: "))
        print("Centimeter: " + str(meter * 100))
    
    #6 
    def circle_area(): 
        pi = 3.14
        radius = float(input("Inform radius: "))
        area = pi * radius * radius
        print("Circle area: %.2f" %area)
    
    #7
    def square_area():
        square = float(input("Inform square value: "))
        area = square * square
        print("Area double: " + str(area * 2))
    
    #8
    def monthly_salary(): 
        hour_money = float(input("Inform how much you receive working an hour: "))
        hour_worked = float(input("Inform the hours you worked this month: ")) 
        
        print("Your salary is " + str(hour_money * hour_worked))
    
    #9
    def fahrenheit_to_celsius(): 
        fahr = float(input("Inform fahrenheit degrees: "))
        print("Temperature in celsius: " + str((5 * (fahr-32) / 9)))
     
    #10   
    def celsius_to_fahrenheit(): 
        celsius = float(input("Inform celsius degrees: "))
        print("Temperature in fahrenheit: " + str(((celsius * 9/5) + 32)))
        
    #11
    def int_numbers_real_number(): 
        integer1 = int(input("Inform a integer number: "))
        integer2 = int(input("Inform another integer number: "))
        real1 = float(input("Inform a float number:"))
        
        #o produto do dobro do primeiro com metade do segundo.
        print("\nproduct of twice the first with half of the second.")
        print("Result : " + str((integer1 * 2) * (integer2/2)))
        
        #a soma do triplo do primeiro com o terceiro
        print("sum of the triple of the first with the third.")
        print("Result: " + str(float(integer1*3) + real1))
        
        #o terceiro elevado ao cubo
        print("third raised to the cube.")
        print("Result: " + str(real1**3))
        
        
    #12
    def ideal_weight(): 
        height = float(input("Inform your height: "))
        print("Ideal weight: " + str((72.7 * height) - 58))
        
    #13
    def ideal_weight_gender(): 
        gender = input("Inform your gender(F/M): ")
        height = float(input("Inform your height: "))
        if (gender == 'F'): 
            print("Ideal height female: " + str((72.7 * height) - 58 ))
        else: 
            print("Ideal height masculine: " + str((62.1* height) - 44.7))
            
    #14
    def fish_weight(): 
        weight = float(input("Inform the weight: "))
        if (weight > 50): 
            overflow = weight - 50
            ticket = overflow * 4 
            print("Overflow: " + str(overflow) + "\nTicket: " + str(ticket)) 
        else:
            print("Weight is fine, João Papo-de-Pescador")
            
    #15
    def monthly_salary_advanced(): 
        hour_money = float(input("Inform how much you receive working an hour: "))
        hour_worked = float(input("Inform the hours you worked this month: ")) 
        
        monthly_salary_raw = hour_money * hour_worked 
        monthly_salary_IR = monthly_salary_raw/100*11
        monthly_salary_INSS = monthly_salary_raw/100*8 
        monthly_salary_syndicate = monthly_salary_raw/100*5 
        monthly_salary_liquid = monthly_salary_raw - (monthly_salary_IR + monthly_salary_INSS + monthly_salary_syndicate)
        
        print("Raw Salary: " + str(monthly_salary_raw))
        print("IR: " + str(monthly_salary_IR))
        print("INSS: " + str(monthly_salary_INSS))
        print("Syndicate: " + str(monthly_salary_syndicate))
        print("Liquid Salary: " + str(monthly_salary_liquid))
        
    #16
    def house_painting(): 
        #1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00
        
        square_meters = int(input("Inform square meters: "))
        liter = square_meters / 3
        can = liter / 18 
        price = can * 80
        
        print("Liters: " + str(liter) + "\nPrice: " + str(price))
       
    #17 
    def house_painting_advanced(): 
    #considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
    #e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    
        square_meters = int(input("Inform square meters: "))
        
        liter = square_meters / 6
        
        can = liter / 18 
        galon = liter / 3.6 
        
        price_can = can * 80
        price_can_discount = price_can - (price_can/100*can)
        price_galon = galon * 25
        price_galon_discount = price_galon - (price_galon/100*galon)
        
        price_galon_can_discount = price_can_discount + price_galon_discount

        
        print("If you buy cans: %.2f " %price_can)
        print("If you buy galons: %.2f" %price_galon)
        print("If you buy cans and galons: %.2f" %price_galon_can_discount)
        
    #18
    def download_archive(): 
        
        size_archive = float(input("Inform archive's size (MB): "))
        internet_speed = float(input("Inform internet speed (Mbps): "))
        
        #transfer tax
        max_speed = (internet_speed * 1024)/8
        
        #Tamanho do arquivo / (Velocidade máxima do Download / 1024)
        download_transfer = (size_archive / (max_speed / 1024))/60

        print("Download Transfer: %.2fmin" %download_transfer)
        
        

        
        
        
        