__author__ = 'Majid Alekasir'
"""
Copyright (c) 2024 Majid Alekasir

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
===============================================
"""

from Quaternion import Quaternion as Q
from Quaternion import XYZVector as V

g = 9.8 # gravitational acceleration

# Quaternion
w = 0.7071
x = 0.7071
y = 0
z = 0

# Acceleration (y-axis, body-frame)
Ax = 0
Ay = g
Az = 0

# rotate body-frame acceleration vector to match the world-frame acceleration
q = Q(w, x, y, z) # define quaternion
q.normalize() # normalize the quaternion vector

A = V(Ax, Ay, Az) # define vector

# Rotate
Ap = A.get_rotated(q)

print("Body-frame acceleration vector:")
print("Ax = ", A.x)
print("Ay = ", A.y)
print("Az = ", A.z, '\n')

print("World-frame acceleration vector:")
print("Ax = ", Ap.x)
print("Ay = ", Ap.y)
print("Az = ", Ap.z)