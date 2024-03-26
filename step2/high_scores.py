class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        highests = []
        temp = self.scores.copy()
        for i in range(min(3, len(temp))):
            highests.append(max(temp))
            temp.remove(max(temp))

        return highests
