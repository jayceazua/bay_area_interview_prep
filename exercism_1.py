def latest(scores):
    if scores: 
        return scores[-1]
    return None


def personal_best(scores):
    highest = 0
    if scores: 
        for score in scores:
            if score > highest: 
                highest = score
    return highest


def personal_top_three(scores):
    first = 0
    second = 0
    third = 0

    if scores: 
        for score in scores: 
            if score >= first: 
                third = second
                second = first
                first = score
            elif score >= second: 
                third = second
                second = score
            elif score >= third: 
                third = score
                
    top_three = [first, second, third]

    return [val for val in top_three if val != 0]
