"""
Python implementation of Drawing With Fourier Epicycles, based on Coding Train Tutorial by Daniel Shiffman:
https://thecodingtrain.com/CodingChallenges/130.3-fourier-transform-drawing.html

Uses drawing coordinate extraction algorithm from Randy Olson:
http://www.randalolson.com/2018/04/11/traveling-salesman-portrait-in-python/

MIT License
"""
import epicycles as epicycles
import fourier as fourier

parameters = {
    "name_image" : "umbrella.png",
    "ratio_indicies" : 2,
    "indices_step_size" : 2,
    "plot_size" : [680, 1209], # [1024, 1200]
    "dpi" : 100, # 1000
    "fps" : 40, # 60
    "lw_mult" : 3,
    "radius_mult" : 20
}
colors = {
    "line" : "#c9d6df",
    "circles" : "#0386b3",
    "vectors" : "#58b0bf",
    "background" : "#15110c" # "#15110c"
}

# get name of image without ending
name = parameters["name_image"].split(".")[0]

# This is just a simple box drawn in paint.  You can adjust num_indicies and indices_step_size to trade speed for
# accuracy. There is also a read_json_as_complex that will read in coordinates in JSON format directly.  You can modify
# Daniel's Coding Train JavaScript coordinates to be JSON and that will run well.
z = epicycles.Epicycles.read_image_as_complex(
    f"./data/in/{parameters['name_image']}", 
    ratio_indicies=parameters["ratio_indicies"], 
    indices_step_size=parameters["indices_step_size"]
)
print(f"Processing data in fourier transform ({len(z)} datapoints)")
fourier_data = fourier.fft(z)
print("Done Fourier Transform")

# Sort so that largest epicycles are at the center, and the smaller ones are at the location of the drawing points
fourier_data.sort(key=lambda x: x.amplitude, reverse=True)

# for i in range(50):
#     fourier_data.append(fourier_data[-1])

epicycles = epicycles.Epicycles(colors, parameters, fourier_data, plot_size=parameters["plot_size"]) # plot_size=[1024, 1024]
epicycles.run(name, parameters["dpi"], parameters["fps"])