# Have the test.txt file in the same directory as this .py file

# r = read text      ]
# w = write text     ]  MODES
# a = append text    ]

try:
    with open("test.txt", "r") as test_file:
        lines_read = test_file.read() # for getting all the text as one string
        lines_readlines = test_file.readlines() # for returning lines as separate strings
        print(lines_read)
        print(lines_readlines)
except Exception as e:
    print(str(e))