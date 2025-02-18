#task7 - Package Control in DevEdu
#CS4300 Zachary Donnelly

import matplotlib.pyplot as plt


#using matlab plot to test package control
def matlab():
    figure, plot = plt.subplots()
    
    plot.plot([1, 2, 3, 4])
    plot.set_ylabel("test y")
    plot.set_xlabel("test x")
    plt.show()
    
    return plot

#testing the output matlab - verifies that the output is an Axes object as well as verifying the x and y axes labels
def test_matlab():
    test_plot = matlab()
    
    assert isinstance(test_plot, plt.Axes)
    assert test_plot.get_ylabel() == "test y"
    assert test_plot.get_xlabel() == "test x"