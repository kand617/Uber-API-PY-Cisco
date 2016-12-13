#Getting started

## How to Build


You must have Python 2 >=2.7.9 or Python 3 >=3.4 installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Uber%20API-Python)


## How to Use

The following section explains how to use the UberAPI SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Uber%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Uber%20API-Python&projectName=uberapilib)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Uber%20API-Python&projectName=uberapilib)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=createFile&workspaceFolder=Uber%20API-Python&projectName=uberapilib)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from uberapilib.uber_api_client import *
```

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Uber%20API-Python&libraryName=uberapilib.uber_api_client&projectName=uberapilib)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=Uber%20API-Python&libraryName=uberapilib.uber_api_client&projectName=uberapilib)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'pip install -r test-requirements.txt'
  3. Invoke 'nosetests'

## Initialization

### Authentication and 
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password | The password to use with basic authentication |



API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = "basic_auth_user_name" # The username to use with basic authentication
basic_auth_password = "basic_auth_password" # The password to use with basic authentication

client = UberAPIClient(basic_auth_user_name, basic_auth_password)
```

## Class Reference

### <a name="list_of_controllers"></a>List of Controllers

* [APIController](#api_controller)

### <a name="api_controller"></a>![Class: ](http://apidocs.io/img/class.png ".APIController") APIController

#### Get controller instance

An instance of the ``` APIController ``` class can be accessed from the API Client.

```python
 client_client = client.client
```

#### <a name="get_request_map"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_request_map") get_request_map

> Get a map with a visual representation of a Request.

```python
def get_request_map(self,
                        request_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| requestId |  ``` Required ```  | Unique identifier representing a Request. |



#### Example Usage

```python
request_id = 'request_id'

result = client_client.get_request_map(request_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues |
| 404 | Not found |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types, such as ?Unacceptable content type. Request resource as: application/json. |
| 409 | A conflict needs to be resolved before the request can be made. |
| 422 | Invalid request. The request body is parse-able however with invalid content or there are issues with a rider's user account. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="delete_request_cancel"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.delete_request_cancel") delete_request_cancel

> Cancel an ongoing Request on behalf of a rider.

```python
def delete_request_cancel(self,
                              request_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| requestId |  ``` Required ```  | Unique identifier representing a Request. |



#### Example Usage

```python
request_id = 'request_id'

client_client.delete_request_cancel(request_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types, such as ?Unacceptable content type. Request resource as: application/json. |
| 409 | A conflict needs to be resolved before the request can be made |
| 422 | Invalid request. The request body is parse-able however with invalid content or there are issues with a rider's user account. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error |




#### <a name="get_request_details"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_request_details") get_request_details

> Get the real time status of an ongoing trip that was created using the Ride Request endpoint.

```python
def get_request_details(self,
                            request_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| requestId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
request_id = 'request_id'

result = client_client.get_request_details(request_id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types, such as ?Unacceptable content type. Request resource as: application/json. |
| 409 | A conflict needs to be resolved before the request can be made. |
| 422 | Invalid request. The request body is parse-able however with invalid content or there are issues with a rider's user account. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error |




#### <a name="get_user_profile"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_user_profile") get_user_profile

> The User Profile endpoint returns information about the Uber user that has authorized with the application.

```python
def get_user_profile(self)
```

#### Example Usage

```python

result = client_client.get_user_profile()

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types: ?Unacceptable content type. Request resource as: application/json, etc. |
| 422 | Invalid request. The request body is parse-able however with invalid content. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="get_products_types"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_products_types") get_products_types

> The Products endpoint returns information about the Uber products offered at a given location. The response includes the display name and other details about each product, and lists the products in the proper display order.

```python
def get_products_types(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| latitude |  ``` Required ```  | Latitude component of location. |
| longitude |  ``` Required ```  | Longitude component of location. |



#### Example Usage

```python
collect = {}

latitude = 174.523294898459
collect['latitude'] = latitude

longitude = 174.523294898459
collect['longitude'] = longitude


result = client_client.get_products_types(collect)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types: ?Unacceptable content type. Request resource as: application/json, etc. |
| 422 | Invalid request. The request body is parse-able however with invalid content. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="get_price_estimates"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_price_estimates") get_price_estimates

> The Price Estimates endpoint returns an estimated price range for each product offered at a given location. The price estimate is provided as a formatted string with the full price range and the localized currency symbol.

```python
def get_price_estimates(self,
                            options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| endLatitude |  ``` Required ```  | Latitude component of end location. |
| endLongitude |  ``` Required ```  | Longitude component of end location. |
| startLatitude |  ``` Required ```  | Latitude component of start location. |
| startLongitude |  ``` Required ```  | Longitude component of start location. |



#### Example Usage

```python
collect = {}

end_latitude = 174.523294898459
collect['end_latitude'] = end_latitude

end_longitude = 174.523294898459
collect['end_longitude'] = end_longitude

start_latitude = 174.523294898459
collect['start_latitude'] = start_latitude

start_longitude = 174.523294898459
collect['start_longitude'] = start_longitude


result = client_client.get_price_estimates(collect)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types: ?Unacceptable content type. Request resource as: application/json, etc. |
| 422 | Invalid request. The request body is parse-able however with invalid content. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="get_time_estimates"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_time_estimates") get_time_estimates

> The Time Estimates endpoint returns ETAs for all products offered at a given location, with the responses expressed as integers in seconds. We recommend that this endpoint be called every minute to provide the most accurate, up-to-date ETAs.

```python
def get_time_estimates(self,
                           options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| startLatitude |  ``` Required ```  | Latitude component of the start location |
| startLongitude |  ``` Required ```  | Longitude component of the start location |
| customerUuid |  ``` Optional ```  | The customer id interested in estimate |
| productId |  ``` Optional ```  | Id of the requested product |



#### Example Usage

```python
collect = {}

start_latitude = 174.523294898459
collect['start_latitude'] = start_latitude

start_longitude = 174.523294898459
collect['start_longitude'] = start_longitude

customer_uuid = 'customer_uuid'
collect['customer_uuid'] = customer_uuid

product_id = 'product_id'
collect['product_id'] = product_id


result = client_client.get_time_estimates(collect)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types: ?Unacceptable content type. Request resource as: application/json, etc. |
| 422 | Invalid request. The request body is parse-able however with invalid content. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="get_user_activity_v_1_1"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_user_activity_v_1_1") get_user_activity_v_1_1

> The User Activity endpoint returns data about a user's lifetime activity with Uber. The response will include pickup locations and times, dropoff locations and times, the distance of past requests, and information about which products were requested.

```python
def get_user_activity_v_1_1(self,
                                options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| limit |  ``` Required ```  | Number of items to return for pagging |
| offset |  ``` Required ```  | Page offset for pagging |



#### Example Usage

```python
collect = {}

limit = 174
collect['limit'] = limit

offset = 174
collect['offset'] = offset


result = client_client.get_user_activity_v_1_1(collect)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types: ?Unacceptable content type. Request resource as: application/json, etc. |
| 422 | Invalid request. The request body is parse-able however with invalid content. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="get_promotions"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_promotions") get_promotions

> The Promotions endpoint returns information about the promotion that will be available to a new user based on their activity's location. These promotions do not apply for existing users.

```python
def get_promotions(self,
                       options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| endLatitude |  ``` Required ```  | Latitude component of end location. |
| endLongitude |  ``` Required ```  | Longitude component of end location. |
| startLatitude |  ``` Required ```  | Latitude component of start location. |
| startLongitude |  ``` Required ```  | Longitude component of start location |



#### Example Usage

```python
collect = {}

end_latitude = 174.523294898459
collect['end_latitude'] = end_latitude

end_longitude = 174.523294898459
collect['end_longitude'] = end_longitude

start_latitude = 174.523294898459
collect['start_latitude'] = start_latitude

start_longitude = 174.523294898459
collect['start_longitude'] = start_longitude


result = client_client.get_promotions(collect)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request. |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found. |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types, such as ?Unacceptable content type. Request resource as: application/json. |
| 409 | A conflict needs to be resolved before the request can be made. |
| 422 | Invalid request. The request body is parse-able however with invalid content or there are issues with a rider's user account. |
| 429 | Too Many Requests. Rate limited |
| 500 | Internal Server Error. |
| 222 | bac |




#### <a name="create_request"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.create_request") create_request

> The Request endpoint allows a ride to be requested on behalf of an Uber user given their desired product, start, and end locations. Please review the Sandbox documentation on how to develop and test against these endpoints without making real-world Requests and being charged.

```python
def create_request(self,
                       body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = RequestBody()

result = client_client.create_request(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Malformed request |
| 401 | Unauthorized the request requires user authentication (not logged in). |
| 403 | Forbidden. Also used for unauthorized requests such as improper OAuth 2.0 scopes or permissions issues. |
| 404 | Not found |
| 406 | Unacceptable content type. Client sent an accepts header for a content type which does not exist on the server. Body includes a list of acceptable content types, such as ?Unacceptable content type. Request resource as: application/json |
| 409 | A conflict needs to be resolved before the request can be made. |
| 422 | Invalid request. The request body is parse-able however with invalid content or there are issues with a rider's user account. |
| 429 | Too Many Requests. Rate limited. |
| 500 | Internal Server Error. |




#### <a name="get_product_detail_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".APIController.get_product_detail_by_id") get_product_detail_by_id

> Get product details w.r.t id

```python
def get_product_detail_by_id(self,
                                 product_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| productId |  ``` Required ```  | Unique identifier representing a specific product for a given latitude & longitude. For example, uberX in San Francisco will have a different product_id than uberX in Los Angeles. |



#### Example Usage

```python
product_id = 'product_id'

result = client_client.get_product_detail_by_id(product_id)

```


[Back to List of Controllers](#list_of_controllers)



