import os, random
try:
    from PIL import Image
except ImportError:
    print('No PIL installed! Install PIL (pillow) and try again.')
    input()
    quit()
srcFN = input('Enter a filename to open: ')
resFN = input('Enter a filename (WITHOUT extension) to save to: ')
ext = ['.jpg', '.png', '.bmp']
if os.path.splitext(srcFN)[1] not in ext:
    for name in os.listdir('.'):
        if os.path.splitext(name)[0] == srcFN:
            srcFN = srcFN + os.path.splitext(name)[1]
try:
    qual = int(input('Enter a quality, from 1 (worst) to 9 (best) or "0" to set a random quality: '))
    qual = qual % 9 + 1
except TypeError:
    print('Integer numbers only! Terminating.')
    quit()
if qual == 0: qual=random.randint(1,9)
try:
    img = Image.open(srcFN)
    img = img.convert('RGB')
    img.save('{}.jpg'.format(resFN), quality=qual)
    print('Done! Press Enter to exit.')
    input()
except IOError:
    print('An error occurred. Press Enter to exit.')
    input()
