# Created by julian.choy at 4/8/23
Feature: Homework 3

  Scenario: User can see Sign in when clicking on Returns and Orders
    Given Open Amazon Page
    When Click on Orders
    Then Verify Sign In is visible
    And Verify Email input field is present

  Scenario: User can see Amazon cart is empty
      Given Open Amazon Page
      When Click on Amazon Cart
      Then Verify Cart is empty