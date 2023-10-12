def main():
    """
    This function will take input from the user, a date in the format mm/dd/yyyy. Then, it will
    split a list of months and print the output in a different format, calling individual
    parts of the list so that whatever number month the user inputs, that it the corresponding
    month.
    """
    date_string = input('Enter a date in the format mm/dd/yyyy: ')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    date_list = date_string.split('/')
    print(months[int(date_list[0])-1] + " " + date_list[1] + ", " + date_list[2])

# Call the main function.
if __name__ == '__main__':
    main()
