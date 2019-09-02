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


#parts of speech
def get_noun():
    input = str(user_input("Noun: "))
    if (input.upper()=="HELP"):
        print("A noun is a person, place, or thing, such as 'hat', 'mouse', or 'table'.")
        return get_noun()
    else:
        return purple(input.lower())


def get_plural_noun():
    input = str(user_input("Plural noun: "))
    if (input.upper()=="HELP"):
        print("A noun is a person, place, or thing. Plural nouns refer to more than one thing, such as 'hats', 'mice', or 'tables'.")
        return get_plural_noun()
    else:
        return purple(input.lower())


def get_int():
    input = str(user_input("Integer: "))
    if (input.upper()=="HELP"):
        print("An integer is a whole number, such as 1, 23, or 100.")
        return get_int()
    else:
        return green(input.lower())


def get_float():
    input = str(user_input("Float: "))
    if (input.upper()=="HELP"):
        print("A float is a number that includes a decimal, such as 1.3, 10.00, or 132.55.")
        return get_float()
    else:
        return green(input.lower())


def get_verb():
    input = str(user_input("Verb: "))
    if (input.upper()=="HELP"):
        print("A verb is an action word, like 'run' or 'eat'.")
        return get_verb()
    else:
        return orange(input.lower())


def get_name():
    input = str(user_input("Name: "))
    if (input.upper()=="HELP"):
        print("A person's name, like 'Sophia' or 'Muhammad'")
        return get_name()
    else:
        return blue(input)


def get_adjective():
    input = str(user_input("Adjective: "))
    if (input.upper()=="HELP"):
        print("An adjective descriptor, such as 'red', 'quick', or 'bad'.\n")
        return get_adjective()
    else:
        return pink(input.lower())


def get_adverb():
    input = str(user_input("Adverb: "))
    if (input.upper()=="HELP"):
        print("An adverb is a descriptor for a verb, such as 'quickly', 'easily', or 'deftly'.\n")
        return get_adverb()
    else:
        return yellow(input.lower())


def get_clothing():
    input = str(user_input("Clothing item: "))
    if (input.upper()=="HELP"):
        print("A type of clothing, like 'pants', 'ha†', or 'shirt'.\n")
        return get_clothing()
    else:
        return purple(input.lower())


def get_accessory():
    input = str(user_input("Clothing accessory: "))
    if (input.upper()=="HELP"):
        print("A nonvital, decorative item of clothing, such as 'bows', 'earrigs', or 'necklace'.\n")
        return get_accessory()
    else:
        return purple(input.lower())
#end parts of speech


def select_story():
    input = user_input("Which story would you like to create? (1/2/3): ")
    if int(input) == 1 or int(input) == 2 or int(input) == 3:
        return int(input)
    else:
        print("Invalid response")
        return select_story()


#colors
def red(item):
    return "\033[31m{}\033[00m".format(item)


def orange(item):
    return "\033[91m{}\033[00m".format(item)


def yellow(item):
    return "\033[93m{}\033[00m".format(item)


def green(item):
    return "\033[32m{}\033[00m".format(item)


def blue(item):
    return "\033[34m{}\033[00m".format(item)


def purple(item):
    return "\033[35m{}\033[00m".format(item)


def pink(item):
    return "\033[95m{}\033[00m".format(item)


def indigo(item):
    return "\033[94m{}\033[00m".format(item)
#end colors


def select_format():
    return user_input("Would you like to fill in the blanks in order, or randomize the order? (ORDER/RANDOM): ")


def welcome_text():
    print ("Madlibs are fun stories you fill in with your own words. We'll prompt you with parts of speech--just type your responses and hit 'ENTER'\nIf you don't know what one of the prompts means, you can enter HELP for a definition.\n\n")


def day_at_the_beach():
    print ("It was an average, {} day and I decided to go to the beach with {}. As we walked up to the shore, we saw a sign for {}'s Discount {}. We ran up {} to get something to eat, but were shocked to find that they only sold {}. We were already there, so we bought {}. They only cost ${} each. Carrying our purchases, we made our way down to the water {}. We put on our swimwear: {} and {} with {} to accessorize. Finally, we tried to get in the ocean. Unfortunately, it was too {} for our liking, so we went home.".format(get_adjective(),get_name(),get_name(),get_plural_noun(), get_adverb(), get_plural_noun(), get_int(), get_float(), get_adverb(), get_clothing(), get_clothing(), get_accessory(), get_adjective()))

welcome_text()
if select_story()==1:
    day_at_the_beach()
