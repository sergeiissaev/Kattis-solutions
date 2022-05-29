class Coconut:
    def __init__(self, game_settings):
        self.syllables, self.players = game_settings
        self.overflow = (self.players * 2)

    def _index_after_step(self, current_index: int, steps: int):
        '''Take care of overflow'''
        return (current_index + steps) % self.overflow

    def _take_step(self, status_list: list, current_index: int):
        '''Take steps until you are at a non-zero valued index'''
        for steps in range(1, len(status_list)):
            if status_list[self._index_after_step(current_index=current_index, steps=steps)] != 0:
                return self._index_after_step(current_index=current_index, steps=steps)

    def _decrement_status(self, status_list: list, current_index: int):
        '''Split 3 into two 2s, otherwise decrement by 1'''
        if status_list[current_index] != 3:
            status_list[current_index] -= 1
        else:
            status_list[current_index] -= 1
            status_list[current_index+1] = 2
        return status_list

    def find_winner(self):
        ''' Simulate the game using an array '''
        status_list = [3 if x % 2 == 0 else 0 for x in range(self.players * 2)]
        current_index = 0
        while len([i for i, element in enumerate(status_list) if element!=0]) > 1:
            steps_to_go = self.syllables - 1
            if status_list[current_index] == 0 or status_list[current_index] == 1:
                current_index = self._take_step(status_list=status_list, current_index=current_index)
            while steps_to_go > 0:
                current_index = self._take_step(status_list=status_list, current_index=current_index)
                steps_to_go -= 1
            status_list = self._decrement_status(status_list=status_list, current_index=current_index)
        print((status_list.index([element for i, element in enumerate(status_list) if element!=0][0]) // 2) + 1)


if __name__ == "__main__":
    coconut = Coconut(game_settings=list(map(int, input().rstrip().split())))
    coconut.find_winner()
