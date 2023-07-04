"""
Python implementation of Drawing With Fourier Epicycles, based on Coding Train Tutorial by Daniel Shiffman:
https://thecodingtrain.com/CodingChallenges/130.3-fourier-transform-drawing.html

Uses drawing coordinate extraction algorithm from Randy Olson:
http://www.randalolson.com/2018/04/11/traveling-salesman-portrait-in-python/

MIT License
"""
import epicycles as epicycles
import fourier as fourier

# This is just a simple box drawn in paint.  You can adjust num_indicies and indices_step_size to trade speed for
# accuracy. There is also a read_json_as_complex that will read in coordinates in JSON format directly.  You can modify
# Daniel's Coding Train JavaScript coordinates to be JSON and that will run well.
z = epicycles.Epicycles.read_image_as_complex("./data/in/heart.png", ratio_indicies=2, indices_step_size=10)
fourier_data = fourier.fft(z)

# Sort so that largest epicycles are at the center, and the smaller ones are at the location of the drawing points
fourier_data.sort(key=lambda x: x.amplitude, reverse=True)
epicycles = epicycles.Epicycles(fourier_data, plot_size=[1024, 1024])
epicycles.run()