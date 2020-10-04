##The program below will test for user input on the bases of age, if the user is qualified to apply for license or not.  

validate_age = {}

applicant = input("\n Please enter your name : ")

#take inputs from applicants for driver's license

age = int(input("\n Please enter your age : "))

license_application = True

#while your purpose is for license application. 

while license_application:

    validate_age[applicant] = age
    
    if age < 18:
        junior_applicant = input("will you like to apply for the junior driving lessons?: ")


        if junior_applicant == "yes":
            print("You may click the link in the application section below")

        else:
            print(" May be you can apply again when you are 18")
            license_application = False

    else:
        for applicant, age in validate_age.items():
            print('Dear' + ' ' + applicant + ', ' + 'with Your age: '+ str(age) + ' '  + 'You may proceed with your application' )

        license_application = False
