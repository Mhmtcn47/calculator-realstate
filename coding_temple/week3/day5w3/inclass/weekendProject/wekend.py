# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will calculate the Return on Investment(ROI) for a rental property. Include a test file and implement at least a few basic tests.

# This project will be completed individually, though you can feel free to share ideas with your fellow students.

# Once completed, commit the project to github and submit the link to this assignment.
#  Ideas:
# create dictioneries about each class
# getting total income
# add them up
# divide them by cash flow
# use OOP
# include a test file and implement at least a few basic test
investment = 40000
expenses =700
rent =1000
def roi (investment,expenses, rent):
    netProfit = investment * 12 - expenses
    roi = (netProfit/investment)*100
    print(roi)
roi(investment,expenses,rent)
