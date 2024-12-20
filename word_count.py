# a word-count program


# input is a line of text
line = input("Please input a line of text: ")

# remove leading and trailing spaces
line = line.strip()

# count number of words
total_words = line.count(" ") + 1

# output is the number of words in the line of text
print(total_words)
