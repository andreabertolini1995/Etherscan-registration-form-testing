Feature: Testing the Etherscan registration form

    Rule: Username must be from 5 to 30 characters in length and containing only alphanumeric characters

        @current
        Scenario: Username is not from 5 to 30 characters in length
            Given a user with username "John"(, email address "john@gmail.com" and password "password")
            When the user enters the username
            Then they see an username error message saying "Please enter at least 5 characters."

        Scenario: Username does not only contain alphanumeric characters
            Given a user with username "Andrea_Bertolini", email address "andrea@gmail.com" and password "password"
            When the user enters the username
            Then they see an username error message saying "Only alphanumeric characters allowed."

        Scenario: Username is from 5 to 30 characters in length and only contains alphanumeric characters
            Given a user with username "Andrea", email address "andrea@gmail.com" and password "password"
            When the user enters the username
            Then there is no username error message

    Rule: Email must be valid

        Scenario: User inserts an invalid email address


        Scenario: User inserts a valid email address

    Rule: Email must be correctly confirmed
        
        Scenario: Wrong email is inserted for confirmation
            Given a user with email address "andre.berto95@gmail.com"
            When the user enters the email address
            And the user enters "andre.berto98@gmail.com" as the email confirmation
            Then they see a confirmation email error message saying "Email address does not match."

        Scenario: Correct email is inserted for confirmation
            Given a user with email address "andre.berto95@gmail.com"
            When the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            Then there is no confirm email error message

    Rule: Password must be correctly confirmed
        
        Scenario: Wrong password is inserted for confirmation
            Given a user with email password "password"
            When the user enters the password
            And the user enters "another password" as the password confirmation
            Then they see a confirmation password error message saying "Password does not match, please check again."
        
        Scenario: Correct password is inserted for confirmation
            Given a user with email password "password"
            When the user enters the password
            And the user enters "password" as the password confirmation
            Then there is no confirm password error message

    Rule: Users can register only if they agree on the terms and conditions

        Scenario: User does not agree on the terms and conditions
            Given a user with username "Andrea", email address "andre.berto95@gmail.com" and password "password"
            When the user enters the username
            And the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            And the user enters the password
            And the user enters "password" as the password confirmation
            And the user does not accept the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then they see a T&C error message saying "Please accept our Terms and Conditions."

        Scenario: User agrees on the terms and conditions
            Given a user with username "Andrea", email address "andre.berto95@gmail.com" and password "password"
            When the user enters the username
            And the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            And the user enters the password
            And the user enters "password" as the password confirmation
            And the user accepts the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then the user can successfully register to Etherscan

    
    Rule: Users can register even if they do not want to receive Etherscan newsletter

        Scenario: User does not want to receive Etherscan newsletter
            Given a user with username "Andrea", email address "andre.berto95@gmail.com" and password "password"
            When the user enters the username
            And the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            And the user enters the password
            And the user enters "password" as the password confirmation
            And the user accepts the Terms and Conditions
            And the user does not want to receive Etherscan Newsletter
            And the user clicks on the "Create an Account" button
            Then the user can successfully register to Etherscan

    Rule: Users can register only if they prove not to be robot

        Scenario: User does not peove not to be a robot
            Given a user with username "Andrea", email address "andre.berto95@gmail.com" and password "password"
            When the user enters the username
            And the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            And the user enters the password
            And the user enters "password" as the password confirmation
            And the user accepts the Terms and Conditions
            And the user does not prove not be a robot
            And the user clicks on the "Create an Account" button
            Then the user can successfully register to Etherscan

        Scenario: User proves not to be a robot
            Given a user with username "Andrea", email address "andre.berto95@gmail.com" and password "password"
            When the user enters the username
            And the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            And the user enters the password
            And the user enters "password" as the password confirmation
            And the user accepts the Terms and Conditions
            And the user proves not be a robot
            And the user clicks on the "Create an Account" button
            Then they see an alert error message saying "Error! Invalid captcha response."