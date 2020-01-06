from built_in import sequence, vars
import os
import colorama
import time

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    print(vars.title)

    try:
        select_mode = int(
            input(
                f'\nPlease choose an option [1] [2] [3]:\n\t1.Image sequence to video\n\t2.Video to image sequence\n\t3.Help\n\t>{colorama.Fore.RED} '))
        print(colorama.Fore.WHITE)
        assert 0 < select_mode <= 3

    except (ValueError, AssertionError):
        print(colorama.Fore.RED + '\nPlease provide a number between 1-3\n')
        print(colorama.Fore.WHITE)
        continue

    os.system('cls' if os.name == 'nt' else 'clear')

    if select_mode == 1:
        print(vars.title + colorama.Fore.GREEN + '\n1> Image sequence to image' + colorama.Fore.WHITE)
        try:
            path = input('\nEnter folder path: ')
            fps = int(input('Frame rate: '))
            out_file = input('Enter an output filename including video format [MP4] [AVI] (Enter to default): ')

        except:
            print(colorama.Fore.RED + '\nSomething went wrong, returning... \n' + colorama.Fore.WHITE)
            time.sleep(1)
            continue

        encode = sequence.ImagesSequence()
        total_time = encode.img_sequence(path, fps, out_file)

    elif select_mode == 2:
        print(vars.title + colorama.Fore.GREEN + '\n2> Video to image sequence' + colorama.Fore.WHITE)
        path = input('\nEnter video path:  ')
        print('Processing...')
        total_time = sequence.video_sequence('vi.mp4')

    elif select_mode == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(vars.title)
        print(vars.help)
        back = input('\nEnter to return: ')
        continue

print('\nVideo saved successfully!\nTotal time: %d seconds' % total_time)
