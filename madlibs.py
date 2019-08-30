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
        print("A noun is a person, place, or thing, such as 'hat', 'mouse', or 'table'.\n")
        return get_noun()
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
    print (get_noun())

welcome_text()
if select_story()==1:
    day_at_the_beach()
