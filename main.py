# from graphic import Draw
from turtle import Turtle

timmy = Turtle()

# start = True
# while start:
choice = int(input(
    "Press\n1 for Saquare\n2 for printing all shapes\n3 for Generating Random Walk\n4 for Spirograph\n5 for HirstPainting.\n"))

if choice == 1:
    from graphic import Draw
    display = Draw(200, 0, 0, 0, 0)
    display.square(timmy)

elif choice == 2:
    from graphic import Draw
    display = Draw(200, 0, 0, 0, 0)
    display.allsahpes(timmy)

elif choice == 3:
    steps = int(input("Enter number of steps. "))
    from graphic import Draw
    display = Draw(steps, 0, 0, 0, 0)
    display.randomwalk(timmy)

elif choice == 4:
    from graphic import Draw
    display = Draw(200, 0, 0, 0, 0)
    display.spirograph(timmy)

elif choice == 5:
    x = int(input("Enter X co-ordinate. "))
    y = int(input("Enter Y co-ordinate. "))
    r = int(input("Enter number of Rows. "))
    c = int(input("Enter number of Columns. "))
    from graphic import Draw
    display = Draw(200, x, y, r, c)
    display.hirstpainting(timmy)

else:
    print("Invalid Input\n")



