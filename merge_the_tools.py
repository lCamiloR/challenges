def merge_the_tools(string, k):
    splited_string = [string[i:i+k] for i in range(0, len(string), k)]

    for value in splited_string:
        temp_string = ""
        for character in value:
            if character not in temp_string:
                temp_string += character
        print(temp_string)


if __name__ == '__main__':
    #string, k = input(), int(input())
    merge_the_tools('AABCAAADA', 3)