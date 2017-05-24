# Spirograph
Drawing a virtual Spirograph with Python

## Setup

To use spirograph.py in another file, it mus be imported.
```python
from spirograph import Spirograph
```

To create a Spirograph with R = 200, r = 35, l = 0.65 in purple
```python
my_spirograph = Spirograph(200)
my_spirograph.setSmallCircle(35)
my_spirograph.setPen(0.65, 'purple')
my_spirograph.draw()
```

This will draw the following Spirograph to the screen
<p align="center">
	<img src="doc/img/spirograph0.png" alt="spirograph0" width="175">
</p>

The `my_spirograph` object can be reused to draw multiple Spirographs with different properties. To
clear the screen, call the “clear” function.

```python
my_spirograph.clear()
```

The file test.py contains a main function and can be executed to see examples.



Below are some examples, generated from this repositories code.

<p align="center">
	<img src="doc/img/spirograph1.png" alt="spirograph1" width="175" hspace="42"> <img src="doc/img/spirograph2.png" alt="spirograph2" width="175" hspace="42">
	<img src="doc/img/spirograph3.png" alt="spirograph3" width="175" hspace="42"> <img src="doc/img/spirograph4.png" alt="spirograph4" width="175">
</p>