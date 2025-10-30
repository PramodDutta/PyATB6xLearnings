def validate_status_code(response_code):
    if response_code > 0:
        if response_code == 200:
            print("Request is success")
        else:
            print("Error is the request")
    else:
        print("Error in the response code value.")

validate_status_code(404)
validate_status_code(200)
validate_status_code(response_code=200)
validate_status_code(input("Enter your status code"))