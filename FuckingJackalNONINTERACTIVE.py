import math, argparse
from PIL import Image
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', type=str, help='A filename to open.')
parser.add_argument('-r', '--result', type=str, help='A filename to save to.')
parser.add_argument('-q', '--quality', type=int, help='Quality, from 1 (worst) to 95 (best, BUT NOT RECOMMENDED)')
args = parser.parse_args()
img = Image.open(args.source)
img = img.convert('RGB')
img.save('{}'.format(args.result), quality=args.quality)
