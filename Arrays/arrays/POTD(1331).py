class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        # Store (value, original index)
        pairs = sorted((value, index) for index, value in enumerate(arr))
        
        result = [0] * n
        rank = 0
        prev = None
        
        for value, index in pairs:
            # Increase rank only for a new value
            if prev is None or value != prev:
                rank += 1
                prev = value
            
            result[index] = rank
        
        return result