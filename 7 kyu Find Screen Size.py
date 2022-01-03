def find_screen_height(width, ratio):
    return f"{width}x{width * int(ratio.split(':')[1]) // int(ratio.split(':')[0])}"


print(find_screen_height(1024, "4:3"), "1024x768")
print(find_screen_height(1280, "16:9"), "1280x720")
print(find_screen_height(3840, "32:9"), "3840x1080")
