def solution(heights):
    answer = [0 for x in range(len(heights))]
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                answer[i] += j+1
                break
    return answer