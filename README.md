import drs_header_files
choice = chr
3 roll = int
dice = int
min = int
max = int
dice_choice = chr
spectrum = int
result = ""
dice = [1, 2, 3, 4, 5, 6]
min = 1
max = 50
spectrum = range(min, max)
choice = input("Do you want to roll the dice ? (y/n): ")
while choice == 'y':
   dice_choice = input("You want an average dice (a) or customized dice (c) ? (a/c): ")
   if dice_choice == 'a':
        result = drs_header_files.dice_func()
        print(result)
    else:
        result = drs_header_files.spectrum_func()
        print(result)
    choice = input("Do you want to roll the dice ? (y/n): ")
