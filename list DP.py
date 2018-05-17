name = "Davis Piper"

subject = ["English","Science","Math","History"]

print("Hello "  + name)

for i in subject:
      print("One of my subjectsis " + i)

tvshows = ["the office","parks and rek","family guy","Simpsons"]

for i in tvshows:
    print("A show I like is " + i)



movies = []

while True:
    print("what movie do you like 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)



