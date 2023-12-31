import sys
import logging
import 
def get_exception_details(error,errors_details:sys):
    _,_,exc_tb = errors_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomeException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = get_exception_details(error_message,errors_details=error_details)
    
    def __str__(self):
        return self.error_message
    



# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomeException(e,sys)