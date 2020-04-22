import streamlit as st
import math
import random
import cairo
import numpy


st.title("Canvas Experiment with Streamlit")

with st.echo():
  WIDTH, HEIGHT = 500, 500

  radius = st.sidebar.slider("Radius", 8.0, 20.0, 11.0)
  grid_width = 9
  scale = 30
  margin = grid_width * scale / 2


  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
  ctx = cairo.Context(surface)

  ctx.save()
  ctx.set_source_rgb(1, 1, 1)
  ctx.paint()
  ctx.restore()

  ctx.rectangle(0, 0, WIDTH, HEIGHT)
  ctx.set_source_rgb(0.2, 0.23, 0.8)
  ctx.fill()

  ctx.translate(margin, margin)

  rotation_list = [(0, math.pi * 1.5), (math.pi * 0.5, math.pi * 2), (math.pi, math.pi * 0.5), (1.5 * math.pi, math.pi)]

  ctx.set_source_rgb(0,0,0)
  for x in range(grid_width):
    for y in range(grid_width):
      current_x = x * scale
      current_y = y * scale
      rotation_point = random.choice(rotation_list)
      ctx.move_to(current_x, current_y)
      ctx.arc(current_x, current_y, radius, rotation_point[0], rotation_point[1])
      ctx.close_path()
      ctx.fill()



  # Convert to bitmap
  buf = surface.get_data()
  bitmap = numpy.ndarray(
      shape=(WIDTH, HEIGHT, 4),
      dtype=numpy.uint8,
      buffer=buf)

  st.image(bitmap)


st.sidebar.button("re-run")