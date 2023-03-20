Feature: Testing the signup feature of the Etherscan registration form

        Background: User enters basic information on the registration form
            Given a user on the Etherscan registration form
            When the user enters
                | value                        | field        |
                | sbertoledi                   | UserName     |
                | a.bertolini1995@gmail.com    | Email        |
                | a.bertolini1995@gmail.com    | ConfirmEmail |
                | password                     | Password     |
                | password                     | Password2    |

        @conditions_not_accepted
        Scenario: User does not accept the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then the user sees an error message saying "Please accept our Terms and Conditions."

        @conditions_accepted
        Scenario: User accepts the Terms and Conditions
            When the user accepts the Terms and Conditions
            And the user clicks on the "Create an Account" button
            Then the user sees an alert saying "Error! Invalid captcha response."

        @newsletter
        Scenario: User wants to receive Etherscan Newsletter
            When the user accepts the Terms and Conditions
            And the user wants to receive Etherscan Newsletter
            And the user clicks on the "Create an Account" button
            Then the user sees an alert saying "Error! Invalid captcha response."

        @robot
        Scenario: User is a robot
            When the user accepts the Terms and Conditions
            And the user wants to receive Etherscan Newsletter
            And the user proves not to be a robot
            And the user clicks on the "Create an Account" button
            Then the user sees an alert saying "Error! Invalid captcha response."
