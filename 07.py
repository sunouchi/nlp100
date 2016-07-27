import sys

if __name__ == '__main__':
   x = int(sys.argv[1])
   y = str(sys.argv[2])
   z = float(sys.argv[3])
   print('{x}時の{y}は{z}'.format(x=x, y=y, z=z))
