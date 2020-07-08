Feature: word check
  Scenario: check letters
    Given I have a letter
    When I input letter y
    Then inputed letter is equal with 'y'