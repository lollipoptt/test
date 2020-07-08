Feature: UI testing
  Scenario: login SHDR
    Given open SHDR website URL
    When input username and passward and click login
    Then it can login successfully