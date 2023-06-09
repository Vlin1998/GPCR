def read_errors():
    with open('./result.txt') as f:
        errors = (line for line in f.readlines())
    return errors


def analysize_errors(errors):
    count = [0, 0, 0]
    for error_msg in errors:
        if error_msg.count(',') != 0:
            r = analysize_line(error_msg)
            for i in range(len(r)):
                if not r[i]:
                    count[i] += 1
    return count


def analysize_line(line):
    result = []
    right, err = line.split(',')
    right_family = analysize_right(right)
    err_family = analysize_err(err)
    for i in range(3):
        if right_family[i] != err_family[i]:
            result.append(False)
        else:
            result.append(True)
    return result


def analysize_right(right_line):
    right_line = right_line[3:]
    family, sub1_family, sub2_family, *_ = right_line.split('_')
    return family, sub1_family, sub2_family


def analysize_err(err_line):
    err_line = err_line[3:]
    family, sub1_family, sub2_family, *_ = err_line.split('_')
    return family, sub1_family, sub2_family

def main(test_num):
    errors = read_errors()
    counts = analysize_errors(errors)
    with open('./result.txt', 'a') as f:
        print("family level:        ", 1-counts[0]/test_num, file=f)
        print("subfamily level:     ", 1-counts[1]/test_num, file=f)
        print("sub-subfamily level: ", 1-counts[2]/test_num, file=f)
