Feature: Testing the registration form

    Rule: Registration is successful if user fill all the mandatory blank spaces

    Rule: Registration is successful if user does not have already an Etherscan account

        Scenario: User does not have already an Etherscan account
            Given a user with username usr and password pwd
            When the user tries to register on Etherscan
            Then the user should be forbidden to register

        Scenario: User has already an Etherscan account


    Rule: Registration is successful only if username is from 5 to 30 characters in length and only contains alphanumeric characters (done)

        Scenario: Username is from 5 to 30 characters in length and only contains alphanumeric characters (done)

        Scenario: Username is not from 5 to 30 characters in length (done)

        Scenario: Username does not only contain alphanumeric characters (done)


    Rule: Registration is successful only if the same email is inserted twice

        Scenario: Wrong email is inserted for confirmation

        Scenario: Correct email is inserted for confirmation

        Scenario: The confirmation code is sent to the email address

        Scenario: The confirmation code is not sent to the email address

        Scenario: The user does not verify the confirmation email

        Scenario: The user verifies the confirmation email


    Rule: Registration is successful only if the same password is inserted twice

        Scenario: Wrong password is inserted for confirmation

        Scenario: Correct password is inserted for confirmation


    Rule: Registration is successful only if the user agrees on the Terms and Conditions

        Scenario: User agrees on the terms and conditions

        Scenario: User does not agree on the terms and conditions


    Rule: Registration is successful even if the user does not want to receive Etherscan newsletter

        Scenario: User wants to receive Etherscan newsletter

        Scenario: User does not want to receive Etherscan newsletter


    Rule: Registration is successful only if the user proves not to be a robot

        Scenario: User proves not to be a robot

        Scenario: User does not prove not to be a robot



