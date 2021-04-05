from Tools import getListFromFile
from v1 import proceed_arguments
from Console import *

if __name__ == '__main__':
    data = getListFromFile()
    request = ''
    while True:
        try:
            request = get_string('Enter search query', default=request if len(request) != 0 else 'exit')
            if request == 'exit':
                break
            print(proceed_arguments(request, data))
        except Exception as err:
            print(err)
        finally:
            print()
