# restful-booker-test-cases
Test cases for Restful-Booker API 

# Test Scenarios
<!-- TEST_SCENARIOS_START -->

| Test Scenario Id   | API endpoint   | Description                                                         |
|:-------------------|:---------------|:--------------------------------------------------------------------|
| RB_TS_01           | /auth          | System accepts login attempts with valid credentials                |
| RB_TS_02           | /auth          | System rejects login attempts with invalid credentials              |
| RB_TS_03           | /auth          | System rejects login attempts with empty username                   |
| RB_TS_04           | /auth          | System rejects login attempts with empty password                   |
| RB_TS_05           | /auth          | System rejects login attempts with both username and password empty |
| RB_TS_06           | /booking       |                                                                     |

<!-- TEST_SCENARIOS_END -->

# Test Cases
<!-- TEST_CASES_START -->

| Test Case ID   | Summary                                                                                             | Preconditions                                      | Steps                                                                                                                     | Expected Result                                                                                                                  | Status   | Comments                                |
|:---------------|:----------------------------------------------------------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:----------------------------------------|
| RBAPI_001      | Auth / Generate an authorization token                                                              | Valid username and password for Restful-Booker API | 1. Send API Request to the /auth endpoint.<br/> In the request, provide the username and password from the preconditions. | 1. Response status is 200 OK.<br/>A token is generated.                                                                          | PASS     |                                         |
| RBAPI_002      | Auth / Verify that an authorization token cannot be generated when invalid credentials are provided |                                                    | 1. Send API Request to the /auth endpoint.</br>In the request, provide an invalid username and password.                  | ⚠️ Documentation update required.</br>👉 Rest API best practices</br> * Response status is 401 Unauthorized for an invalid token. | BLOCKED  | Currently, the response code is 200 OK. |

<!-- TEST_CASES_END -->
