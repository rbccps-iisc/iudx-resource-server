Feature: Vermillion is able to handle geospatial queries

        Scenario: Geo-spatial query with empty body
                Given Vermillion is running
                When The geospatial query body is empty
                Then The response status should be 400

        Scenario: Geo-spatial query with invalid resource id
                Given Vermillion is running
                When The geospatial query resource id is invalid
                Then The response status should be 400

        Scenario: Geo-spatial query with empty resource id
                Given Vermillion is running
                When The geospatial query resource id is empty
                Then The response status should be 400

        Scenario: Geo-spatial query for invalid body
                Given Vermillion is running
                When The geospatial query body is invalid
                Then The response status should be 400
	
	Scenario: Geo-spatial query with just resource id as payload
                Given Vermillion is running
                When The geospatial query has only resource id
                Then The response status should be 400


        Scenario: Geo-spatial query for invalid coordinates
                Given Vermillion is running
                When The geospatial query coordinates are invalid
                Then The response status should be 400

        Scenario: Geo-spatial query for empty coordinates
                Given Vermillion is running
                When The geospatial query coordinates are empty
                Then The response status should be 400
	
	Scenario: Geo-spatial query for coordinates not present
                Given Vermillion is running
                When The geospatial query coordinates are not present
                Then The response status should be 400

	Scenario: Geo-spatial query for distance not present
                Given Vermillion is running
                When The geospatial query distance is not present
                Then The response status should be 400


	Scenario: Geo-spatial query for invalid distance
                Given Vermillion is running
                When The geospatial query distance is invalid
                Then The response status should be 400

        Scenario: Geo-spatial query for empty distance
                Given Vermillion is running
                When The geospatial query distance is empty
                Then The response status should be 400

        Scenario: Geo-spatial query for distance in cm
                Given Vermillion is running
                When A geo-spatial query with distance in cm
                Then The response status should be 400

        Scenario: Geo-spatial query for distance in mm
                Given Vermillion is running
                When A geo-spatial query with distance in mm
                Then The response status should be 400

        Scenario: Geo-spatial query for distance in km
                Given Vermillion is running
                When A geo-spatial query with distance in km
                Then The response status should be 400
        Scenario: Geo-spatial query
                Given Vermillion is running
                When A geo-spatial query is initiated
                Then All matching records are returned














