import json

try:
    data = open("story.json", "r")
except:
    print("story.json was not found. Exiting")
    quit
story = json.loads(data.read())

decision = "start"

while True:
    decision_data = story[decision]

    print(decision_data["text"])
    print(decision_data["question"])

    answer = input()

    decision = decision_data[answer]

    print("Nächste Entscheidung: " + decision)
