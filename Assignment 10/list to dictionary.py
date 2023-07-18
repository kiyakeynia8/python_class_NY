names = ["mamad", "jafar", "kiya", "sara", "nima", "nika", "babak"]
scores = [18.5, 19, 19, 19,5, 17, 20]

scores_dict = {}

i = 0
for name in names:
    scores_dict[name] = scores[i]
    i += 1

print(scores_dict)