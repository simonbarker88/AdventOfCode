import re

def main():

    text_file = 'H:\AdventOfCode\Day5.txt'

    with open(text_file,'r') as f:
        lines = [re.findall(r'(\d*),(\d*)', x) for x in f.readlines()]
        lines = [[(int(x), int(y)) for x, y in coords] for coords in lines]

    coordinates_dict = {}
    for line in lines:
        current_x, current_y = line[0]
        end_x, end_y = line[1]
        initial_x = current_x 

        #Horiontal
        if current_y == end_y:

            while True:
                coordinates = (current_x, current_y)
                if coordinates_dict.get(coordinates, '.') == '.':
                    coordinates_dict[coordinates] = 1
                else:
                    coordinates_dict[coordinates] += 1

                if current_x == end_x:
                    break

                current_x += 1 if current_x < end_x else -1
        #Vertical
        elif initial_x == end_x:

            while True:
                coordinates = (current_x, current_y)
                if coordinates_dict.get(coordinates, '.') == '.':
                    coordinates_dict[coordinates] = 1
                else:
                    coordinates_dict[coordinates] += 1

                if current_y == end_y:
                    break

                current_y += 1 if current_y < end_y else -1
        #Diagonal
        else:
            while True:
                coordinates = (current_x, current_y)
                if coordinates_dict.get(coordinates, '.') == '.':
                    coordinates_dict[coordinates] = 1
                else:
                    coordinates_dict[coordinates] += 1

                if current_x == end_x:
                    break

                current_x += 1 if current_x < end_x else -1
                current_y += 1 if current_y < end_y else -1
        
    dangerous_areas = sum([1 if x > 1 else 0 for x in coordinates_dict.values()])

    print("Number of dangerous areas:", dangerous_areas)

if __name__ == '__main__':
    main()