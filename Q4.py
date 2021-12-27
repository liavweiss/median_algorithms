import statistics


def compute_budget(total_budget: float, citizen_votes: list) -> list:
    l = 0
    r = 1
    while l <= r:
        mid = l + (r - l) / 2
        if sum(sum_of_medians(citizen_votes, total_budget, mid)) == total_budget:
            return sum_of_medians(citizen_votes, total_budget, mid)
        elif sum(sum_of_medians(citizen_votes, total_budget, mid)) < total_budget:
            l = mid
        else:
            r = mid
    return sum_of_medians(citizen_votes, total_budget, mid)


def sum_of_medians(citizen_votes, c, t):
    const_list = []
    ans_list = []
    for i in range(1, len(citizen_votes)):
        const_vote = c * min(1, i * t)
        const_list.append(const_vote)
    for i in range(len(citizen_votes[0])):
        temp_list = const_list.copy()
        for voter in citizen_votes:
            temp_list.append(voter[i])
        ans_list.append(statistics.median(temp_list))
    return ans_list


if __name__ == '__main__':
    citizen_votes1 = [[6, 6, 6, 6, 0, 0, 6, 0, 0], [0, 0, 6, 6, 6, 6, 0, 6, 0], [6, 6, 0, 0, 6, 6, 0, 0, 6]]
    total1 = 30
    print("Example 1:")
    print("[[6, 6, 6, 6, 0, 0, 6, 0, 0], [0, 0, 6, 6, 6, 6, 0, 6, 0], [6, 6, 0, 0, 6, 6, 0, 0, 6]]")
    print("the medians:")
    print(compute_budget(total1, citizen_votes1))

    print("Example 2:")
    print("[[100, 0, 0], [0, 0, 100]]")
    print("the medians:")
    citizen_votes2 = [[100, 0, 0], [0, 0, 100]]
    total2 = 100
    print(compute_budget(total2, citizen_votes2))
