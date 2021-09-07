def sed(file_input, file_output, pattern_string, replacement_string):
    try:
        with open(file_input) as f_in:
            with open(file_output, 'w') as f_out:
                for line in f_in:
                    f_out.write(line.replace(pattern_string, replacement_string))
    except Exception as err:
        print(err)


sed("text.txt", "resault.txt", "are", "is")
