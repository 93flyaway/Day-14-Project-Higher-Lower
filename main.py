from art import logo, vs
from game_data import data
from random import choice
from replit import clear

#next, we need to find a way to choose an element from the data list and delete that component from the list
def choose(data_pool):
    """returns a randomly chosen account from data list. chosen account is removed from the list"""
    account = choice(data_pool)
    data_pool.remove(account)
    return account

#find way to determine winner
def did_a_win(competitors):
    """returns True if A is the winner. returns false if B is the winner. this function assumes that the two competitors have different follower counts."""
    count_a = competitors[0]['follower_count']
    count_b = competitors[1]['follower_count']
    if count_a > count_b:
        return True
    if count_a < count_b:
        return False    

def play_game():
    #first, we need to print the logo
    print(logo)
    score = 0
    is_user_win = True
    account_pool = data
    competitor_list =[]
    competitor_list.append(choose(account_pool))

    while is_user_win:
        #choose A and B and put them in a list in order
        competitor_list.append(choose(account_pool))
        choice_a = competitor_list[0]
        choice_b = competitor_list[1]

        #determine winner. if A won, did_a_win will be True.
        is_a_winner = did_a_win(competitor_list)
        is_b_winner = not is_a_winner

        #initial score = 0

        #next, print "Compare A: {name}, a {description}, from {country}."
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")

        #then print vs
        print(vs)

        #then, print "Against B: "{name}, a {description}, from {country}."
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

        #finally, make user choose:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        #find out if user_answer is correct
        if user_answer == 'a':
            if is_a_winner:
                is_user_win = True
            else:
                is_user_win = False
        elif user_answer == 'b':
            if is_b_winner:
                is_user_win = True
            else:
                is_user_win = False
        else:
            is_user_win = False
        
        #clear console
        clear()
        print(logo)
        
        if is_user_win:
            score += 1
            print(f"You're right! Current score: {score}.")
            competitor_list.pop(0)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()