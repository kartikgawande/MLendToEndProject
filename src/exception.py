import sys,logger
log = logger.logging

def error_msg_details(error_msg, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg ='''
    Error occured in Python Script named:
    [{0}]
    Line number [{1}]
    Error message [{2}]
    '''.format(
        file_name,
        exc_tb.tb_lineno,
        str(error_msg)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=error_msg_details(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg

if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        log.info(e)
        raise CustomException(e,sys)