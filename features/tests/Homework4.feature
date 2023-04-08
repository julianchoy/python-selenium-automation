# Created by julian.choy at 4/8/23
Feature: Verify link on Amazon Best Sellers page

  Scenario: User can see text on Amazon
    Given Open Amazon Best Sellers page
    Then Verify that Best Sellers tab has 5 links

    Scenario: User can add item to cart
      Given Open Amazon page
      When Input text pineapple
      When Click on search button
      And Click on first product
      And Click on Add to Cart
     Then Verify that cart has 1 item