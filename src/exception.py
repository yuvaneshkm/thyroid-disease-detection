# Importing necessary libraries:
import sys
import warnings

warnings.filterwarnings("ignore")


# Creating a class to handle custom exception:
class CustomException(Exception):

    def __init__(self, error_message):

        _, _, exc_tb = sys.exc_info()

        filename = exc_tb.tb_frame.f_code.co_filename
        linenumber = exc_tb.tb_lineno
        errormessage = str(error_message)

        self.messsage = f"Error occured in Python script name: [{filename}], line number: [{linenumber}] and error message: [{errormessage}]"

    def __str__(self) -> str:
        return self.messsage


if __name__ == "__main__":
    try:
        9 / 0
    except Exception as ex:
        raise CustomException(ex)
