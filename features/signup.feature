Feature: Testing the signup feature of the Etherscan registration form

    # Rule: Users can register only if they agree on the terms and conditions
        Background: User enters basic information on the registration form
            Given a user on the Etherscan registration form
            And the user enters
                | sbertoledi                   | UserName     |
                | a.bertolini1995@gmail.com    | Email        |
                | a.bertolini1995@gmail.com    | ConfirmEmail |
                | password                     | Password     |
                | password                     | Password2    |
            # And the user enters "sbertoledi" as "UserName" 
            # And the user enters "a.bertolini1995@gmail.com" as "Email" 
            # And the user enters "a.bertolini1995@gmail.com" as "ConfirmEmail"
            # And the user enters "password" as "Password"
            # And the user enters "password" as "Password2"

    # Rule: Users can register only if they prove not to be robot and agrees on the terms and conditions
        Scenario: User does not accept the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then they see a T&C error message saying "Please accept our Terms and Conditions."

        Scenario: User accepts the Terms and Conditions
            When the user accepts the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then they see an alert error message saying "Error! Invalid captcha response."
    
        Scenario: User wants to receive Etherscan Newsletter
            When the user accepts the Terms and Conditions
            And the user wants to receive Etherscan Newsletter
            And the user clicks on the "Create an Account" button
            Then they see an alert error message saying "Error! Invalid captcha response."

        Scenario: User is a robot
            When the user accepts the Terms and Conditions
            And the user wants to receive Etherscan Newsletter
            And the user proves not to be a robot
            And the user clicks on the "Create an Account" button
            Then they see an alert error message saying "Error! Invalid captcha response."