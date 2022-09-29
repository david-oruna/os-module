import os

while True:

        try:
            def makedir(self, name):
                self.name = name
                'Hi this is the directory creator'
                x = input('Enter name of directory: ')
                if len(x) < 5:
                    print('Name has to be larger than 5 char')
                    continue

                else:
                    y = input('Enter dir: ')
                    os.mkdir(y)
                    print(f'{x} has been cratedd')
                
                    
        except ValueError:
            print(ValueError)




