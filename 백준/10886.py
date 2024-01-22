N = int(input())

cute_count = 0
not_cute_count = 0

for i in range(N):
    cute_not_cute = int(input())
    if cute_not_cute == 1:
        cute_count += 1
    else:
        not_cute_count += 1

if cute_count > not_cute_count:
    print('Junhee is cute!')

else:
    print('Junhee is not cute!')