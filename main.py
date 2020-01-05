from built_in import sequence
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:

    try:
        select_mode = int(input('Please choose an option [1] [2]:\n\t1.Image sequence to video\n\t2.Video to image sequence\n\t> '))
        break

    except ValueError:
        print('\nPlease provide a number between 1-2\n')
        continue


if select_mode == 1:
    path = input('\nEnter folder path: ')
    fps = int(input('Frame rate: '))
    out_file = input('Enter an output filename including video format [MP4] [AVI] (Enter to default): ')

    encode = sequence.ImagesSequence()
    total_time = encode.img_sequence(path, fps, out_file)

elif select_mode == 2:
    path = input('\nEnter video path:  ')
    print('Processing...')
    total_time = sequence.video_sequence('vi.mp4')

print('\nVideo saved successfully!\nTotal time: %d seconds' % total_time)
