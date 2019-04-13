import sys
import tqdm
from utils import convert_single_file

if __name__ == "__main__":
    print("PDF2IMG v1.0.0")
    if len(sys.argv) == 5:
        source = sys.argv[1]
        destination = sys.argv[2]
        page_start = sys.argv[3]
        page_end = sys.argv[4]

        filenames = os.listdir('source')

        for filename in tqdm(filenames):
            print("Converting: " + filename)
            try:
                convert_single_file(filename, destination, page_start, page_end)
                print("Converted: " + filename)
            except Exception as err:
                print("Failed to convert: " + filename)
                print("Error: " + str(err))
        
        print("Done!")

