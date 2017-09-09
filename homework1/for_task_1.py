def print_average(list, where=""):
    average = sum(list)/len(list)
    print("Среднее значение {} {}".format(where, average))


school_clases = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [4, 5, 2, 3 , 4, 2, 5]},
    {'school_class': '5a', 'scores': [4, 4, 5, 2, 4, 5, 2, 4]},
    {'school_class': '5b', 'scores': [3, 4, 3, 4, 5]},
    {'school_class': '6a', 'scores': [3, 4, 5, 5, 3, 4]},
    {'school_class': '6b', 'scores': [5, 5, 3, 4, 4, 5]},
    {'school_class': '7a', 'scores': [5, 5, 5, 3, 4, 2]},
    {'school_class': '7b', 'scores': [4, 5, 5, 5, 3, 3]},
    {'school_class': '8a', 'scores': [4, 3, 4, 3, 3]},
    {'school_class': '8b', 'scores': [3, 5, 3, 4, 3]},
    {'school_class': '9a', 'scores': [3, 4, 3, 4]},
    {'school_class': '9b', 'scores': [3, 5, 3, 5, 5, 3]},
    {'school_class': '10a', 'scores': [3, 4, 5, 4, 3, 5]},
    {'school_class': '10b', 'scores': [3, 4, 4, 5 ,2, 3, 3]},
    {'school_class': '11a', 'scores': [3, 4, 4, 5, 5, 5]},
    {'school_class': '11b', 'scores': [3, 2, 2, 2]}
]

all_scores = []
for school_class in school_clases:
    scores = school_class.get('scores')
    print_average(list=scores, where="по {} классу".format(school_class.get('school_class')))
    all_scores.extend(scores)

print_average(list=all_scores, where="по всей школе")
