---
title: "Other Projects"
permalink: /projects/
---

## Shape Viewer
_November 2024-present_
<figure class="half">
  <a href="/assets/images/furrow.png" title="Visualization of the surface z=1-x^2-y^2-2.5exp(-(x^2/4 + y^2)), colored by shape index with asymptotic curves drawn.">
  <img src="/assets/images/furrow.png" alt=""></a>
  <a href="/assets/images/monkeysaddle.png" title="Visualization of the surface z=x^3-3xy^2 colored by Gaussian curvature, with lines of principal curvature drawn and colored by family.">
  <img src="/assets/images/monkeysaddle.png" alt=""></a>
  <!-- <figcaption></figcaption> -->
</figure>
A key component of my PhD dissertation research is geometric shape analysis. This entails studying the properties of 2D and 3D shapes, and in particular, what makes one shape different from another. A lot of this depends on the local curvature of the surface or boundary, measured through various means. I created this Shape Viewer as a way to visualize local shape properties such as principal and asymptotic directions, ridges, flecnodes, etc. of any parametric surface (see _Jan J. Koenderink. 1990. Solid shape. MIT Press, Cambridge, MA, USA._) In addition, Shape Viewer allows for visualization of the Gauss and asymptotic spherical maps of a surface. These provide additional information as to shape properties.

Code can be found at [https://github.com/qscgy/shape-viewer/](https://github.com/qscgy/shape-viewer/).

## Fractal generator
_April 2024-present_
<figure class="third">
  <a href="/assets/images/julia_rainbow_0.285+0.01i_-1.5_-1.5_res3e+02.png" title="Julia of iteration of f(z)=z^2+0.285+0.01i." alt="Julia of iteration of f(z)=z^2+0.285+0.01i.">
  <img src="/assets/images/julia_rainbow_0.285+0.01i_-1.5_-1.5_res3e+02.png" alt=""></a>
  <a href="/assets/images/multijulia_rainbow2_o2.95_-0.5+-0.05i_-1.5_-1.5_res300.png" title="Julia set of iteration of f(z)=z^3-0.5-0.05i." alt="Julia set of iteration of f(z)=z^3-0.5-0.05i.">
  <img src="/assets/images/multijulia_rainbow2_o2.95_-0.5+-0.05i_-1.5_-1.5_res300.png" alt=""></a>
  <a href="/assets/images/multijulia_magma2_o4_-0.5+0.45i_-1.5_-1.5_res300.png" title="Julia set of iteration of f(z)=z^4-0.5+0.45i.">
  <img src="/assets/images/multijulia_magma2_o4_-0.5+0.45i_-1.5_-1.5_res300.png"></a>
  <!-- <figcaption></figcaption> -->
</figure>
I've been fascinated by fractals since 10th grade, when I learned how to use Java by generating them. I decided to write a fractal generator in C++ this time, in order to improve my skills with the languange and with OpenCV for C++. As of now, the user can generate Mandelbrot, Julia, or burning ship fractals and zoom in on parts of them by clicking at the corners of a bounding box. As part of this project, I wrote a lightweight library for color-mapping scalar values to a color scale.

The code can be found [here](https://github.com/qscgy/fractals-redux/).

## 3D Printed Topographic Map of Contiguous US
_March-October 2021_
![A 3D printed topographical map of the United States, in blue plastic.](/assets/images/IMG_4153.jpg)
This took several months, printing each state individually with a lot of time spent dialing in print settings. Done in PLA with 0.2 mm layer height.

## Open-Source Projects
In addition to my own projects, I am also an open-source contributor to Pandas and in the top 0.25% of English Wikipedia editors ([user page](https://en.wikipedia.org/wiki/User:ElasticSnake)).