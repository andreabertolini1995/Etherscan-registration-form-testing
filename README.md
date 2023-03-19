# Etherscan-registration-form-testing

[Etherscan](https://etherscan.io/) is a block explorer and analytics platform that allows users to access details on any Ethereum blockchain transactions that are pending or confirmed. As in most websites, Etherscan has a page dedicated to a [registration form](https://etherscan.io/register) to allow new users to sign up on the platform. 

The goal of this project is to create **test scenarios** for the registration form on Etherscan website, create **E2E browser tests** to cover all test scenarios and justify the choice of the tools that have been used for the automatic testing.


### Create test scenarios for the registration form on Etherscan website 
 
Test scenarios or test cases are a document with steps to be completed as planned out ahead of time. The testing framework I have chosen to outline the test scenarios for this application is [Cucumber](https://cucumber.io/). Cucumber is well documented and it encourages collaboration among developers, quality assurance experts, and customer representatives in a software project through [behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD).

![Cucumber](images/cucumber.png)

Test scenarios are written in [Gherkin](https://cucumber.io/docs/gherkin/), a plain-text language with a simple structure. It is designed to be easy to learn by non-programmers, yet structured enough to allow concise description of test scenarios and examples to illustrate business rules in most real-world domains. 

In a Cucumber project, test scenarios are contained in <em>feature<em> files, where they are described in descriptive language (like English). With regard to this task, I have created two separated feature files:
 * [form_entries.feature](https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/features/form_entries.feature) contains the test scenarios to test the individual entries of the Etherscan registration form
 * [signuo.feature](https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/features/signup.feature) contains the test scenarios to test actual action of registration from the user once the form has been properly filled. 





