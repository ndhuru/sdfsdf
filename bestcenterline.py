def drawCenterLine(image, lines):
    # Prevents program from crashing if no lines detected
    if lines is not None:
        # Variables needed to find the centerline
        slope_arr = []
        lines_list = []
        for line in lines:
            # Creates array of lines
            x1, y1, x2, y2 = line[0]
            lines_list.append(line[0])

            # Calculates the slopes of the lines
            slope = 0
            if x2 - x1 != 0:
                slope = (y2 - y1) / (x2 - x1)
            slope_arr.append(slope)

        # Loops through the slope array to calculate the centerline
        for i in range(len(slope_arr)):
            for j in range(len(slope_arr)):
                x1, y1, x2, y2 = lines_list[i]
                x3, y3, x4, y4 = lines_list[j]
                # Calculates and displays the centerline
                cv.line(image, ((x1 + x3) // 2, (y1 + y3) // 2), ((x2 + x4) // 2, (y2 + y4) // 2), (251, 13, 136), 10)
