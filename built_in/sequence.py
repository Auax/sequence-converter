from built_in import Encode
import cv2
import os
import time


class ImagesSequence(Encode):

    def img_sequence(self, path: str, fps: int = 30, out_filename: str = 'output.avi'):
        """
        Transform a sequence of images in the same folder to a video format.
        The sequence is ordered by following the alphabetical order.
        :param path: Current path of image sequence folder.
        :param fps: FrameRate to save the video.
        :param out_filename: Custom file name to save the video output.
        """

        # Sequence array
        img_array = []

        if not out_filename:
            out_filename = 'output.avi'

        # Get file format from filename
        file_format = '.' + out_filename.split('.')[-1].lower()

        # Check if file format is in EncodeVideoFormats
        if file_format not in self.EncodeVideoFormats.keys():
            print('File format not found!')
            file_format = '.avi'  # Change format to .avi (default)
            out_filename = out_filename + file_format  # Add file format to filename

        file_format = self.EncodeVideoFormats[file_format]  # Assign the encode format to file_format

        # Print out the video output options
        mx = int(max(len(path), len(file_format), len(out_filename))) + 10
        print(
            '\nCONFIG INFO:\n' + '-' * mx + f'\nPath: {path}\nFilename: {out_filename}\nEncode: {file_format}\nFrameRate: {fps}\n' + '-' * mx)
        input('\nPress enter to continue: ')

        start_time = time.time()

        try:
            for file in os.listdir(path):
                filename = str(os.path.join(path, file))  # Create path for every sequence image inside folder
                img = cv2.imread(filename)  # Read image file
                height, width, layers = img.shape  # Gets size of image file
                size = (width, height)
                img_array.append(img)  # Append image to final sequence to be exported

        except FileNotFoundError:
            print("Files path couldn't be found!")

        # Write video
        out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(*file_format), fps, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

        return time.time() - start_time


def video_sequence(path):
    start_time = time.time()
    os.system('mkdir OUTPUT')
    video_capture = cv2.VideoCapture(path)
    success, image = video_capture.read()
    count = 0
    while success:
        cv2.imwrite('OUTPUT\\frame%d.jpg' % (count + 1), image)
        success, image = video_capture.read()
        count += 1
    return time.time() - start_time
