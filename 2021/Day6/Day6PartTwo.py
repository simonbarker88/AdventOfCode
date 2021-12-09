def main():

    text_file = 'H:\AdventOfCode\Day6.txt'

    with open(text_file,'r') as f:
        lines = [int(x) for x in f.readlines()[0].split(',')]

    #OOM error for list method(!!) for 256 days :(
    
    state_dict =  {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in lines:
        state_dict[fish] += 1

    for day in range(256):
        new_fish_state_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        
        for key in state_dict.keys():
            new_fish_state_dict[key - 1] = state_dict[key]

        for key in new_fish_state_dict:
            if key == -1:
                new_fish_state_dict[8] = new_fish_state_dict[-1]
                new_fish_state_dict[6] += new_fish_state_dict[-1]

        state_dict = new_fish_state_dict
        del state_dict[-1]

    print('Number of lanternfish: ',sum(state_dict.values()))

if __name__ == '__main__':
    main()
