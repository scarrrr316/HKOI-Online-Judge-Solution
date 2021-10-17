while True:
    try:
        for _ in input()+'\n':
            if (_.isalpha() and not _.isdigit()) or _.isspace():
                print(_,end='')
    except EOFError:
        break