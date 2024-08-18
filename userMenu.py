from matplotlib import pyplot
import AxisSelector


def menu():
    x = AxisSelector.getXAxis()
    y = None
    while True:
        try:
            choice = int(input("Please Enter your choice of Y Axis from Below Options"
                               "\n(1)Sepal Length"
                               "\n(2)Sepal Width"
                               "\n(3)Petal Length"
                               "\n(4)Petal Width\n"))
        except:
            print("Something went wrong with input")
        else:
            if choice == 1:
                y = AxisSelector.getSepalLength()
            elif choice == 2:
                y = AxisSelector.getSepalWidth()
            elif choice == 3:
                y = AxisSelector.getPetalLength()
            elif choice == 4:
                y = AxisSelector.getPetalWidth()
            else:
                print("Invalid Choice")
            break
    pyplot.scatter(x,y)
    name=input("Please Enter the name by which you wish to save the graph: \n")
    pyplot.savefig(f"{name}.png")