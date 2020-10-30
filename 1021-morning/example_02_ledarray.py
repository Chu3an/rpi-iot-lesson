from sense_emu import SenseHat

sense = SenseHat()

white = (255, 255, 255)
green = (0, 255, 0)

pixels = []
for i in range(64):
    pixels.append(white)
pixels[10]=green
sense.set_pixels(pixels)
