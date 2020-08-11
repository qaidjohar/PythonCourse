import termcolor as tm

# help(termcolor)

text = tm.colored('Hello Python!!', color='red', on_color='on_green')
print(text)

# colored(text, color=None, on_color=None, attrs=None)
#         Colorize text.
        
#         Available text colors:
#             red, green, yellow, blue, magenta, cyan, white.
        
#         Available text highlights:
#             on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
        
#         Available attributes:
#             bold, dark, underline, blink, reverse, concealed.

#         Example:
#             colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
#             colored('Hello, World!', 'green')