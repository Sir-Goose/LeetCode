class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0] * k
        
        users = {}
        for log in logs:
            if log[0] in users:
                users[log[0]] = users[log[0]] + [log[1]]
            else:
                users[log[0]] = [log[1]]


        for user in users:
            index = len(set(users[user]))
            answer[index - 1] += 1

        return answer

