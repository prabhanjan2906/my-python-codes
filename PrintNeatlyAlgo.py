import sys
INFINITY = sys.maxint


def calculateExtraSpaceCharacterMatrix(words, extraSpaceCharacters, M):
    for i in range(len(words)):
        extraSpaceCharacters[i][i] = M - len(words[i])
        j = i + 1
        while j < len(words):
            extraSpaceCharacters[i][j] = extraSpaceCharacters[i][j-1] - len(words[j]) - 1
            j += 1


def calculateLeastCount(words, extraSpaceCharacters, leastCount):
    for i in range(len(words)):
        j = i
        while (j < len(words)):
            if extraSpaceCharacters[i][j] < 0:
                leastCount[i][j] = INFINITY
            elif ((j == len(words) - 1) and (extraSpaceCharacters[i][j] >= 0)):
                leastCount[i][j] = 0
            else:
                leastCount[i][j] = extraSpaceCharacters[i][j] * extraSpaceCharacters[i][j] * extraSpaceCharacters[i][j]
            j += 1


def calculateCost(words, cost, leastCount, p):
    cost[0] = 0
    for j in range(len(words)):
        cost[j] = INFINITY
        i = 0
        while i < j:
            if (cost[i-1] + leastCount[i][j]) < cost[j]:
                cost[j] = cost[i-1]+leastCount[i][j]
                p[j] = i
            i += 1


def print_neatly(words, M):
    """ Print text neatly.
    Parameters
    ----------
    words: list of str
    Each string in the list is a word from the file.
    M: int
    The max number of characters per line including spaces

    Returns
    -------
    cost: number
        The optimal value as described in the textbook.
    text: str
        The entire text as one string with newline characters.
        It should not end with a blank line.

    Details
    -------
        Look at print_neatly_test for some code to test the solution.
    """
    # TODO: Solve the problem

    extraSpaceCharacters = []
    leastCount = []
    cost = []
    p = []

    for i in range(len(words)):
        extraSpaceCharacters.append([0]*len(words))
        leastCount.append([0]*len(words))
        cost.append(0)
        p.append(0)

    calculateExtraSpaceCharacterMatrix(words, extraSpaceCharacters, M)

    calculateLeastCount(words, extraSpaceCharacters, leastCount)

    calculateCost(words, cost, leastCount, p)

    # print neatly
    i = 0
    j = len(words)
    finalString = ""

    while j >= 0:
        i = p[j - 1]
        line = words[i]
        for j in range(i + 1, j):
            line = line + ' ' + words[j]
        if j != len(words)-1:
            finalString = line + '\n' + finalString
        else:
            finalString = line

        j = i

        if j == 0:
            j = -1

    return cost[-1], finalString
