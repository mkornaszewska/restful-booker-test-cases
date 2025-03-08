# restful-booker-test-cases
Test cases for Restful-Booker API 

# Test Scenarios
<!-- TEST_SCENARIOS_START -->

| Test Scenario Id   | Priority   | API endpoint        | Description                                                                                                  |
|:-------------------|:-----------|:--------------------|:-------------------------------------------------------------------------------------------------------------|
| RB_TS_01           | P0         | POST /auth          | System accepts login attempts with valid credentials                                                         |
| RB_TS_02           | P0         | POST /auth          | System rejects login attempts with invalid credentials                                                       |
| RB_TS_03           | P0         | POST /auth          | System rejects login attempts with empty username                                                            |
| RB_TS_04           | P0         | POST /auth          | System rejects login attempts with empty password                                                            |
| RB_TS_05           | P0         | POST /auth          | System rejects login attempts with both username and password empty                                          |
| RB_TS_06           | P2         | GET /booking        | Filter by existing first name                                                                                |
| RB_TS_07           | P2         | GET /booking        | Filter by existing last name                                                                                 |
| RB_TS_08           | P2         | GET /booking        | Filter by first and last names                                                                               |
| RB_TS_09           | P2         | GET /booking        | Filter by existing check in date                                                                             |
| RB_TS_10           | P2         | GET /booking        | Filter by existing check out date                                                                            |
| RB_TS_11           | P2         | GET /booking        | Filter by existing check in and check out dates                                                              |
| RB_TS_12           | P2         | GET /booking        | Filter by existing first name and check in date                                                              |
| RB_TS_13           | P2         | GET /booking        | Filter by existing first name and check out date                                                             |
| RB_TS_14           | P2         | GET /booking        | Filter by existing last name and check in date                                                               |
| RB_TS_15           | P2         | GET /booking        | Filter by existing last name and check out date                                                              |
| RB_TS_16           | P2         | GET /booking        | Filter by invalid first name                                                                                 |
| RB_TS_17           | P2         | GET /booking        | Filter by invalid last name                                                                                  |
| RB_TS_18           | P2         | GET /booking        | Filter by invalid check in date (string instead of date)                                                     |
| RB_TS_19           | P2         | GET /booking        | Filter by invalid check out date (string instead of date)                                                    |
| RB_TS_20           | P2         | GET /booking        | Filter by check in date with invalid date format                                                             |
| RB_TS_21           | P2         | GET /booking        | Filter by check out date with invalid date format                                                            |
| RB_TS_22           | P0         | GET /booking        | Read all bookings with no filters                                                                            |
| RB_TS_23           | P0         | GET /booking/:id    | Read existing bookingId (JSON / XML)                                                                         |
| RB_TS_24           | P0         | GET /booking/:id    | Error for non-existing bookingId (JSON/XML)                                                                  |
| RB_TS_25           | P0         | GET /booking/:id    | Error for no bookingId (JSON/XML)                                                                            |
| RB_TS_26           | P0         | POST /booking       | Create valid booking (JSON / XML)                                                                            |
| RB_TS_27           | P1         | POST /booking       | Error for booking without first name (JSON / XML)                                                            |
| RB_TS_28           | P1         | POST /booking       | Error for booking without last name (JSON / XML)                                                             |
| RB_TS_29           | P2         | POST /booking       | Error for booking without total price (JSON / XML)                                                           |
| RB_TS_30           | P1         | POST /booking       | Error for booking without deposit paid (JSON / XML)                                                          |
| RB_TS_31           | P1         | POST /booking       | Error for booking without check in date (JSON / XML)                                                         |
| RB_TS_32           | P1         | POST /booking       | Error for booking without check out date (JSON / XML)                                                        |
| RB_TS_33           | P3         | POST /booking       | Error for booking without additional needs (JSON / XML)                                                      |
| RB_TS_34           | P1         | POST /booking       | Error for invalid first name (data type other than string) (JSON / XML)                                      |
| RB_TS_35           | P1         | POST /booking       | Error for invalid last name (data type other than string) (JSON / XML)                                       |
| RB_TS_36           | P2         | POST /booking       | Error for invalid total price (negative integer) (JSON / XML)                                                |
| RB_TS_37           | P2         | POST /booking       | Error for invalid deposit paid (data type other than boolean) (JSON / XML)                                   |
| RB_TS_38           | P1         | POST /booking       | Error for invalid check in date (data type other than date) (JSON / XML)                                     |
| RB_TS_39           | P1         | POST /booking       | Error for invalid check out date (data type other than date) (JSON / XML)                                    |
| RB_TS_40           | P3         | POST /booking       | Error for invalid addtional needs (data type other than string) (JSON / XML)                                 |
| RB_TS_41           | P1         | POST /booking       | Total price is a decimal (JSON / XML)                                                                        |
| RB_TS_42           | P1         | POST /booking       | Error for invalid date format for check in date (JSON / XML)                                                 |
| RB_TS_43           | P1         | POST /booking       | Error for invalid date format check out date (JSON / XML)                                                    |
| RB_TS_44           | P0         | PUT /booking/:id    | Update booking with valid cookie (JSON / XML)                                                                |
| RB_TS_45           | P0         | PUT /booking/:id    | Update booking with valid authorization token (JSON / XML)                                                   |
| RB_TS_46           | P0         | PUT /booking/:id    | Error for update booking with invalid cookie (JSON / XML)                                                    |
| RB_TS_47           | P0         | PUT /booking/:id    | Error for update booking with invalid authorization token (JSON / XML)                                       |
| RB_TS_48           | P0         | PUT /booking/:id    | Error for update booking with no cookie (JSON / XML)                                                         |
| RB_TS_49           | P0         | PUT /booking/:id    | Error for update booking with no authorization token (JSON / XML)                                            |
| RB_TS_50           | P2         | PUT /booking/:id    | Error for update booking for non-existing bookingId (JSON / XML)                                             |
| RB_TS_51           | P2         | PUT /booking/:id    | Error for update booking without first name (JSON / XML)                                                     |
| RB_TS_52           | P2         | PUT /booking/:id    | Error for update booking without last name (JSON / XML)                                                      |
| RB_TS_53           | P2         | PUT /booking/:id    | Error for update booking without total price (JSON / XML)                                                    |
| RB_TS_54           | P2         | PUT /booking/:id    | Error for update booking without deposit paid (JSON / XML)                                                   |
| RB_TS_55           | P1         | PUT /booking/:id    | Error for update booking without check in date (JSON / XML)                                                  |
| RB_TS_56           | P1         | PUT /booking/:id    | Error for update booking without check out date (JSON / XML)                                                 |
| RB_TS_57           | P3         | PUT /booking/:id    | Error for update booking without additional needs (JSON / XML)                                               |
| RB_TS_58           | P2         | PUT /booking/:id    | Error for update booking with invalid first name (data type other than string) (JSON / XML)                  |
| RB_TS_59           | P2         | PUT /booking/:id    | Error for update booking with invalid last name (data type other than string) (JSON / XML)                   |
| RB_TS_60           | P2         | PUT /booking/:id    | Error for update booking with invalid total price (negative integer) (JSON / XML)                            |
| RB_TS_61           | P2         | PUT /booking/:id    | Error for update booking with invalid deposit paid (data type other than boolean) (JSON / XML)               |
| RB_TS_62           | P1         | PUT /booking/:id    | Error for update booking with invalid check in date (data type other than date) (JSON / XML)                 |
| RB_TS_63           | P1         | PUT /booking/:id    | Error for update booking with invalid check out date (data type other than date) (JSON / XML)                |
| RB_TS_64           | P3         | PUT /booking/:id    | Error for update booking with invalid additional needs (data type other than string) (JSON / XML)            |
| RB_TS_65           | P1         | PUT /booking/:id    | Error for update booking with invalid date format for check in date (JSON / XML)                             |
| RB_TS_66           | P1         | PUT /booking/:id    | Error for update booking with invalid date format for check out date (JSON / XML)                            |
| RB_TS_67           | P2         | PUT /booking/:id    | Update booking when total price is a decimal (JSON / XML)                                                    |
| RB_TS_68           | P1         | PUT /booking/:id    | Error for update booking with no bookingId (JSON / XML)                                                      |
| RB_TS_69           | P0         | PATCH /booking/:id  | Partial update booking with valid cookie (JSON / XML)                                                        |
| RB_TS_70           | P0         | PATCH /booking/:id  | Partial update booking with valid authorization token (JSON / XML)                                           |
| RB_TS_71           | P0         | PATCH /booking/:id  | Error for partial update booking with invalid cookie (JSON / XML)                                            |
| RB_TS_72           | P0         | PATCH /booking/:id  | Error for partial update booking with invalid authorization token (JSON / XML)                               |
| RB_TS_73           | P0         | PATCH /booking/:id  | Error for partial update booking with no cookie (JSON / XML)                                                 |
| RB_TS_74           | P0         | PATCH /booking/:id  | Error for partial update booking with no authorization token (JSON / XML)                                    |
| RB_TS_75           | P2         | PATCH /booking/:id  | Error for partial update booking for non-existing bookingId (JSON / XML)                                     |
| RB_TS_76           | P1         | PATCH /booking/:id  | Valid partial update for first name (JSON / XML)                                                             |
| RB_TS_77           | P1         | PATCH /booking/:id  | Valid partial update for last name (JSON / XML)                                                              |
| RB_TS_78           | P1         | PATCH /booking/:id  | Valid partial update for total price (JSON / XML)                                                            |
| RB_TS_79           | P1         | PATCH /booking/:id  | Valid partial update for deposit paid (JSON / XML)                                                           |
| RB_TS_80           | P1         | PATCH /booking/:id  | Valid partial update for check in date (JSON / XML)                                                          |
| RB_TS_81           | P1         | PATCH /booking/:id  | Valid partial update for check out date (JSON / XML)                                                         |
| RB_TS_82           | P3         | PATCH /booking/:id  | Valid partial update for additional needs (JSON / XML)                                                       |
| RB_TS_83           | P2         | PATCH /booking/:id  | Error for partial update booking with invalid first name (data type other than string) (JSON / XML)          |
| RB_TS_84           | P2         | PATCH /booking/:id  | Error for partial update booking with invalid last name (data type other than string) (JSON / XML)           |
| RB_TS_85           | P2         | PATCH /booking/:id  | Error for partial update booking with invalid total price (negative integer) (JSON / XML)                    |
| RB_TS_86           | P2         | PATCH /booking/:id  | Error for partial update booking with invalid deposit paid (data type other than boolean) (JSON / XML)       |
| RB_TS_87           | P1         | PATCH /booking/:id  | Error for partial update partial booking with invalid check in date (data type other than date) (JSON / XML) |
| RB_TS_88           | P1         | PATCH /booking/:id  | Error for partial update booking with invalid check out date (data type other than date) (JSON / XML)        |
| RB_TS_89           | P3         | PATCH /booking/:id  | Error for partial update booking with invalid additional needs (data type other than string) (JSON / XML)    |
| RB_TS_90           | P1         | PATCH /booking/:id  | Error for partial update booking with invalid date format for check in date (JSON / XML)                     |
| RB_TS_91           | P1         | PATCH /booking/:id  | Error for partial update booking with invalid date format for check out date (JSON / XML)                    |
| RB_TS_92           | P2         | PATCH /booking/:id  | Valid partial update booking when total price is a decimal (JSON / XML)                                      |
| RB_TS_93           | P1         | PATCH /booking/:id  | Error for partial update booking for non-existing bookingId (JSON / XML)                                     |
| RB_TS_94           | P1         | PATCH /booking/:id  | Error for partial update booking with no bookingId (JSON / XML)                                              |
| RB_TS_95           | P0         | DELETE /booking/:id | Delete booking with valid cookie (JSON / XML)                                                                |
| RB_TS_96           | P0         | DELETE /booking/:id | Delete booking with valid authorization token (JSON / XML)                                                   |
| RB_TS_97           | P0         | DELETE /booking/:id | Error for delete booking with invalid cookie (JSON / XML)                                                    |
| RB_TS_98           | P0         | DELETE /booking/:id | Error for delete booking with invalid authorization token (JSON / XML)                                       |
| RB_TS_99           | P0         | DELETE /booking/:id | Error for delete booking with no cookie (JSON / XML)                                                         |
| RB_TS_100          | P0         | DELETE /booking/:id | Error for delete booking with no authorization token (JSON / XML)                                            |
| RB_TS_101          | P0         | DELETE /booking/:id | Error for delete booking for non-existing bookingId (JSON / XML)                                             |
| RB_TS_102          | P0         | DELETE /booking/:id | Error for delete booking with no bookingId (JSON / XML)                                                      |
| RB_TS_103          | P0         | GET /ping           | Read health check                                                                                            |

<!-- TEST_SCENARIOS_END -->

# Test Cases


| Test Case ID   | Summary                                                                                             | Preconditions                                      | Steps                                                                                                                     | Expected Result                                                                                                                  | Status   | Comments                                |
|:---------------|:----------------------------------------------------------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:---------|:----------------------------------------|
| RBAPI_001      | Auth / Generate an authorization token                                                              | Valid username and password for Restful-Booker API | 1. Send API Request to the /auth endpoint.<br/> In the request, provide the username and password from the preconditions. | 1. Response status is 200 OK.<br/>A token is generated.                                                                          | PASS     |                                         |
| RBAPI_002      | Auth / Verify that an authorization token cannot be generated when invalid credentials are provided |                                                    | 1. Send API Request to the /auth endpoint.</br>In the request, provide an invalid username and password.                  | ⚠️ Documentation update required.</br>👉 Rest API best practices</br> * Response status is 401 Unauthorized for an invalid token. | BLOCKED  | Currently, the response code is 200 OK. |


