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
    return user_input.strip()


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
        return blue(input.lower().capitalize())


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
        print("A nonvital, decorative item of clothing, such as 'bows', 'earrings', or 'necklace'.\n")
        return get_accessory()
    else:
        return purple(input.lower())


def get_food():
    input = str(user_input("Type of food: "))
    if (input.upper()=="HELP"):
        print("A variety of food, such as 'pancakes', 'pizza', or 'breakfast'.\n")
        return get_food()
    else:
        return purple(input.lower())


def get_location():
    input = str(user_input("Location: "))
    if (input.upper()=="HELP"):
        print("A place, such as 'grocery store' or 'dog park'.\n")
        return get_location()
    else:
        return purple(input.lower())


def get_year():
    input = str(user_input("Year: "))
    if (input.upper()=="HELP"):
        print("A calendar year, such as '2019', '1802', or '300 BCE'.\n")
        return get_year()
    else:
        return green(input.lower())
#end parts of speech


def select_story():
    input = user_input("Which story would you like to create? (1/2): ")
    if str(input) == "1" or str(input) == "2":
        return int(input)
    elif str(input).upper() == "Q":
        return 0
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


def ccapitalize(item): #color capitalize
    #print(item[5:len(item)-4].capitalize())
    return "\0" + item[0:5] + item[5:len(item)-4].capitalize() + "\0" + item[len(item)-4:len(item)]


def select_format(): #didn't get to this in time
    return user_input("Would you like to fill in the blanks in order, or randomize the order? (ORDER/RANDOM): ")


def select_pronouns():
    selection = user_input("Which pronuns do you use? Enter:\nS: she/her/hers\nH: he/him/his\nT: they/them/theirs\nC: custom\n[S/H/T/C]: ")
    pronouns_dict = {
    "they": "they",
    "them": "them",
    "their": "their",
    "theirs": "theirs",
    "ww" : "were"
    }
    if selection.upper() == "S":
        pronouns_dict["they"] = "she"
        pronouns_dict["them"] = "her"
        pronouns_dict["their"] = "her"
        pronouns_dict["theirs"] = "hers"
        pronouns_dict["ww"] = "was"
        return pronouns_dict
    elif selection.upper() == "H":
        pronouns_dict["they"] = "he"
        pronouns_dict["them"] = "him"
        pronouns_dict["their"] = "his"
        pronouns_dict["theirs"] = "his"
        pronouns_dict["ww"] = "was"
        return pronouns_dict
    elif selection.upper() == "T":
        return pronouns_dict
    elif selection.upper() == "C":
        return custom_pronouns()
    else:
        print ("Please enter a valid selection.")
        return select_pronouns()


def custom_pronouns():
    pronouns_dict = {
    "they": "they",
    "them": "them",
    "their": "their",
    "theirs": "theirs",
    "ww" : "were"
    }

    pronouns_dict["they"] = user_input("What pronoun would you use to replace 'they' in the following sentence?\n" + purple("They") + " own(s) that jacket. ")
    pronouns_dict["them"] = user_input("What pronoun would you use to replace 'them' in the following sentence?\nThat jacket belongs to " + purple("them") + ". ")
    pronouns_dict["their"] = user_input("What pronoun would you use to replace 'their' in the following sentence?\nThat is " + purple("their") + " jacket. ")
    pronouns_dict["theirs"] = user_input("What pronoun would you use to replace 'theirs' in the following sentence?\nThat jacket is " + purple("theirs") + ". ")
    pronouns_dict["ww"] = custom_ww(pronouns_dict)

    print ("\nDoes this look right?\nI saw " + purple(pronouns_dict["them"]) + " walking to the store with "+ purple(pronouns_dict["their"]) + " friend. " + purple(pronouns_dict["they"].capitalize()) + " " + purple(pronouns_dict["ww"]) + " walking a dog, but I'm not sure if it was " + purple(pronouns_dict["theirs"]) + ".")
    yn = user_input("[YES/NO]: ")
    if yn.upper() == "YES" or yn.upper() == "Y":
        return pronouns_dict
    else:
        return custom_pronouns()


def custom_ww(pronouns_dict): #separate function so i can call recursively if input is invalid
    ww = user_input("Would you use 'was' or 'were' in the following sentence?\n" + pronouns_dict["they"].capitalize() + " " + purple("was/were") + " planning on getting a new jacket.\n[WAS/WERE]: ")
    if ww.upper() == "WAS" or ww.upper() == "WERE":
        return ww.lower()
    else:
        print ("Please input either WAS or WERE.")
        return custom_ww(pronouns_dict)


def welcome_text():
    print ("Madlibs are fun stories you fill in with your own words. We'll prompt you with parts of speech--just type your responses and hit 'ENTER'\nIf you don't know what one of the prompts means, you can enter HELP for a definition.\n")


def day_at_the_beach(): #story 1
    print ("\nA Day At The Beach\nIt was an average, {} day and I decided to go to the beach with {}. As we walked up to the shore, we saw a sign for {}'s Discount {}. We ran up {} to get something to eat, but were shocked to find that they only sold {}. We were already there, so we bought {}. They only cost ${} each. Carrying our purchases, we made our way down to the water {}. We put on our swimwear: {} and {} with {} to accessorize. Finally, we tried to get in the ocean. Unfortunately, it was too {} for our liking, so we went home.".format(get_adjective(), get_name(), get_name(), ccapitalize(get_food()), get_adverb(), get_plural_noun(), get_int(), get_float(), get_adverb(), get_clothing(), get_clothing(), get_accessory(), get_adjective()))

def my_wiki(): #story 2
    personal_info = {
    "fname": user_input("What is your first name? ").lower().capitalize(),
    "lname": user_input("What is your last name? ").lower().capitalize()
    }
    pronouns = select_pronouns()
    for key in pronouns:
        personal_info[key] = pronouns[key]

    #for key in personal_info:
    #    print(key + ": " + personal_info[key])

    your_noun = get_plural_noun()
    #story start
    print("\nMy Wikipedia Page\n\n{} {} was born in the year {} but is now {} years old, due to inexplicable time discrepancies. {} is most well known for being the inventor of the {} and owning the largest known collection of {}.\n\nEarly Life\n\n{} shocked onlookers when {} {} born in a {} at the tender age of 0. One witness reportedly claimed that {}'s birth was 'so {} I had to look away.' Not much is known about {}'s childhood due to extensive government redaction, though there is some debate as to whether {} may have written the popular and {} novel 'The {} {}.'\n\nShort-lived Career in {} Manufacture\n\n{} {} entered the public eye when {} announced a new business venture specializing in the manufacture of {} called {}{}. Unfortunately, the business declared bankruptcy after selling only {} units and forced {} into relative obscurity. Complaints that the {} were too {} and {} were cited as the cause of {}'s downfall.".format(personal_info["fname"], personal_info["lname"], get_year(), get_int(), personal_info["lname"], get_noun(), get_plural_noun(), personal_info["lname"], personal_info["they"], personal_info["ww"], get_location(), personal_info["lname"], get_adjective(), personal_info["lname"], personal_info["they"], get_adjective(), ccapitalize(get_adjective()), ccapitalize(get_noun()), ccapitalize(your_noun), personal_info["fname"], personal_info["lname"], personal_info["they"], your_noun, ccapitalize(get_adjective()), your_noun, get_int(), personal_info["lname"], your_noun, get_adjective(), get_adjective(), personal_info["fname"]))
    #story end


print(ccapitalize(purple("hello")))

welcome_text()

selection = select_story()
if selection == 1:
    day_at_the_beach()
elif selection == 2 :
    my_wiki()
