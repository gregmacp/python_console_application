#bbc test

import csv
import uuid


# Open the csv file and use python's csv utility to read into memory

f = open('rms_albums.csv')
csv_f = csv.reader(f)

# transfer the csv reader object data to a standard list object
data = []
for row in csv_f:
    data.append(row)

#########################
# Handler functions
# made for each option to abstract some functionalities and simplify organisation
#########################

def handle_get():
  get()

def handle_update():
    print ("Please choose which entry to update.")
    update()

def handle_add():

    # obtain details for our new entry from the user
    print()
    print ("Please enter details of your new entry.")
    album = input("Album Title: ")
    print()
    artist = input("Artist: ")
    print()
    year = input("Year: ")
    print()

    # use python's uuid utility to generate a new uuid for our entry
    id = str(uuid.uuid4())

    # call the add function and pass in the details supplied by the user
    add(album, artist, year, id)

def handle_delete():
    # call selector function to search for a specific entry in the data
    # result returned is a single row (album)
    print ("")
    print ("Please choose which entry to delete.")
    result = selector("deleted")

    # confirm the action with the user and then call the delete function, passing
    # the uuid of the target entry to be deleted
    confirm = input ("Are you sure you want to delete "+ result[1] +"? [Y/N]\n")
    if (confirm == "Y"):
        delete(result[0])

#########################
#########################

#########################
# Main functions
# perform the main actions of the program
#########################

# get function
# searches data by either id, album, artist or year depending on user's choice
# will return an error message if no results Found
# will return multiple results if found
def get():

    param = ""
    query = ""
    # asks the user how they would like to search the data
    # then asks for a specific query
    while param != "album" and param != "artist" and param != "year" and param != "id":
        print ()
        param = input("How do you want to search for an entry? [id, artist, album, year]\n")
        print ()
    if param != "":
        query = input("Please enter the " + param + " you want to search for:\n")

    # creates a dictionary to easily map the user's choice to an index
    target_dict = {"album": 1, "artist": 2, "year": 3}
    results = []

    # search the data and find a matching row
    # matching row added to new list 'results'
    # strip() used to remove whitespace from both query and data

    # Display the results to the user.
    # If more than one result is found, number the results
    for row in data:
        if (query.strip() == row[target_dict[param]].strip()):
            results.append(row)
    if results is None:
            print ()
            print ("No results found for query.")
            print ()
    else:
        x = "y"
        if (len(results)>1):
            x = "ies"
        print()
        print ("Found "+ str(len(results)) + " entr"+ x +":")
        i = 1
        for row in results:
            print (str(i) + ". " + str(row[1:]).strip('[]'))
            i += 1
        return results

# Selector function
# calls get() and then asks the user to select one of the results
# returns just one result
# accepts "action" which is either the string "deleted" or "updated"
def selector(action):
    results = []
    while len(results) != 1:
        results = get()
        if results is None:
            results = []
        elif len(results) > 1:
            print()
            choice = ""
            while True:
                e = input ("Which entry should be "+ action +"?\n")
                choice = int(e) if e.isdigit() else None
                if choice:
                    if choice <= len(results) and choice > 0:
                        break
            c = results[(choice-1)]
            results.clear()
            results.append(c)
    result = results[0]
    return result

# update function
# calls selector function to receive an Entry
# gets new details from user
# changes data to reflect these changes
def update():
    result = selector("updated")
    target_dict = {"album": 1, "artist": 2, "year": 3}
    target_row = ""

    #identify entry in data
    for row in data:
        if (result[0] == row[0]):
            target_row = row
            break

    param = ""
    while param != "album" and param != "artist" and param != "year":
        print ()
        param = input("What would you like to change? [album, artist, year]\n")
        print ()

    target_param = target_dict[param]
    print ()

    newvalue = input("Enter new value for " + param + ":\n")
    print ()
    target_row[target_param] = newvalue

    print ()
    print ("Entry has been updated")
    print (str(target_row[1:]).strip('[]'))

# Add function
# Receives details for a new entry
# appends new entry to data as a list
def add(album, artist, year, id):
    entry = [id, album, artist, year]

    print ()
    print ("Adding the following entry:")
    print (entry)
    print ()

    data.append(entry)

    print ("Entry succesfully added.")
    print ()

# Delete function
# Identifies a row to be deleted using the supplied id
# Removes entry from data
def delete(id):
    target_row = []
    for row in data:
        if (id == row[0]):
            removed = row
            data.remove(row)
            print()
            print ("removed entry" + str(removed))

# Show all
# Simply prints all of the data
# used for debugging
def show_all():
    print ()
    print ("Showing all data:")
    for row in data:
        print (row)
    print ()

#########################
#########################

# Menu
# While loop used to keep the user in a permanent loop until they choose to exit the app
def main():
    print()
    print ("1. Lookup an entry \n2. Update an entry \n3. Add an entry \n4. Delete Entry \n5. Show All \n0. Exit")
    response = int(input("Please choose an option: "))
    while response != 0:
        if response == 1:
          handle_get()
        elif response == 2:
          handle_update()
        elif response == 3:
          handle_add()
        elif response == 4:
          handle_delete()
        elif response == 5:
          show_all()


        else:
            print("Please enter a valid option.")

        print()
        print ("1. Lookup an entry \n2. Update an entry \n3. Add an entry \n4. Delete Entry \n5. Show All \n0. Exit")
        response = int(input("Please choose an option: "))

    print("\nThanks for using the application.")


if __name__ == "__main__":
    main()















#
