#TODO TC2 TLE

def h_index(n, citations):
    citations = list(citations)
    ans = [1]
    for paper_index in range(2, n+1):
        next = ans[-1]+1
        res = next if sum(map(lambda x: x >= next, citations[:paper_index])) >= next else ans[-1]
        ans.append(res)
    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        citations = map(int, input().split()) # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
