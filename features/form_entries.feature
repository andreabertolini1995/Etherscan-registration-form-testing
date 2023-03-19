Feature: Testing the indvidual entries of the Etherscan registration form

        Background: User goes to the Etherscan registration form
            Given a user on the Etherscan registration form

        @wrong_format
        Scenario Outline: Entries are insterted in the wrong format
            When the user enters <value> as <field>
            Then the user sees a <error_type> message saying <error_message>

        Examples: Username is less than 5 characters long and/or it does not only contain alphanumeric characters 
        | value            | field     | error_type      | error_message                         |
        | John             | UserName  | UserName-error  | Please enter at least 5 characters.   |
        | Andrea_Bertolini | UserName  | UserName-error  | Only alphanumeric characters allowed. |

        # Email address is valid if in the form: (anything)@(alphanumeric)
        Examples: Email address is not valid 
        | value            | field     | error_type   | error_message                         |
        | andreagmail.com  | Email     | Email-error  | Please enter a valid email address.   |
        | andrea@+-.com    | Email     | Email-error  | Please enter a valid email address.   |
        | /@_.com          | Email     | Email-error  | Please enter a valid email address.   |

        Examples: Password is more than 8 characters long
        | value            | field     | error_type      | error_message                                     |
        | test             | Password  | Password-error  | Your password must be at least 8 characters long. |

        
        @correct_format
        Scenario Outline: Entries are inserted in the correct format
            When the user enters <value> as <field>
            Then there is no <error_type> message 

        Examples: Username is between 5 and 30 characters long and it only contains alphanumeric characters 
        | value       | field     | error_type      |
        | Andrea      | UserName  | UserName-error  |
        | TestUser98  | UserName  | UserName-error  |

        Examples: Email address is valid
        | value              | field  | error_type   |
        | andrea@gmail.com   | Email  | Email-error  |
        | _@andrea.42        | Email  | Email-error  |

        Examples: Password is at least 8 characters long
        | value          | field     | error_type      |
        | testpassword   | Password  | Password-error  |
        | 12345678       | Password  | Password-error  |

        
        @wrong_confirmation
        Scenario Outline: Wrong entries are inserted for confirmation
            When the user enters <value> as <field>
            And the user enters <confirmation> as <confirmation_field>
            Then the user sees a <error_type> message saying <error_message>
        
        Examples: Wrogn email confirmation
        | value                   | field  | confirmation             | confirmation_field       | error_type          | error_message                   | 
        | andre.berto95@gmail.com | Email  | andre.berto98@gmail.com  | ConfirmEmail             | ConfirmEmail-error  | Email address does not match.   |

        Examples: Wrong password confirmation
        | value    | field    | confirmation      | confirmation_field   | error_type       | error_message                                 | 
        | password | Password | another password  | Password2            | Password2-error  | Password does not match, please check again.  |

        
        @correct_confirmation
        Scenario Outline: Correct entries are inserted for confirmation
            When the user enters <value> as <field>
            And the user enters <confirmation> as <confirmation_field>
            Then there is no <error_type> message

        Examples: Correct email confirmation
        | value                   | field  | confirmation             | confirmation_field       | error_type          |
        | andre.berto95@gmail.com | Email  | andre.berto95@gmail.com  | ConfirmEmail             | ConfirmEmail-error  |

        Examples: Correct password confirmation
        | value     | field     | confirmation  | confirmation_field   | error_type       |
        | password  | Password  | password      | Password2            | Password2-error  |

