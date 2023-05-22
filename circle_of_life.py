from animal import Empty, Zebra, Lion  
import random

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):
        
        self.timestep = 0
        self.world = world_size
        self.zebras = []
        self.lions = []

        # Randomly spawn zebras
        available_coordinates = [(x, y) for x in range(self.world) for y in range(self.world)]
        random.shuffle(available_coordinates)
        for _ in range(num_zebras):
            x, y = available_coordinates.pop()
            self.zebras.append(Zebra(x, y))

        # Randomly spawn lions
        available_coordinates = [(x, y) for x in range(self.world) for y in range(self.world)]
        random.shuffle(available_coordinates)
        for _ in range(num_lions):
            x, y = available_coordinates.pop()
            self.lions.append(Lion(x, y))

        print(f'\n')
        print("welcome to AIE safari")
        print(f'\nworld size = {world_size}')
        print(f'\nnum zebras = {num_zebras}')
        print(f'\nnum lions = {num_lions}')
        print(f'\n')
    
    def display(self):
        
        self.update_grid()
        cell_size = 5
        #para el 1234 de arriba
        coordenates = [f'{coord}' for coord in range(len(self.grid))]
        print(' ',end=' ')
        for coord in coordenates:
            if int(coord) < 10:
                print('    ' + coord, end=' ')
            else:
                print('   ' + coord, end=' ')
        print()

        # por la cantidad de cuadros por - te da cierta cantidad pero es insuficiente. Lo llenas con '--'
        print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
        for row_idx, row in enumerate(self.grid):
            buffer = [str(animal) for animal in row]
            if row_idx < 10:
                print(f"{coordenates[row_idx]}  |" + "|".join(buffer) + "|")
                print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')
            else:
                print(f"{coordenates[row_idx]} |" + "|".join(buffer) + "|")
                print('   ' + "-" * ((cell_size + 1) * self.world - 1) + '--')

        print(f'time step: {self.timestep}')

        #for line in self.grid:
            #print(line)

        key = input('press [q] to quit')
        if key == 'q':
            exit()

    def update_grid(self):

        self.grid = []
        # arma 5 listas blancas
        for row in range(self.world):
            self.grid.append([])
            # en las que en cada lista tienen 5 espacios blancos de tamano 3.
            for col in range(self.world):
                #se puede entender como grid[row], como la parte row, lista 1,2,3,y asi
                if any(animal.x == col and animal.y == row for animal in self.zebras):
                    self.grid[row].append(Zebra(col, row))
                elif any(animal.x == col and animal.y == row for animal in self.lions):
                    self.grid[row].append(Lion(col, row))
                else:
                    self.grid[row].append(Empty(col, row))

    def step_move(self):

        animals = [animal for row in self.grid for animal in row
                   if not isinstance(animal, Empty)]
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)
                
    def step_breed(self):
        for animal in self.zebras + self.lions:
            x, y = 0, 0
            animal.breed(x,y)

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            #self.step_breed()
            #self.display()

if __name__ == '__main__':

    safari = CircleOfLife(20, 20, 20)
    safari.display()
    # safari.step_move()
    # safari.step_breed()
    safari.run(2)