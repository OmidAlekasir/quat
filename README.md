# Introduction
## Abstract
This library is primarily derived from the contributions of Geir Istad and has been released as a pip-installable package. The main objective of this library is to streamline operations involving vectors and quaternions, particularly in the context of working with Inertial Measurement Units (IMUs).

To install this package, execute the following command:

`pip install quat`

## Library Structure and Functions
* Quaternion:
    * **get_product**: Computes and returns the product of the current quaternion with another quaternion.
    * **get_conjugate**: Calculates and returns the conjugate of the quaternion.
    * **get_magnitude**: Determines and provides the magnitude of the quaternion.
    * **normalize**: Normalizes the quaternion to ensure unit length.
    * **get_normalized**: Retrieves the normalized form of the quaternion.
* XYZVector:
    * **get_magnitude**: Computes and returns the magnitude of the vector.
    * **normalize**: Normalizes the vector to maintain unit length.
    * **get_normalized**: Retrieves the normalized version of the vector.
    * **rotate**: Rotates the vector based on a given quaternion.
    * **get_rotated**: Returns the vector after rotation, as per the specified quaternion.

## About Rotation
In many scenarios, particularly in the context of Inertial Measurement Unit (IMU) applications, the rotation of a vector using a quaternion is a common requirement. For instance, the acceleration data acquired from an IMU is typically represented in a "body-frame," aligning with the IMU's axes.
However, in the realm of Inertial Navigation Systems (INS), having access to a world-frame acceleration vector is essential for accurate navigation. The illustration below illustrates the orientation of the world-frame and body-frame axes:

<p align="center"><img src="https://ars.els-cdn.com/content/image/3-s2.0-B9780128131893000162-f16-01-9780128131893.jpg"></p>

The rotation of a vector using a quaternion is achieved through the following formula:

$$A_p=q\times A\times q^*$$

where $q^*$ represents the conjugate of the quaternion q, and $A_p$ denotes the rotated original vector $A$.

## Example
Let's consider the scenario where the accelerometer outputs $(0, g, 0)$, with $g$ representing the gravitational acceleration. Assuming the quaternion corresponding to this vector (obtained from the IMU) is $(0.7071, 0.7071, 0, 0)$.

Upon rotating the acceleration vector using the provided quaternion, the resulting vector would be $(0, 0, g)$, now aligned towards the Earth (assuming the z-axis points towards the Earth).