Feature: Testing the signup feature of the Etherscan registration form

    # Rule: Users can register only if they agree on the terms and conditions
        Background: User enters basic information on the registration form
            Given a user with username "Andrea", email address "andre.berto95@gmail.com" and password "password"
            When the user enters the username
            And the user enters the email address
            And the user enters "andre.berto95@gmail.com" as the email confirmation
            And the user enters the password
            And the user enters "password" as the password confirmation

        Scenario: User does not agree on the terms and conditions
            And the user does not accept the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then they see a T&C error message saying "Please accept our Terms and Conditions."

        Scenario: User agrees on the terms and conditions
            And the user accepts the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then the user can successfully register to Etherscan

    
    # Rule: Users can register even if they do not want to receive Etherscan newsletter
        @current
        Scenario: User does not want to receive Etherscan newsletter
            And the user accepts the Terms and Conditions
            And the user does not want to receive Etherscan Newsletter
            And the user clicks on the "Create an Account" button
            Then the user can successfully register to Etherscan

    # Rule: Users can register only if they prove not to be robot
        Scenario: User does not peove not to be a robot
            And the user accepts the Terms and Conditions
            And the user does not prove not be a robot
            And the user clicks on the "Create an Account" button
            Then the user can successfully register to Etherscan

        Scenario: User proves not to be a robot
            And the user accepts the Terms and Conditions
            And the user proves not be a robot
            And the user clicks on the "Create an Account" button
            Then they see an alert error message saying "Error! Invalid captcha response."
