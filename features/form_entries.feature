Feature: Testing the Etherscan registration form individual entries

        Background: User goes to the Etherscan registration form
            Given a user on the Etherscan registration form

    # Rule: Username must be from 5 to 30 characters in length and containing only alphanumeric characters
        Scenario: Username is not from 5 to 30 characters in length
            When the user enters "John" as "UserName"
            Then the user sees a "UserName-error" message saying "Please enter at least 5 characters."
        
        Scenario: Username does not only contain alphanumeric characters
            When the user enters "Andrea_Bertolini" as "UserName"
            Then the user sees a "UserName-error" message saying "Only alphanumeric characters allowed."

        Scenario: Username is from 5 to 30 characters in length and only contains alphanumeric characters
            When the user enters "Andrea" as "UserName"
            Then there is no "UserName-error" message

    # Rule: Email address must be valid --> in the form (anything)@(alphanumeric).(alhpanumeric)
        Scenario: User inserts an invalid email address
            When the user enters "andreagmail.com" as "Email"
            Then the user sees a "Email-error" message saying "Please enter a valid email address."

        Scenario: User inserts a valid email address
            When the user enters "andrea@gmail.com" as "Email"
            Then there is no "Email-error" message

    # Rule: Email address must be correctly confirmed
        Scenario: Wrong email is inserted for confirmation
            When the user enters "andre.berto95@gmail.com" as "Email"
            And the user enters "andre.berto98@gmail.com" as "ConfirmEmail"
            Then the user sees a "ConfirmEmail-error" message saying "Email address does not match."

        Scenario: Correct email is inserted for confirmation
            When the user enters "andre.berto95@gmail.com" as "Email"
            And the user enters "andre.berto95@gmail.com" as "ConfirmEmail"
            Then there is no "ConfirmEmail-error" message

    #Rule: Password must be at least 8 characters long
        @current
        Scenario: Password is less than 8 characters long
            When the user enters "test" as "Password"
            Then the user sees a "Password-error" message saying "Your password must be at least 8 characters long."

        Scenario: Password is at least 8 characters long
            When the user enters "testpassword" as "Password" 
            Then there is no "Password-error" message

    # Rule: Password must be correctly confirmed
        Scenario: Wrong password is inserted for confirmation
            When the user enters "password" as "Password" 
            And the user enters "another password" as "Password2" 
            Then the user sees a "Password2-error" message saying "Password does not match, please check again."
        
        Scenario: Correct password is inserted for confirmation
            When the user enters "password" as "Password" 
            And the user enters "password" as "Password2" 
            Then there is no "Password2-error" message
