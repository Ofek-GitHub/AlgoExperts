def tournamentWinner(competitions, results):
    score = {}

    for i in range(len(competitions)):
        score.setdefault(competitions[i][0], 0)
        score.setdefault(competitions[i][1], 0)

    for i in range(len(results)):
        if results[i] == 0:
            score[competitions[i][1]] += 3
        else:
            score[competitions[i][0]] += 3
    max_key = None
    max_value = float('-inf')

    for key, value in score.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

result = [0, 0, 1]  # 0 means away team wins, 1 means home team wins.

winner = tournamentWinner(competitions, result)
print(winner)
