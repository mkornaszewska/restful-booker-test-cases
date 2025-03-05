# restful-booker-test-cases
Test cases for Restful-Booker API 

# Test Scenarios
<!-- TEST_SCENARIOS_START -->

| Test Scenario Id   | API endpoint     | Description                                                         |
|:-------------------|:-----------------|:--------------------------------------------------------------------|
| RB_TS_01           | POST /auth       | System accepts login attempts with valid credentials                |
| RB_TS_02           | POST /auth       | System rejects login attempts with invalid credentials              |
| RB_TS_03           | POST /auth       | System rejects login attempts with empty username                   |
| RB_TS_04           | POST /auth       | System rejects login attempts with empty password                   |
| RB_TS_05           | POST /auth       | System rejects login attempts with both username and password empty |
| RB_TS_06           | GET /booking     | Filter by existing first name                                       |
| RB_TS_07           | GET /booking     | Filter by existing last name                                        |
| RB_TS_08           | GET /booking     | Filter by first and last names                                      |
| RB_TS_09           | GET /booking     | Filter by existing check in date                                    |
| RB_TS_10           | GET /booking     | Filter by existing check out date                                   |
| RB_TS_11           | GET /booking     | Filter by existing check in and check out dates                     |
| RB_TS_12           | GET /booking     | Filter by existing first name and check in date                     |
| RB_TS_13           | GET /booking     | Filter by existing first name and check out date                    |
| RB_TS_14           | GET /booking     | Filter by existing last name and check in date                      |
| RB_TS_15           | GET /booking     | Filter by existing last name and check out date                     |
| RB_TS_16           | GET /booking     | Filter by invalid first name                                        |
| RB_TS_17           | GET /booking     | Filter by invalid last name                                         |
| RB_TS_18           | GET /booking     | Filter by invalid check in date (string instead of date)            |
| RB_TS_19           | GET /booking     | Filter by invalid check out date (string instead of date)           |
| RB_TS_20           | GET /booking     | Filter by check in date with invalid date format                    |
| RB_TS_21           | GET /booking     | Filter by check out date with invalid date format                   |
| RB_TS_22           | GET /booking     | Read all bookings with no filters                                   |
| RB_TS_23           | GET /booking/:id | Read existing bookingId (JSON)                                      |
| RB_TS_24           | GET /booking/:id | Read existing bookingId (XML)                                       |
| RB_TS_25           | GET /booking/:id | Error for non-existing bookingId                                    |
| RB_TS_26           | POST booking     | Create valid booking (JSON)                                         |
| RB_TS_27           | POST booking     | Create valid booking (XML)                                          |
| RB_TS_28           | POST booking     | Error for booking without first name (JSON)                         |
| RB_TS_29           | POST booking     | Error for booking without last name (JSON)                          |
| RB_TS_30           | POST booking     | Error for booking without total price (JSON)                        |
| RB_TS_31           | POST booking     | Error for booking without deposit paid (JSON)                       |
| RB_TS_32           | POST booking     | Error for booking without check in date (JSON)                      |
| RB_TS_33           | POST booking     | Error for booking without check out date (JSON)                     |
| RB_TS_34           | POST booking     | Error for booking without additional needs (JSON)                   |
| RB_TS_35           | POST booking     | Error for booking without first name (XML)                          |
| RB_TS_36           | POST booking     | Error for booking without last name (XML)                           |
| RB_TS_37           | POST booking     | Error for booking without total price (XML)                         |
| RB_TS_38           | POST booking     | Error for booking without deposit paid (XML)                        |
| RB_TS_39           | POST booking     | Error for booking without check in date (XML)                       |
| RB_TS_40           | POST booking     | Error for booking without check out date (XML)                      |
| RB_TS_41           | POST booking     | Error for booking without additional needs (XML)                    |
| RB_TS_42           | POST booking     | Error for invalid first name (JSON)                                 |
| RB_TS_43           | POST booking     | Error for invalid last name (JSON)                                  |
| RB_TS_44           | POST booking     | Error for invalid total price (negative number) (JSON)              |
| RB_TS_45           | POST booking     | Error for invalid deposit paid (JSON)                               |
| RB_TS_46           | POST booking     | Error for invalid first name (JSON)                                 |
| RB_TS_47           | POST booking     | Error for invalid check in date (JSON)                              |
| RB_TS_48           | POST booking     | Error for invalid check out date (JSON)                             |
| RB_TS_49           | POST booking     | Error for invalid addtional needs (JSON)                            |
| RB_TS_50           | POST booking     | Error for invalid first name (XML)                                  |
| RB_TS_51           | POST booking     | Error for invalid last name (XML)                                   |
| RB_TS_52           | POST booking     | Error for invalid total price (negative number) (XML)               |
| RB_TS_53           | POST booking     | Error for invalid deposit paid (XML)                                |
| RB_TS_54           | POST booking     | Error for invalid first name (XML)                                  |
| RB_TS_55           | POST booking     | Error for invalid check in date (XML)                               |
| RB_TS_56           | POST booking     | Error for invalid check out date (XML)                              |
| RB_TS_57           | POST booking     | Error for invalid addtional needs (XML)                             |
| RB_TS_58           | POST booking     | Total price is a decimal (JSON)                                     |
| RB_TS_59           | POST booking     | Total price is a decimal (XML)                                      |
| RB_TS_60           | POST booking     | Error for invalid date format for check in date (JSON)              |
| RB_TS_61           | POST booking     | Error for invalid date format check out date (JSON)                 |

<!-- TEST_SCENARIOS_END -->

# Test Cases
<!-- TEST_CASES_START -->

| Test Case ID   | Summary                                                                                             | Preconditions                                      | Steps                                                                                                                     | Expected Result                                                                                                                  | Status   | Comments                                |
|:---------------|:----------------------------------------------------------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:----------------------------------------|
| RBAPI_001      | Auth / Generate an authorization token                                                              | Valid username and password for Restful-Booker API | 1. Send API Request to the /auth endpoint.<br/> In the request, provide the username and password from the preconditions. | 1. Response status is 200 OK.<br/>A token is generated.                                                                          | PASS     |                                         |
| RBAPI_002      | Auth / Verify that an authorization token cannot be generated when invalid credentials are provided |                                                    | 1. Send API Request to the /auth endpoint.</br>In the request, provide an invalid username and password.                  | ⚠️ Documentation update required.</br>👉 Rest API best practices</br> * Response status is 401 Unauthorized for an invalid token. | BLOCKED  | Currently, the response code is 200 OK. |

<!-- TEST_CASES_END -->
