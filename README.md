# Etherscan-registration-form-testing

[Etherscan](https://etherscan.io/) is a block explorer and analytics platform that allows users to access details on any Ethereum blockchain transactions that are pending or confirmed. As in most websites, Etherscan has a page dedicated to a [registration form](https://etherscan.io/register) to allow new users to sign up on the platform.

The goal of this project is to:

- create test scenarios for the registration form on Etherscan website,
- create End-To-End (E2E) browser tests to cover all test scenarios, and
- justify the choice of the tools that have been used for the automatic testing.

## Test scenarios

Test scenarios (or test cases) are documents with steps to be completed as planned out ahead of time. The testing framework I have chosen to outline the test scenarios for this application is [Cucumber](https://cucumber.io/). Cucumber is well documented and it encourages collaboration among developers, quality assurance experts, and customer representatives in a software project through [Behavior-Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD).

<p align="center">
  <img src="https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/images/cucumber.png" width="400" height="110" />
</p>

Test scenarios are written in [Gherkin](https://cucumber.io/docs/gherkin/), a plain-text language with a simple structure. It is designed to be easy to learn by non-programmers, yet structured enough to allow concise description of test scenarios and examples to illustrate business rules in most real-world domains.

In a Cucumber project, test scenarios are contained in <em>feature</em> files, where they are described in descriptive language (like English). With regard to this task, I have created two separated feature files:

- [form_entries.feature](https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/features/form_entries.feature) contains the test scenarios to test the individual entries of the Etherscan registration form,
- [signup.feature](https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/features/signup.feature) contains the test scenarios to test actual action of registration from the user once the form has been properly filled.

Each scenario should test only one business rule and it usually contains multiple <em>steps</em>, each of which is linked to a Python expression (also called <em>step definition</em>) which is the code-equivalent of the step, and gets executed when Cucumber executes its associated Gherkin step in a scenario. All the step definitions for this task are contained in the [steps](https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/features/steps/steps.py) folder.

## End-to-end Browser Tests

The step definitions of this project had to reproduce the behavior of a user trying to sign up through the Etherscan registration form, which is a common <em>browser test</em>. The testing framework used for this task to enable E2E browser testing is [Selenium Webdrvier](https://www.selenium.dev/documentation/webdriver/). Selenium is amongst the most popular frameworks to test websites, it is open-source and also has good documentation.

To run a test, follow the next steps:

- Clone the current Git repository

```
git clone https://github.com/andreabertolini1995/Etherscan-registration-form-testing.git
```

- Be sure you have installed the packages listed in the [requirements](https://github.com/andreabertolini1995/Etherscan-registration-form-testing/blob/main/requirements.txt). [Behave](https://behave.readthedocs.io/en/stable/) is the Python implementation of the Cucumber framework:

```
behave==1.2.6
selenium==4.8.2
webdriver-manager==3.8.5
```

- Each test scenario is identified by an individual tag, so that it can be run independently from the others. Following, an example:

```
behave --tags==conditions_not_accepted
```

- Finally, the automated test doing its job:

https://user-images.githubusercontent.com/51784826/226219811-ca162d36-afcb-4933-852f-c24801c34da7.mp4
