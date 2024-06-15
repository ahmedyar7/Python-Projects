import numpy as np
import matplotlib.pyplot as plt


class TrignometricFunctionPlot:
    def __init__(self) -> None:
        self.x_axis = np.linspace(
            start=0, stop=np.pi * 2, num=100
        )  # Evenly spaces values from 0 - 2pi

    def sin_function(self):
        """This function would plot the sin graph"""

        y_axis = np.sin(self.x_axis)  # Compute the sin values

        plt.title("Sin Function")
        plt.xlabel("X")
        plt.ylabel("y")

        plt.plot(self.x_axis, y_axis)
        plt.show()

    def cos_funtion(self):
        """This would plot the cos function"""

        y_axis = np.cos(self.x_axis)

        plt.title("Cos Function")
        plt.xlabel("X")
        plt.ylabel("y")

        plt.plot(self.x_axis, y_axis)
        plt.show()

    def tan_funtion(self):
        """This would plot the tan function"""

        y_axis = np.tan(self.x_axis)
        y_axis = np.clip(y_axis, -10, 10)

        plt.title("Tan Function")
        plt.xlabel("X")
        plt.ylabel("y")

        plt.plot(self.x_axis, y_axis)
        plt.show()

    def cosh_funtion(self):
        """This would plot the sec function"""

        y_axis = np.cosh(self.x_axis)

        plt.title("Cos Function")
        plt.plot(self.x_axis, y_axis)

        plt.show()
