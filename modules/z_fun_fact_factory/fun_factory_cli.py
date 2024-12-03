from fun_factory import FunFactory

is_exit = False
fun_factory = FunFactory()
win_score = 3
greeting_msg = f"""
\n
  _____                        _____               __                       
_/ ____\_ __  ____           _/ ____\____    _____/  |_  ___________ ___.__.
\   __\  |  \/    \   ______ \   __\\__  \ _/ ___\   __\/  _ \_  __ <   |  |
 |  | |  |  /   |  \ /_____/  |  |   / __ \\  \___|  | (  <_> )  | \/\___  |
 |__| |____/|___|  /          |__|  (____  /\___  >__|  \____/|__|   / ____|
                 \/                      \/     \/                   \/     
Welcome to the Fun (Fact) Factory! 
I will generate random fun facts that are either true or false.
You will have to guess whether they are true or false.
If you guess correctly, you win a point, otherwise, I win a point.
First to {win_score} points wins, good luck!
\n
"""
print(greeting_msg)
print()
player = 0
ai = 0
while not is_exit:
    try:
        user_input = input("Press Enter to generate a fun fact (or `exit`). ")
        if user_input == "exit":
            is_exit = True
            continue
        elif user_input != "":
            continue
        fact = fun_factory.generate_fun_fact()
        print(fact.fact)
        answer = input("Is it true? (true/false) ")
        is_true = answer == "true"
        followup = fun_factory.generate_followup(fact, is_true)
        print(followup)

        if is_true == fact.is_true:
            player += 1
            print("You win a point!")
        else:
            ai += 1
            print("I win a point!")

        # print scores
        print(f"Player: {player}, AI: {ai}")
        print()

        if player == win_score:
            print("Congratulations! You won!")
            is_exit = True
        elif ai == win_score:
            print("I won! Better luck next time!")
            is_exit = True
    except Exception as e:
        print("Error occurred, please try again")
        print("Error: ", e)
