from sense_emu import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp
    pixels = []
    for i in range(64):
        if i < temp:
            pixels.append(red)
        else:
            pixels.append(blue) 
    sense.set_pixels(pixels)
