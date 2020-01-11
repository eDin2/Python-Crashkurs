import random

# print(random.randint(0, 7))

part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]

best_word = [part1, part2, part3, part4]


# print(best_word)

def twitter_bot():
    satz = []
    for part in best_word:
        r = random.randint(0, len(part) - 1)
        # print(r)
        satz.append(part[r])
    # print(satz)
    print(" ".join(satz) + "!")  # ohne komma zwischen den einzelnen wörtern


twitter_bot()
twitter_bot()
twitter_bot()
