# CSC 122
# Tests for Lab3
# Color Mixer programm

import os.path
import sys
from Lab3 import main
from tud_tests import *

def test_Lab3():
    
    try:
        exists = os.path.exists("Lab3.py")
        assert exists == True
    except:
        sys.exit()
    
    # Test 1
    set_keyboard_input(["red","Green"])
    main()
    output = get_display_output()

    assert output == [
            "Enter the first primary color to mix (red, green, or blue): ",
            "Enter the second primary color to mix (red, green, or blue): ",
            "The secondary color you mixed is yellow.",
            "Bye!"
        ]
    
    # Test 2
    set_keyboard_input(["Blue","RED"])
    main()
    output = get_display_output()

    assert output == [
            "Enter the first primary color to mix (red, green, or blue): ",
            "Enter the second primary color to mix (red, green, or blue): ",
            "The secondary color you mixed is magenta.",
            "Bye!"
        ]

    # Test 3
    set_keyboard_input(["GrEEn","bLue"])
    main()
    output = get_display_output()

    assert output == [
            "Enter the first primary color to mix (red, green, or blue): ",
            "Enter the second primary color to mix (red, green, or blue): ",
            "The secondary color you mixed is cyan.",
            "Bye!"
        ]

    # Test 4
    set_keyboard_input(["Blue","PINK"])
    main()
    output = get_display_output()

    assert output == [
            "Enter the first primary color to mix (red, green, or blue): ",
            "Enter the second primary color to mix (red, green, or blue): ",
            "The seconday color you mixed is invalid!",
            "Bye!"
        ]
