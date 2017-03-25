negative_list = []
positive_list = []
with open("negatives.txt", "r") as negatives:
    for line in negatives:
        line = line.replace(' ', '').strip('\n')
        negative_list.append(line)

with open("positives.txt", "r") as positives:
    for line in positives:
        line = line.replace(' ', '').strip('\n')
        positive_list.append(line)


def start_conversation(friend_name):
    your_responses = []
    friend_responses = []

    your_response = ""
    friend_response = ""

    print("Conversation started")

    while ("bye" not in your_response.split(' ')) and ("bye" not in friend_response.split(' ')):

        punctuations = ['.', '?', '!', ':', ',', ';', '(', ')', '[', ']', '/']

        # Allows you to enter your msg to your friend.
        print("ME:", end=' ')
        your_response = input()
        # print(your_response)         # FIX THIS
        your_response = your_response.lower()
        your_response = "".join([i for i in your_response if i not in punctuations])
        your_words = your_response.split(' ')
        your_responses += your_words            # Stores your response in a list.

        # Allows your friend to respond.
        print(friend_name, end='')
        print(":", end=' ')
        friend_response = input()
        # print(friend_response)
        friend_response = friend_response.lower()
        friend_response = "".join([i for i in friend_response if i not in punctuations])
        friend_words = friend_response.split(' ')
        friend_responses += friend_words      # Stores the friend's response in list.

    your_score = 5
    friend_score = 5

    for word in your_responses:
        for response in negative_list:
            if word == response:
                your_score -= 1
                break
        for response in positive_list:
            if word == response:
                your_score += 1
                break

    for word in friend_responses:
        for response in negative_list:
            if word == response:
                friend_score -= 1
                break
        for response in positive_list:
            if word == response:
                friend_score += 1
                break

    print("Your Score: ", your_score)
    print("Friend's Score: ", friend_score)


def message(name):
    start_conversation(name)

friends = {1: "Delaney", 2: "Jason", 3: "Elijah"}

print("Who do you want to message?")

x = 1
for friend in friends:
    print(x, end='')
    print(". ", end='')
    print(friends[x])
    x += 1

y = int(input())

message(friends[y])

#




