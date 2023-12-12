#define our bookshelf
myShelf = "Little Women~An Absolutely Remarkable Thing~The Bluest Eyes~Python for Everyone~The Hunger Games~Fun Home"

#Function bookCount should take a string and return the number of books on your shelf
def bookCount(myShelf):
    splitBook = myShelf.split("~")
    number_of_book = len(splitBook)
    return number_of_book
    
print("How many books? ", bookCount(myShelf))
