N = int(input())

score_list = list(map(int, input().split()))
max_score = max(score_list)
new_score_list = [(score/max_score)*100 for score in score_list]

print(sum(new_score_list)/N)