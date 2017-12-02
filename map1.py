class Map_1():
    def __init__(self):
        #the info about map_1
        #self.max_blocks_number = 30
        self.block_info = []
        self.basis_side = 40

        '''The Map's (x, y) information'''
        #col A
        self.block_info.append((self.basis_side * 1, self.basis_side * 0)) 
        self.block_info.append((self.basis_side * 3, self.basis_side * 0))
        self.block_info.append((self.basis_side * 12, self.basis_side * 0))
        #col B
        self.block_info.append((self.basis_side * 0, self.basis_side * 1))
        self.block_info.append((self.basis_side * 1, self.basis_side * 1))
        self.block_info.append((self.basis_side * 3, self.basis_side * 1))
        self.block_info.append((self.basis_side * 4, self.basis_side * 1))
        self.block_info.append((self.basis_side * 11, self.basis_side * 1))
        self.block_info.append((self.basis_side * 12, self.basis_side * 1))
        #col C
        self.block_info.append((self.basis_side * 3, self.basis_side * 2))
        self.block_info.append((self.basis_side * 12, self.basis_side * 2))
        #col D
        self.block_info.append((self.basis_side * 0, self.basis_side * 3))
        self.block_info.append((self.basis_side * 1, self.basis_side * 3))
        self.block_info.append((self.basis_side * 2, self.basis_side * 3))
        self.block_info.append((self.basis_side * 3, self.basis_side * 3))
        self.block_info.append((self.basis_side * 4, self.basis_side * 3))
        self.block_info.append((self.basis_side * 5, self.basis_side * 3))
        self.block_info.append((self.basis_side * 6, self.basis_side * 3))
        self.block_info.append((self.basis_side * 7, self.basis_side * 3))
        self.block_info.append((self.basis_side * 8, self.basis_side * 3))
        self.block_info.append((self.basis_side * 9, self.basis_side * 3))
        self.block_info.append((self.basis_side * 10, self.basis_side * 3))
        self.block_info.append((self.basis_side * 11, self.basis_side * 3))
        self.block_info.append((self.basis_side * 12, self.basis_side * 3))
        #col E
        self.block_info.append((self.basis_side * 3, self.basis_side * 4))
        self.block_info.append((self.basis_side * 7, self.basis_side * 4))
        self.block_info.append((self.basis_side * 12, self.basis_side * 4))
        #col F
        self.block_info.append((self.basis_side * 3, self.basis_side * 5))
        self.block_info.append((self.basis_side * 7, self.basis_side * 5))
        self.block_info.append((self.basis_side * 12, self.basis_side * 5))
        #col G
        self.block_info.append((self.basis_side * 3, self.basis_side * 6))
        self.block_info.append((self.basis_side * 7, self.basis_side * 6))
        self.block_info.append((self.basis_side * 12, self.basis_side * 6))
        #col H
        self.block_info.append((self.basis_side * 3, self.basis_side * 7))
        self.block_info.append((self.basis_side * 7, self.basis_side * 7))
        self.block_info.append((self.basis_side * 8, self.basis_side * 7))
        self.block_info.append((self.basis_side * 9, self.basis_side * 7))
        self.block_info.append((self.basis_side * 10, self.basis_side * 7))
        self.block_info.append((self.basis_side * 11, self.basis_side * 7))
        self.block_info.append((self.basis_side * 12, self.basis_side * 7))
        #col I
        self.block_info.append((self.basis_side * 3, self.basis_side * 8))
        self.block_info.append((self.basis_side * 4, self.basis_side * 8))
        self.block_info.append((self.basis_side * 5, self.basis_side * 8))
        self.block_info.append((self.basis_side * 6, self.basis_side * 8))
        self.block_info.append((self.basis_side * 7, self.basis_side * 8))
        self.block_info.append((self.basis_side * 8, self.basis_side * 8))
        self.block_info.append((self.basis_side * 12, self.basis_side * 8))
        #col J
        self.block_info.append((self.basis_side * 3, self.basis_side * 9))
        self.block_info.append((self.basis_side * 8, self.basis_side * 9))
        self.block_info.append((self.basis_side * 12, self.basis_side * 9))
        #col K
        self.block_info.append((self.basis_side * 3, self.basis_side * 10))
        self.block_info.append((self.basis_side * 8, self.basis_side * 10))
        self.block_info.append((self.basis_side * 12, self.basis_side * 10))
        #col L
        self.block_info.append((self.basis_side * 3, self.basis_side * 11))
        self.block_info.append((self.basis_side * 8, self.basis_side * 11))
        self.block_info.append((self.basis_side * 12, self.basis_side * 11))
        #col M
        self.block_info.append((self.basis_side * 3, self.basis_side * 12))
        self.block_info.append((self.basis_side * 4, self.basis_side * 12))
        self.block_info.append((self.basis_side * 5, self.basis_side * 12))
        self.block_info.append((self.basis_side * 6, self.basis_side * 12))
        self.block_info.append((self.basis_side * 7, self.basis_side * 12))
        self.block_info.append((self.basis_side * 8, self.basis_side * 12))
        self.block_info.append((self.basis_side * 9, self.basis_side * 12))
        self.block_info.append((self.basis_side * 10, self.basis_side * 12))
        self.block_info.append((self.basis_side * 11, self.basis_side * 12))
        self.block_info.append((self.basis_side * 12, self.basis_side * 12))
        self.block_info.append((self.basis_side * 13, self.basis_side * 12))
        self.block_info.append((self.basis_side * 14, self.basis_side * 12))
        self.block_info.append((self.basis_side * 15, self.basis_side * 12))
        #col N
        self.block_info.append((self.basis_side * 3, self.basis_side * 13))
        self.block_info.append((self.basis_side * 12, self.basis_side * 13))
        #col O
        self.block_info.append((self.basis_side * 3, self.basis_side * 14))
        self.block_info.append((self.basis_side * 4, self.basis_side * 14))
        self.block_info.append((self.basis_side * 11, self.basis_side * 14))
        self.block_info.append((self.basis_side * 12, self.basis_side * 14))
        self.block_info.append((self.basis_side * 14, self.basis_side * 14))
        self.block_info.append((self.basis_side * 15, self.basis_side * 14))
        #col P
        self.block_info.append((self.basis_side * 3, self.basis_side * 15))
        self.block_info.append((self.basis_side * 12, self.basis_side * 15))
        self.block_info.append((self.basis_side * 14, self.basis_side * 15))
