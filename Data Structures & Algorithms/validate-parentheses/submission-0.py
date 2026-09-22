"""
Understand: valid parenthesis
input: as tring s consisting of chars '(', ')', '{', '}', and '[', ']' 
string s is valid if and only if:
- every open bracket is closed by the same type of close bracket
- open brackets are closed in the correct order
- every close bracket has a corresponding open bracket of the same type
Output: true if valid and false otherwise
edge cases:
- string is empty -> true
- there's one bracket -> false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in closeToOpen: #only keys of our dict get checked - closing brackets
                if stack and stack[-1] == closeToOpen[c]: # looks up correct matching open bracket to whatever close bracket c is
# once we find that the closing bracket c matches the open bracket sitting on top of the stack (stack[-1] == closeToOpen[c]), that pair is now fully resolved — the open bracket has been "closed," so it no longer needs to stay in the stack waiting for a match. pop() removes it, so the next open bracket down becomes the new "most recent unclosed bracket."
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # if it's not a closing bracket, add it to stack
        
        return True if not stack else False
        # if not stack: #stack is empty
            #return True
        #else:
            #return False -> if we had s = ((
                    



        