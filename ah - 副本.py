def judge_input():
    while True :
        input_number=input()
        if input_number.isnumeric():
            guess_number=int(input_number)
            if judgement_input():
                exit(0)
            else:
                continue
        else:
            print("You must type an integer!")
