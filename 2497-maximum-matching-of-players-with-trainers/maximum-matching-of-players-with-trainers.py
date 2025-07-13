class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n1 = len(players)
        n2 = len(trainers)
        players.sort()
        trainers.sort()
        i=0
        j=0
        ans =0
        while i<n1 and j<n2:
            if trainers[j]>=players[i]:
                ans+=1
                i+=1
                j+=1
            else:
                j+=1
        return ans
            
