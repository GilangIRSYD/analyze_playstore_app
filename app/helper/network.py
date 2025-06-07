class BaseResponse:
    def __init__(self, code: int, message: str, data: dict = None):
        self.code = code
        self.message = message
        self.data = data or {}
        
    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "data": self.data
        }
        
def error_response(message: str, code: int = 500):
    return BaseResponse(
        code=code,
        message=message
    ).to_dict()
    
def success_response(data):
    return BaseResponse(
        code=200,
        message="success",
        data=data
    )