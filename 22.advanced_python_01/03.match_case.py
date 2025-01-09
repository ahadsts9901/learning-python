def http_status(status) -> str:
    match status:
        case 200:
            return "success"
        case 404:
            return "not found"
        case 401:
            return "unauthorized"
        case 403:
            return "forbidden"
        case 500:
            return "server error"
        case _:
            return "hello world"
        
    

print(http_status(200))
print(http_status(404))
print(http_status(500))