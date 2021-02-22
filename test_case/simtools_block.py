import numpy as np
import math
import sys
import matplotlib.pyplot as plt
from ..simtools import *
from ..simtools.gaussian import LinearGaussian, SineGaussian
from ..simtools.pulse import Square

print('********************************************************************')
print('')
print('block:')

TEST_COUNT = 0

sampling_rate = 1000.;end_time = 4.
clock = Time(1./sampling_rate)

# step verify
print('\tTest step\t\t', end =" ");TEST_COUNT += 1
l = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
clock.SetTick(1./10.)
clock.Reset()
c = clock.Offline(1.0)
if (len(c) != len(l)):
    print('Signal: Fail in ', TEST_COUNT, '-1')
    print(c)
    print(l)
    print(np.arange( 0.0, 1.0, clock.step() ))
    print( range(int(math.floor((1.0-0.0)/clock.step()))+1 ) )
    raise AssertionError()
if ((c != l).any()):
    print('Signal: Fail in ', TEST_COUNT, '-1')
    print(c != l)
    print(c)
    print(l)
    raise AssertionError()
l = np.array([0.0, 0.090909, 0.181818, 0.272727, 0.363636, 0.454545, 0.545455, 0.636364, 0.727273, 0.818182, 0.909091, 1.0])
clock.SetTick(1./11.)
clock.Reset()
c = np.around( clock.Offline(1.0), 6)
if (len(c) != len(l)):
    print('Signal: Fail in ', TEST_COUNT, '-2')
    print(c)
    print(l)
    print( range(int(math.floor((1.0-0.0)/clock.step()))+1 ) )
    raise AssertionError()
if ((c != l).any()):
    print('Signal: Fail in ', TEST_COUNT, '-2')
    print(c)
    print(l)
    raise AssertionError()
l = np.array([0.0, 0.111111, 0.222222, 0.333333, 0.444444, 0.555556, 0.666667, 0.777778, 0.888889, 1.0])
clock.SetTick(1./9.)
clock.Reset()
c = np.around( clock.Offline(1.0), 6)
if (len(c) != len(l)):
    print('Signal: Fail in ', TEST_COUNT, '-3')
    print(c)
    print(l)
    print(np.arange( 0.0, 1.0+clock.step(), clock.step() ))
    print( range(int(math.ceil((1.0-0.0)/clock.step()))+1 ) )
    raise AssertionError()
if ((c != l).any()):
    print('Signal: Fail in ', TEST_COUNT, '-3')
    print(c)
    print(l)
    raise AssertionError()
print('Pass')

#LinearGaussian test
print('\tTest LinearGaussian\t', end =" ");TEST_COUNT += 1
clock.SetTick(1./sampling_rate)

sigma = 0.2;m = 1.;c = 1.
clock.Reset()

line = LinearGaussian(0.0, m, c)
line_ran = LinearGaussian(sigma, m, c)
while (clock.now() < end_time):
    clock.Tick()
    line.Update(None)
    line_ran.Update(None)

y = np.around(np.linspace(c, m*end_time+c, clock.Len()), 3)
yl = np.around(line.Y(), 3)
yl2 = np.around(line_ran.Y(), 3)
if ( len(y) != len(yl) ):
    print('Signal: Fail in ', TEST_COUNT, '-1')
    print('y:  ', len(y))
    print('yl: ', len(yl))
    raise AssertionError()
if ( len(y) != len(yl2) ):
    print('Signal: Fail in ', TEST_COUNT, '-2')
    print('y:   ', len(y))
    print('yl2: ', len(yl2))
    raise AssertionError()
if ((y != yl).any()):
    print('Signal: Fail in ', TEST_COUNT, '-3')
    #for i in range( len(y) ):
    #    if (y[i] != yl[i]):
    #        print(i, y[i], yl[i])
    raise AssertionError()

plt.subplot(311)
plt.scatter(clock.timespace(), yl2, c='g', s=0.5)
plt.plot(clock.timespace(), yl)
plt.title("Linear")
print('Pass')


#SineGaussian test
print('\tTest SineGaussian\t', end =" ");TEST_COUNT += 1
amp = 1.;frq = 1.;shift = 0.
clock.Reset()

sine = SineGaussian(0.0, amp, frq, shift)
sine_ran = SineGaussian(sigma, amp, frq, shift)
while (clock.now() < end_time):
    clock.Tick()
    sine.Update(None)
    sine_ran.Update(None)

t = np.linspace(0., end_time, clock.Len())
y = np.around(np.array( amp*np.sin(2.*math.pi*frq*t+shift) ), 3)
ys = np.around(sine.Y(), 3)
ys2 = np.around(sine_ran.Y(), 3)
if ( len(t) != clock.Len() ):
    print('Signal: Fail in ', TEST_COUNT, '-1')
    print('t:  ', len(t))
    print('clock.t: ', clock.Len())
    raise AssertionError()
if ( len(y) != len(ys) ):
    print('Signal: Fail in ', TEST_COUNT, '-2')
    print('y:  ', len(y))
    print('ys: ', len(ys))
    raise AssertionError()
if ( len(y) != len(ys2) ):
    print('Signal: Fail in ', TEST_COUNT, '-3')
    print('y:   ', len(y))
    print('ys2: ', len(ys2))
    raise AssertionError()
if ((y != ys).any()):
    print('Signal: Fail in ', TEST_COUNT, '-4')
    print(y)
    print(ys)
    print(sine.t())
    raise AssertionError()

plt.subplot(312)
plt.scatter(clock.timespace(), ys2, c='g', s=0.5)
plt.plot(clock.timespace(), ys)
plt.title("Sine")
print('Pass')

#Square test
print('\tTest SineGaussian\t', end =" ");TEST_COUNT += 1
terms = 80;amp = 4.;frq = 4.;d = 0.5;shift = 0.
clock.Reset()

square = Square(0.0, terms, amp, frq, d, shift)
square_ran = Square(sigma, terms, amp, frq, d, shift)
while (clock.now() < end_time):
    clock.Tick()
    square.Update(None)
    square_ran.Update(None)
y = square.Y()
yw = square_ran.Y()

plt.subplot(313)
plt.plot(clock.timespace(), y)
plt.scatter(clock.timespace(), yw, c='g', s=0.5)
plt.title("Square")
print('Pass')

print()

if (len(sys.argv) > 1):
    if (bool(sys.argv[1]) is True):
        plt.show()
