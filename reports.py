
def count_games(file_name):
    f = open(file_name, "r")
    data_list = []
    for i in f.readlines():
        content = i.strip().split("\t")
        data_list.append(str(content[0]))
        result = len(data_list)
    return result


def decide(file_name, year):
    f = open(file_name, "r")
    data_list = []
    for row in f.readlines():
        file_row = row.strip().split("\t")
        data_list.append(file_row)
    f.close()
    for i in range(len(data_list)):
        if data_list[i][2] == year:
            return False
    return True


def get_latest(file_name):
    f = open(file_name, "r")
    data_list = []
    maximum = -1
    maximum_index = -1
    for row in f.readlines():
        file_row = row.strip().split("\t")
        data_list.append(file_row)
    f.close()
    for i in range(len(data_list)):
        year = int(data_list[i][2])
        if year > maximum:
            maximum = year
            maximum_index = i
    return data_list[maximum_index][0]


def count_by_genre(file_name, genre):
    f = open(file_name, "r")
    data_list = []
    maximum = -1
    lel = []
    for row in f.readlines():
        file_row = row.strip().split("\t")
        data_list.append(file_row[3])
    f.close()
    for x in data_list:
        if x not in lel:
            lel.append(x)
    result = len(lel)-1
    return result


def get_line_number_by_title(file_name, title):
    f = open(file_name, "r")
    data_list = []
    for row in f.readlines():
        file_row = row.strip().split("\t")
        data_list.append(file_row[0])
        for x in data_list:
            if x == title:
                result = data_list.index(title)+1
                return result


def main():
    a = count_games(file_name)
    b = decide(file_name, year)
    c = get_latest(file_name)
    d = count_by_genre(file_name, genre)
    e = get_line_number_by_title(file_name, title)
if __name__ == "__main__":
    main()
# Report functions
