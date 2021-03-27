from random import choice,shuffle

#It is just representing 0 - "Goat" and 1 - "Prize" 
test_list = [ 0, 1, 0 ]

#It returns True If after changing our choice works else False
def change_choice(dct , person_choice, opend_choice):

    #this is extracting a list of keys in dict
    key = list(dct.keys())

    # this is removing key from list after matching it with person_choice
    key.remove(person_choice)

    # this is removing key from list after matching it with person_choice
    key.remove(opend_choice)


    if dct[key[0]] == 0:
        return False
    else:
        return True




def testing_cases(n):

    #these are 2 variables given initiation just to count favourable cases or not 
    count_change_choice_works = 0
    count_staying_at_choice_works = 0


    for _ in range(n):

        #shuffle is random module function which is used to shuffle elements
        shuffle(test_list)

        test_dict = { "A":test_list[0], "B":test_list[1], "C":test_list[2] }
        key_list = ["A", "B", "C"]
        x = choice(list(test_dict.keys()))
        key_list.remove(x)
        if test_dict[key_list[0]] == 0:
            if change_choice(test_dict, x, key_list[0]):
                count_change_choice_works += 1
            else:
                count_staying_at_choice_works += 1
        else:
            if change_choice(test_dict, x, key_list[1]):
                count_change_choice_works += 1
            else:
                count_staying_at_choice_works += 1




    print(f"Changing decision works: {count_change_choice_works}\n"+
          f"Staying at Choice works: {count_staying_at_choice_works}"
          )


if __name__ == "__main__":
    n = int(input("Enter number upto you want to test cases for Monty Hall: "))
    print()
    testing_cases(n)
    print()