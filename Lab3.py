# CSC 122
# Lab3
# Color Mixer
# by Brian McBride

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""
def main():
    #collecting primary colors
    color1 = input("Enter the first primary color to mix (red, green, or blue): ")
    color2 = input("Enter the second primary color to mix (red, green, or blue): ")

    # color test decision
    if (color1.lower() == "red" and color2.lower() == "green" or color1.lower() == "green" and color2.lower() == "red"):
        print("The secondary color you mixed is yellow.")
    elif (color1.lower() == "red" and color2.lower() == "blue" or color1.lower() == "blue" and color2.lower() == "red"):
        print("The secondary color you mixed is magenta.")
    elif (color1.lower() == "green" and color2.lower() == "blue" or color1.lower() == "blue" and color2.lower() == "green"):
        print("The secondary color you mixed is cyan.")
    else:
        print("The seconday color you mixed is invalid!")

    print("Bye!")

if __name__ == "__main__":
    main()   
