class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            temp = "" 
            temp += s
            temp += "#ENDHERE#"
            final += temp

        return final

    def decode(self, s: str) -> List[str]:
        final = s.split("#ENDHERE#")
        final.pop(len(final)-1)
        return final
