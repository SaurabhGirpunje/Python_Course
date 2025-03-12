# Escape Sequence Table in Python

# Escape Sequence    Meaning                        Example                               Output
# --------------------------------------------------------------------------------------------------
# \n                 Newline (Next line)            print("Hello\nWorld")                 Hello
#                                                                                         World
# \t                 Tab (Adds a tab space)         print("Hello\tWorld")                 Hello    World
# \\                 Backslash (\)                  print("C:\\Users\\Name")              C:\Users\Name
# \'                 Single Quote (')               print('It\'s Python')                 It's Python
# \"                 Double Quote (")               print("He said, \"Hello\"")           He said, "Hello"
# \r                 Carriage Return                print("Hello\rWorld")                 Worldo
# \b                 Backspace (Deletes a char)     print("Hello\b World")                Hell World
# \f                 Form Feed (Page Break)         print("Hello\fWorld")                 Hello (new page) World
# \v                 Vertical Tab                   print("Hello\vWorld")                 Hello ⬇ World
# \ooo               Octal Value                    print("\110\145\154\154\157")         Hello
# \xhh               Hex Value                      print("\x48\x65\x6C\x6C\x6F")         Hello



lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(lorem_ipsum)
