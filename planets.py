def weight_on_planets():
   weight = float(input('What do you weigh on earth? '))
   WoM = weight * 0.38
   WoJ = weight * 2.34
   print('\nOn Mars you would weigh {:0.2f} pounds.\n'
         'On Jupiter you would weigh {:0.2f} pounds.'.format(WoM, WoJ))

if __name__ == '__main__':
   weight_on_planets()