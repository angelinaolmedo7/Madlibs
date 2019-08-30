responses = list()


def create(item):
    responses.append(item)


def read(index):
    return responses[index]


def update(index, item):
    if index < len(checklist):
        responses[index] = item
    else:
        print ("Invalid index\n")


def destroy(index):
    if index < len(checklist):
        responses.pop(index)
    else:
        print ("Invalid index\n")


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def get_noun():
    input = str(user_input("Noun: "))
    if (input.upper()=="HELP"):
        print("A noun is a person, place, or thing, such as 'hat', 'mouse', or 'table'.")
        return get_noun()
    else:
        return input.lower()


def get_verb():
    input = str(user_input("Verb: "))
    if (input.upper()=="HELP"):
        print("A verb is an action word, like 'run' or 'eat'.")
        return get_verb()
    else:
        return input.lower()


def get_adjective():
    input = str(user_input("Adjective: "))
    if (input.upper()=="HELP"):
        print("An adjective descriptor, such as 'red', 'quick', or 'bad'.\n")
        return get_adjective()
    else:
        return input.lower()


def get_adverb():
    input = str(user_input("Adverb: "))
    if (input.upper()=="HELP"):
        print("An adverb is a descriptor for a verb, such as 'quickly', 'easily', or 'deftly'.\n")
        return get_adverb()
    else:
        return input.lower()


def select_story():
    input = user_input("Which story would you like to create? (1/2/3): ")
    if int(input) == 1 or int(input) == 2 or int(input) == 3:
        return int(input)
    else:
        print("Invalid response")
        return select_story()


def select_format():
    return user_input("Would you like to fill in the blanks in order, or randomize the order? (ORDER/RANDOM): ")


def welcome_text():
    print ("Madlibs are fun stories you fill in with your own words. We'll prompt you with parts of speech--just type your responses and hit 'ENTER'\nIf you don't know what one of the prompts means, you can enter HELP for a definition.\n\n")


def day_at_the_beach():
    print ("It was an average, {} day and I decided to go to the beach with {}. As we walked up to the shore, we saw a sign for {}'s Discount {}. We ran up {} to get something to eat, but were shocked to find that they only sold {}. We were already there, so we bought {}. They only cost ${} each. Carrying our purchases, we made our way down to the water {}. We put on our swimwear: {} and {} with {} to accessorize. Finally, we tried to get in the ocean. Unfortunately, it was too {} for our liking, so we went home.".format(get_adjective(),get_noun(),get_noun(),get_noun(), get_adverb(), get_noun(), get_noun(), get_noun(), get_adverb(), get_noun(), get_noun(), get_noun(), get_adjective()))

welcome_text()
if select_story()==1:
    day_at_the_beach()
