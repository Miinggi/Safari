from animal import Animal
import os

def print_TODO(todo):
    print(f'<<<NOT IMPLEMENTED: {todo}>>>')

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):

        #self.zebras = [Animal(0,0) for _ in range(num_zebras)]
        #self.lions = [Animal(0,0) for _ in range(num_lions)]
        self.timestep = 0
        print("welcome to AIE safari")
        print(f'\nworld size = {world_size}')
        print(f'\nnum zebras = {num_zebras}')
        print(f'\nnum lions = {num_lions}')
        print(f'\n')

        cols = world_size
        cell_size = 10
        self.grid = []
        # arma 5 listas blancas
        for row in range(cols):
            self.grid.append([])
            # en las que en cada lista tienen 5 espacios blancos de tamano 3.
            for _ in range(cols):
                #se puede entender como grid[row], como la parte row, lista 1,2,3,y asi
                self.grid[row].append(" " * cell_size)
        
        #para el 1234 de arriba
        coordenates = [f'{coord+1}' for coord in range(len(self.grid))]
        print('   ' + ((int(cell_size/2))*' ') + (cell_size*' ').join(coordenates))
        # por la cantidad de cuadros por - te da cierta cantidad pero es insuficiente. Lo llenas con '--'
        print('   ' + "-" * ((cell_size + 1) * world_size - 1) + '--')
        for row_idx, row in enumerate(self.grid):
            print(f"{coordenates[row_idx]}  |" + "|".join(row) + "|")
            print('   ' + "-" * ((cell_size + 1) * world_size - 1) + '--')

            
        #print(grid)



    def display(self):

        print(f'time step: {self.timestep}')

        for animal in self.zebras:
            self.grid[animal.y][animal.x] = 'Z'
        for animal in self.lions:
            self.grid[animal.y][animal.x] = 'L'
        for line in self.grid:
            print(line)


        key = input('press [q] to quit')
        if key == 'q':
            exit()

    def step_move(self):
        print_TODO('step_move()')
        for zebra in self.zebras:
            print_TODO('get empty neighbor')
            direction = 'left'
            zebra.move(direction)
        for lion in self.lions:
            print_TODO('get empty neighbor')
            print_TODO('move to zebra if found, else move to empty')
            print_TODO('get empty neighbor')
            direction = 'left'
            lion.move(direction)

    def step_breed(self):
        print_TODO('step_breed()')
        for animal in self.zebras + self.lions:
            print_TODO('get empty neighbor')
            x, y = 0, 0
            animal.breed(x,y)

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()

if __name__ == '__main__':
    safari = CircleOfLife(5, 5, 2)
    safari.display()
    # safari.step_move()
    # safari.step_breed()
    #safari.run(2)