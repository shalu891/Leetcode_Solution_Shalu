class Solution(object):
    def numMatchingSubseq(self, s, words):
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        count = 0
        
        for char in s:
            current_waiting = waiting[char]
            waiting[char] = []
            
            for it in current_waiting:
                next_char = next(it, None)
                if next_char is None:
                    count += 1
                else:
                    waiting[next_char].append(it)
                    
        return count
        