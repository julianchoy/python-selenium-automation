# Created by julian.choy at 4/15/23
Feature: Homework8

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias handmade
    When Input text pineapple
    When Click on search button
    Then Verify that text "pineapple" is shown

  Scenario: User can see deals when hovering over New Arrivals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify deals are visible
