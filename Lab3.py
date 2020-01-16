import utilities

def rotate_90_degrees(image_array, direction = 1):
#1 for clock_wise. -1 for anticlockwise

    size = len(image_array)
    output = []
    
    if direction == 1:
        for x in range(size):
            temp_list = []
            for y in range(size - 1, -1, -1):
                temp_list.append(image_array[y][x])
            output.append(temp_list)
            
    if direction == -1:
        for x in range(size - 1, -1, -1):
            temp_list = []
            for y in range(size):
                temp_list.append(image_array[y][x])
            output.append(temp_list)
    return output    
    
#return output_array

def flip_image(image_array, axis = 0):
    #axis = -1 (along x = y), 0 along y, 1 along x
    
    size = len(image_array)
    output = []
    
    #flip over y-axis
    if axis == 0:
        for x in range(size):
            temp_list = []
            for y in range(size - 1, -1, -1):
                temp_list.append(image_array[x][y])
            output.append(temp_list)
    
    #flip over x-axis
    if axis == 1:
        for x in range(size - 1, -1, -1):
            temp_list = []
            for y in range(size):
                temp_list.append(image_array[x][y])
            output.append(temp_list)
    
    #flip over line y=x 
    if axis == -1:
        for x in range(size - 1, -1, -1):
            temp_list = []
            for y in range(size - 1, -1, -1):
                temp_list.append(image_array[y][x])
            output.append(temp_list)
    return output


    #return output_array

def invert_grayscale(image_array):
   
    rows = len(image_array)
    columns = len(image_array[0])
    output = []
    
    for x in range(rows):
        temp_list = []
        for y in range(columns):
            temp_list.append(abs(image_array[x][y] - 255))
        output.append(temp_list)
    return output
            


def crop(image_array, direction, n_pixels):
    
    rows = len(image_array) 
    columns = len(image_array[0]) 
    output = []    
    
    if direction == 'left':
        for x in range(rows):
            temp_list = []
            for y in range(n_pixels, columns):
                temp_list.append(image_array[x][y])
            output.append(temp_list)  
            
    if direction == 'right':
        for x in range(rows):
            temp_list = []
            for y in range(0, columns - n_pixels):
                temp_list.append(image_array[x][y])
            output.append(temp_list)  
            
    if direction == 'up':
        for x in range(0, rows - n_pixels):
            temp_list = []
            for y in range(columns):
                temp_list.append(image_array[x][y])
            output.append(temp_list)
    if direction == 'down':
        for x in range(n_pixels, rows):
            temp_list = []
            for y in range(columns):
                temp_list.append(image_array[x][y])
            output.append(temp_list)
        
    return output
        
        
    #return output_array

def rgb_to_grayscale(rgb_image_array):
    
    rows = len(rgb_image_array) #2 rows
    columns = len(rgb_image_array[0]) #3 columns
    output = []    
    
    for x in range(rows):
        temp_list = []
        for y in range(columns):
            gray = 0
            for z in range(3):
                place = rgb_image_array[x][y][z]
                if z == 0:
                    gray += 0.2989 * place
                elif z == 1:
                    gray += 0.5870 * place
                elif z == 2:
                    gray += 0.1140 * place
            temp_list.append(gray)
        output.append(temp_list)
    return output
                
        

    #return output_array
    

def invert_rgb(image_array):
    
    rows = len(image_array)
    columns = len(image_array[0])
    output = []
    
    for x in range(rows):
        pixel_row = []
        for y in range(columns):
            pixel = []
            for z in range(3):
                pixel.append(abs(image_array[x][y][z] - 255))
            pixel_row.append(pixel)
        output.append(pixel_row)
           
    return output
                


if (__name__ == "__main__"):
    '''file = 'robot.png'
    utilities.write_image(rgb_to_grayscale(utilities.image_to_list(file)), 'gray.png')
    '''
    square = 'square.jpg'
    robot = 'robot.png'
    graysquare = 'gray_square.png'
    pikachu = 'surprised_pikachu.png'
    gray_pikachu = 'gray_pikachu.png'
    #utilities.write_image(rgb_to_grayscale(utilities.image_to_list(square)), 'test1.png')
    utilities.write_image(crop(utilities.image_to_list(square), 'down', 13), 'wtf2.png')
    #utilities.write_image(rotate_90_degrees(utilities.image_to_list(square), -1), 'test7.png')
    #utilities.write_image(flip_image(utilities.image_to_list(square), -1), 'test8.png')
    #utilities.write_image(rotate_90_degrees(utilities.image_to_list(robot), 1), 'clockwise_robot.png')
    #utilities.write_image(invert_grayscale(utilities.image_to_list(graysquare)), 'test5.png')
    utilities.write_image(rgb_to_grayscale(utilities.image_to_list(pikachu)), 'gray_pikachu.png')
    utilities.write_image(invert_grayscale(utilities.image_to_list(gray_pikachu)), 'test9.png')
    utilities.write_image(invert_rgb(utilities.image_to_list(pikachu)), 'test6.png')
