class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()

        expected = defaultdict(int)
        for h in hand:
            if h in expected:
                expected[h] -= 1
                if expected[h] == 0:
                    expected.pop(h)
            else:
                for i in range(1, groupSize):
                    expected[h+i] += 1
        
        return (len(expected) == 0)

        

