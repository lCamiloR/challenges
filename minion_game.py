def minion_game(target_string:str):
    vowels = ('A', 'E', 'I', 'O', 'U')
    stuart_occurs = []
    kevin_occurs = []
    kevin_score = 0
    stuart_score = 0
    target_string = target_string.upper()

    for idx in range(len(target_string)):
        for inner_idx in range(idx, len(target_string)):
            interation_str = target_string[idx : inner_idx + 1]
            if interation_str[0] in vowels:
                if interation_str not in kevin_occurs:
                    kevin_occurs.append(interation_str)
                    kevin_score += target_string.count(interation_str)
            else:
                if interation_str not in stuart_occurs:
                    stuart_occurs.append(interation_str)
                    stuart_score += target_string.count(interation_str)
    print(kevin_occurs)
    if kevin_score == stuart_score:
        print('Draw')
    elif kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print(f'Stuart {stuart_score}')


if __name__ == '__main__':
    #s = input()
    # minion_game("BANANA")
    # print("ANANAS".count("ANANAS"))

    teste_var = "BAANANAS"

    for idx in range(len(teste_var)):
        for inner_idx in range(idx, len(teste_var)):
            print(teste_var[idx:inner_idx + 1])