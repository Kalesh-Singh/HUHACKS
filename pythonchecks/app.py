import  MySQLdb
import sys

negative_list = []
positive_list = []

with open("negatives.txt", "r") as negatives:
    for line in negatives:
        line = line.replace(' ', '').strip('\n\r')
        negative_list.append(line)

with open("positives.txt", "r") as positives:
    for line in positives:
        line = line.replace(' ', '').strip('\n\r')
        positive_list.append(line)

your_responses = []
friend_responses = []

punctuations = ['.', '?', '!', ':', ',', ';', '(', ')', '[', ']', '/', ' ']

your_words = []
friend_words = []

connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="platinum5*", db="huhacks")
cursor = connection.cursor()

cursor.execute("select message from conversations where fromnumber='123'")
your_data = cursor.fetchone()

while your_data is not None:
    your_words += your_data[0].split(' ')
    your_data = cursor.fetchone()
for i in range(len(your_words)):
    your_words[i] = your_words[i].lower()
    your_words[i] = "".join([j for j in your_words[i] if j not in punctuations])

#print(your_words)
#print(negative_list) 
#print(positive_list) 

cursor.execute("select message from conversations where fromnumber = '456' ")
friend_data = cursor.fetchone()
while friend_data is not None:
    friend_words += friend_data[0].split(' ')
    friend_data = cursor.fetchone()
for i in range(len(friend_words)):
    friend_words[i] = friend_words[i].lower()
    friend_words[i] = "".join([j for j in friend_words[i] if j not in punctuations])


print(friend_words)

your_score = 50
friend_score = 50

for word in your_words:
    for response in negative_list:
        if word == response:
            your_score -= 1
            break
    for response in positive_list:
        if word == response and your_score < 100:
            your_score += 1
            break

for word in friend_words:
    for response in negative_list:
        if word == response:
            friend_score -= 1
            break
    for response in positive_list:
        if word == response and friend_score < 100:
            friend_score += 1
            break


print("Your score:",your_score)
print("Your friend's score:",friend_score)



