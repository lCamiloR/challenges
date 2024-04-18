class BalenceValidation:

    opening_characters = ('(', '[', '{')
    closing_characters = (')', ']', '}')
    maped_characters = dict(zip(closing_characters, opening_characters))

    def execute(self, value:str):
        ctrl_stack = []
        for character in value:

            if character in self.opening_characters:
                ctrl_stack.append(character)
            elif character in self.closing_characters:

                if len(ctrl_stack) == 0:
                    return False
                
                if self.maped_characters[character] == ctrl_stack[-1]:
                    ctrl_stack.pop()

        return True if len(ctrl_stack) == 0 else False


if __name__ == '__main__':
    print(BalenceValidation().execute('{[Lorem]{()Ipsum}}'))