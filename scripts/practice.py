def glitch_the_image():

    glitcher = ImageGlitcher()

    img = Image.open(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/images/test_image.JPG')
    
    glitch_img = glitcher.glitch_image(img, glitch_amount(), color_offset= color_offset(), seed = random_seed())

    glitch_img.save(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/output/test_out.jpg')
glitch_the_image()