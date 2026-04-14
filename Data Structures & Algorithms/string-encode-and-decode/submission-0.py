class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            length = len(word)
            result+=f'{length}#{word}'
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        my_list: List[str] = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:length+j+1]
            my_list.append(word)
            i = length+j+1
        return my_list
