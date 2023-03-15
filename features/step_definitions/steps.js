const { Given, When, Then } = require("@cucumber/cucumber");

Given(
  "a user with username {word} and password {word}",
  function (username, password) {
    return "pending";
  }
);

When("the user tries to register on Etherscan", function () {
  return "pending";
});

Then("the user should be forbidden to register", function () {
  return "pending";
});
