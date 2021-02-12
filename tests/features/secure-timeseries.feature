Feature: Vermillion is able to handle secure timeseries datasets


        Scenario: Consumer publishes data with a valid token
	   
            Given Vermillion is running
            When The consumer publishes data with a valid token 
            Then The response status should be 201
	
        Scenario: Consumer publishes data with an invalid token 
		
	    Given Vermillion is running
            When The consumer publishes data with an invalid token
            Then The response status should be 403
	
	Scenario: Consumer publishes data with an empty token
    
	    Given Vermillion is running
            When The consumer publishes data with an empty token
            Then The response status should be 403
	
	Scenario: Consumer publishes data when body is null 
		
	    Given Vermillion is running
            When The consumer publishes data when body is null
            Then The response status should be 400

	Scenario: Consumer publishes data without a body
           
            Given Vermillion is running
            When The consumer publishes data without a body 
            Then The response status should be 400

	Scenario: Consumer publishes data with an invalid resource id
           
            Given Vermillion is running
            When The consumer publishes data with an invalid resource id
	    Then The response status should be 400
	
	Scenario: Consumer publishes data with an empty resource id
           
            Given Vermillion is running
            When The consumer publishes data with an empty resource id
            Then The response status should be 400

	Scenario: Authorised ID - single
		
	    Given Vermillion is running
            When The consumer requests for a standalone authorised ID 
	    Then The response status should be 200
	    And  The response should contain the secure timeseries data	
	
	Scenario: Authorised ID - multiple
	   
            Given Vermillion is running
            When The consumer requests for multiple authorised IDs
            Then The response status should be 200
	    And The response should contain the secure timeseries data

	Scenario: Unauthorised ID - single
            
            Given Vermillion is running
            When The consumer requests for an unauthorised ID
            Then The response status should be 403

        Scenario: Unauthorised ID - multiple
            
            Given Vermillion is running
            When The consumer requests for multiple unauthorised IDs
            Then The response status should be 403

        Scenario: Unauthorised ID - mixed
            
            Given Vermillion is running
            When The consumer requests for unauthorised IDs among authorised IDs
            Then The response status should be 403
