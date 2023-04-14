# Created by svetlanalevinsohn at 2/25/23
Feature: Amazon Sign in tests

 Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens

 Scenario: Sign in page is visible for a few seconds
    Given Open Amazon page
    Then Verify Sign in Popup shown
    When Wait for 5 sec
    Then Verify Sign in popup shown
    Then Verify Sign in popup disappears