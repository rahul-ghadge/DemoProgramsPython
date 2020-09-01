

class balanced_parenthesis_check(object):

    def is_balanced(self, str):

        stack = []
        opening_parenthesis = ['(', '{', '[']

        matches = set((   ('(', ')'),  ('{', '}'),  ('[',']')   ))

        for s in str:
            if s in opening_parenthesis:
                stack.append(s)

            else:
                if len(stack) == 0:
                    return False

                last_open = stack.pop()

                if (last_open, s) not in matches:
                    return False

        return len(stack) == 0



balanced = balanced_parenthesis_check()

print('{{(([[{}]]))}} :: ', balanced.is_balanced("{{(([[{}]]))}}"))
print('{([{}])} :: ', balanced.is_balanced("{([{}])}"))
print('{(} :: ', balanced.is_balanced("{(}"))



# -------------------
# Output
# -------------------
# {{(([[{}]]))}} ::  True
# {([{}])} ::  True
# {(} ::  False
