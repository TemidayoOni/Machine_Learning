import sys
from src.logger import logging

# function to collect error details

def get_error_message(error, error_details:sys):

    _,_,exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in script [{0}] line number [{1}] error message [{2}]".format(

    file_name, exc_tb.tb_lineno, str(error))

    return error_message


# custom exception class 

class CustomException(Exception):

    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)

        self.error_message = get_error_message(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message

    