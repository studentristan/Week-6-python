#assignment 6.5
#Tristan Werden
#TODO: None
#NOTES: I originally did this with like 4 lines, but the autograder kept telling me that I had to "pull data from the variable", which made no sense to me. It was because I had 0.8475 written into the text.find() function rather than just 0. Both work the same. It's the same thing. But I'm glad it made me do it that way, because I ended up reusing this single line on the week 7 assignment.

text = "X-DSPAM-Confidence:    0.8475"

print(float(text[text.find("0"):]))

