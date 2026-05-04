class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            exploded = False
            while stack:
                if stack[-1] < 0 or asteroid > 0:
                    break
                else:
                    if -asteroid > stack[-1]:
                        stack.pop()
                    else:
                        if -asteroid == stack[-1]:
                            stack.pop()
                        exploded = True
                        break
            if not exploded:
                stack.append(asteroid)
        
        return stack
                
        