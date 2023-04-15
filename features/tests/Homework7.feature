# Created by julian.choy at 4/14/23
Feature: Homework7

  Scenario: Logged out user sees Sign in page when clicking Orders
   Given Open Amazon page
   When Click Amazon Orders link
   Then Verify Sign In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
   Given Open Amazon page
   When Click on cart icon
   Then Verify Your Amazon Cart is empty text present

  Scenario: User can add item to cart
    Given Open Amazon page
    When Input text pineapple
    When Click on search button
    And Click on first product
    And Click on Add to Cart
    Then Verify that cart has 1 item