Feature: Run APIs
    Feature Description

    @101
    Scenario: Verify /api/user get API
       Given I initiated /api/user get API
       Then I validate /api/user get response

    @102
    Scenario: Verify /api/users post API
       Given I initiated /api/users post API
       Then I validate /api/users post response

    @103
    Scenario: Verify /api/users/2 put API
       Given I initiated /api/users/2 put API
       Then I validate /api/users/2 put response

    @104
    Scenario: Verify /api/users/2 delete API
       Given I initiated /api/users/2 delete API
       Then I validate /api/users/2 delete response