from typing import List


class UniqueMorseCodeWords:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codeMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({''.join(codeMap[ord(c) - ord('a')] for c in w) for w in words})


    def uniqueMorseRepresentations2(self, words: List[str]) -> int:
        codeMap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for w in words:
            code = ""
            for c in w:
                code = code + codeMap[ord(c) - ord('a')]
            seen.add(code)
        return len(seen)