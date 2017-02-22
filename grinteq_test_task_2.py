def third_miss_range(end, *args):
    if len(args) == 0:
        start, end, step = 0, end, 1
    elif len(args) == 1:
        start, end, step = 0, end, args[0]
    elif len(args) == 2:
        start, end, step = end, args[0], args[1]
    else:
        raise Exception('Expected at most 3 arguments, got {0}'.format(len(args)+1))

    if end > start and step > 0:
        cond = 'start < end'
    elif end < start and step < 0:
        cond = 'start > end'
    else:
        raise Exception('Wrong arguments')

    count = 0
    while eval(cond):
        count += 1
        if not count % 3 == 0:
            yield start
        start += step


for a in third_miss_range(14, 3, -2):
   print(a)