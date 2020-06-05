# !python3
import array as a
import sys
import logging
import subprocess
import re


def sort_array(array, l_bracket='[', r_bracket=']', delimiter=', '):
    try:
        count = 0
        final_sort = ""
        combined_array = sorted(array)
        final_sort += l_bracket
        for x in combined_array:
            count += 1
            if count < len(combined_array):
                final_sort += (x + delimiter)
            else:
                final_sort += (x + r_bracket)
        return final_sort
    except ValueError:
        logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')


def import_params(param):
    concated_str = ''
    l_bracket = '['
    r_bracket = ']'
    delimiter = '\,'
    param = param.replace(" ", '')

    regex = re.compile(f'{delimiter}|\{l_bracket}|\{r_bracket}')
    concated_str = re.sub(regex, '', param)

    unsorted_arr = a.array('u', concated_str)
    final_str = (sort_array(unsorted_arr))
    # direct output to dev null to avoid command injection
    print(final_str) and subprocess.run('&>dev/null')
    return final_str


if __name__ == '__main__':
    # scrub and validate input
    try:
        if sys.argv[1] and sys.argv[2]:
            import_params(sys.argv[1] + sys.argv[2])
        else:
            print('you need 2 args')

    except IndexError:
        logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
