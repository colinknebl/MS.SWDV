

def main():
    # read the file
    file = open('./workouts.csv', 'r')
    dict = {}
    sortedDict = {}

    print(file)
    file.readline()
    #
    for line in file.readlines():
        # ['date', 'title', 'description', 'best_result_raw',
        # 'best_result_display', 'score_type', 'barbell_lift',
        # 'set_details', 'notes', 'rx_or_scaled', 'pr\n']
        data = line.split(',')
        # print(data)
        if data[1] not in dict:
            dict[data[1]] = []
        dict[data[1]].append(data)

    for i in sorted(dict.keys()):
        # print(i)
        sorted

    print(dict)


    # close the file
    file.close()


if __name__ == '__main__':
    main()