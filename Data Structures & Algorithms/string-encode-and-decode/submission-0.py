class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        encoded = s
        i = 0
        j = i
        while i < len(encoded):
            if encoded[i] == "#":
                length = encoded[j:i]
                end_idx = i + int(length) 
                decoded.append(encoded[i+1: end_idx + 1])
                j = end_idx + 1
                i = j
            else:
                i += 1
        
        return decoded


