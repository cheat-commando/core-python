"""Restaurant rating lister."""

# put your code here

import random, os, sys

print('\nHello, and welcome to the Restaurant Ratings App!')

def main():

    print("Please select one of the following lists of restaurants:\n")

    for file in os.listdir('./restaurants'):
        print(file)

    open_this_file = input("\nWhich of those lists would you like to look at? ")

    while not (open_this_file in os.listdir('./restaurants')):
        print(' ')
        for file in os.listdir('./restaurants'):
            print(file)
        open_this_file = input("\nTry again. Which of those lists would you like to look at? ")

    raw_restaurants_RAW = open(f'./restaurants/{open_this_file}', 'r')
    raw_restaurants = raw_restaurants_RAW.readlines()

    # This code takes the raw data and puts them into the restauratns object
    restaurants = {}
    for line in raw_restaurants:
        clean_line = line.strip()
        name, rating = clean_line.split(':')
        restaurants[name] = int(rating)

    def validate_rating(num):
        while not (num in ['1', '2', '3', '4', '5']):
            num = input("That was not a valid entry. Try again\nValid entries are 1, 2, 3, 4, or 5 ")
        return num

    # Displays an alphabetized list of the restaurants 
    def print_alpha_restaurants(dict):

        def sorter(item):
            return item[0].lower()

        list_restaurants = sorted(dict.items(), key=sorter)

        for restaurant in list_restaurants:
            print(restaurant[0], "is rated at", restaurant[1])
        
        print('\n')
        opening_query()
    
    # User adds a new restaurant and rating to the object
    def add_new_restaurant():

        new_restaurant = input("What restaurant are you rating? ")
        new_rating = input('What rating would you give this restaurant? Viable ratings are 1, 2, 3, 4, or 5\n')

        restaurants[new_restaurant] = int(validate_rating(new_rating))

        print_alpha_restaurants(restaurants)

    # User edits the rating on a random restaurant
    def review_rando_restaurant():
        rando_restaurant = random.choice(list(iter(restaurants.items())))
        print("You are reviewing ", rando_restaurant[0], ". Its rating is currently: ", rando_restaurant[1], sep='')
        new_rating = input("Please give this restaurant a new rating. (Valid options are 1, 2, 3, 4, or 5) ")
        
        restaurants[rando_restaurant[0]] = int(validate_rating(new_rating))
        print("Thank you!", rando_restaurant[0], "now has a rating of:", new_rating)

        print_alpha_restaurants(restaurants)

    # User edits a chosen restaurant's rating
    def review_chosen_restaurant():
        chosen_restaurant = input("Enter the name of a restaurant: ")

        while not (chosen_restaurant in restaurants.keys()):
            if not chosen_restaurant == 'back':
                chosen_restaurant = input("That restaurant is not in the list.\nEnter the name of a restaurant. Type 'back' if you are stuck and can't remember anything.")

        if not chosen_restaurant == 'back':
            print("You are reviewing ", chosen_restaurant, ". Its rating is currently: ", restaurants[chosen_restaurant], sep='')
            new_rating = input('Enter a new rating for this restaurant. Valid entries are: 1, 2, 3, 4, 5 ')

            restaurants[chosen_restaurant] = int(validate_rating(new_rating)) 

            print(f"{chosen_restaurant}'s rating has been updated to {restaurants[chosen_restaurant]}\n") 

            print_alpha_restaurants(restaurants)
        else:
            main()
    
    def change_list():
        raw_restaurants_RAW.close()
        main()

    def opening_query():

        print("Select one of the following options (Do NOT type quotation marks):")
        command = input("Ratings (type: 'ratings')\nAdd a new restaurant (type: 'add')\nEdit random restaurant rating (type: 'edit')\nChoose a restaurant to rate (type: 'choose')\nChange which list to view (type: 'change')\nQuit (type: 'quit')\n\n").lower()

        if not (command in ['ratings', 'add', 'edit', 'choose', 'change', 'quit']):
            print('\nTry again.')
            opening_query()
        else:
            if command == 'ratings':
                print_alpha_restaurants(restaurants)
            elif command == 'add':
                add_new_restaurant()
            elif command == 'edit':
                review_rando_restaurant()
            elif command == 'choose':
                review_chosen_restaurant()
            elif command == 'change':
                change_list()
            elif command == 'quit':
                sys.exit("Have a good day!\n")
    
    opening_query()

main()


