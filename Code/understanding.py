# ARTIFICIAL INTELLIGENCE PROJECT - Automatic Story Summarization 

# ALGORITHM NAME - Information Extraction

import MontyLingua

ml = MontyLingua.MontyLingua()

f1 = open('gift-of-magi.txt')
f2 = open('the-skylight-room.txt')
f3 = open('the-cactus.txt')

# OWN - read the files
text1 = f1.read()
text2 = f2.read()
text3 = f3.read()


# OWN
# s-v-o-o tuple for a sentence is of form:
# ' "subject" "verb" "object" "object" '
# the following line removes the first and last space, "
# result: 'subject" "verb" "object" "object'
stuples1 = [w[2:-2] for w in ftuples1]
stuples2 = [w[2:-2] for w in ftuples2]
stuples3 = [w[2:-2] for w in ftuples3]

# OWN
# input: 'subject" "verb" "object" "object'
# output: [subject, verb, object, object]
btuples1 = [w.split('" "') for w in stuples1]
btuples2 = [w.split('" "') for w in stuples2]
btuples3 = [w.split('" "') for w in stuples3]

# OWN
# generates summary for the input
summary1 = ml.generate_summary(btuples1)
summary2 = ml.generate_summary(btuples2)
summary3 = ml.generate_summary(btuples3)

# OWN - print the summary generated for each story
print 'gift of magi:\n', summary1

print '\n\nthe skylight room:\n', summary2

print '\n\nthe cactus:\n', summary3
