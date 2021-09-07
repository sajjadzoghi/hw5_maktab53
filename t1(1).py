from io import UnsupportedOperation


def sed(file_input, file_output, pattern_string, replacement_string):
    try:
        f_in = open(file_input)
    except FileNotFoundError:
        print(f'Sorry! File "{file_input} is not found."')
    except UnsupportedOperation:
        print(f'Sorry! File "{file_input} is not readable."')
    else:
        with f_in:
            try:
                f_out = open(file_output, 'w')
            except FileNotFoundError:
                print(f'Sorry! File "{file_output} is not found."')
            else:
                try:
                    with f_out:
                        for line in f_in:
                            f_out.write(line.replace(pattern_string, replacement_string))
                except UnsupportedOperation:
                    print(f'Sorry! File "{file_output} is not writable."')


sed("te.txt", "resault.txt", "are", "is")
