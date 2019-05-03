# Cloth-Simulator
A real-time cloth simulator using point masses and springs system. 

<br/>

## Part 1: Masses and springs

Evenly spaced grid of point masses and then connected them by strings. Spring has three types, STRUCTURAL, SHEARING, BENDING. 


<img src="website/part1/all_constraints.jpeg" width="400"/>  <img src="website/part1/2.jpeg"  width="400"/>



<br/>

## Part 2: Simulation via numerical integration

### Extension

The constant ks controls the extension of the cloth.The larger the ks is, the more flat the cloth looks like. 

Small ks:

<img src="website/part2/ks/ks=1000.jpeg"  width="400"/>

Large ks:

<img src="website/part2/ks/ks=100000.jpeg"  width="400"/>


### Density

The constant density controls the gravity of the cloth. By increasing the density, the wrinkle part of the cloth is pulled down more by gravity. 

Small density:

<img src="website/part2/density/density1.jpeg" width="400"/>  

Large density:

<img src="website/part2/density/density10.jpeg"  width="400"/>


### Damping

Damping constant controls the oscillation of the spring force. The smaller the damping constant, the longer the cloth stay oscillated and moving. 

Small damping:

<img src="website/part2/damping/damping0.0_2.jpg" width="200"/>  <img src="website/part2/damping/damping0.0_3.jpg"  width="200"/>  <img src="website/part2/damping/damping0.0_4.jpg" width="200"/>  <img src="website/part2/damping/damping0.0_5.jpg"  width="200"/>

<br/>

Large damping:

<img src="website/part2/damping/damping0.2_1.jpg" width="200"/>  <img src="website/part2/damping/damping0.2_2.jpg"  width="200"/>  <img src="website/part2/damping/damping0.2_3.jpg" width="200"/>  <img src="website/part2/damping/damping0.2_4.jpg"  width="200"/>

<br/>

## Part 3: Handling collisions with other objects

Cloth on sphere

<img src="website/part3/5000.jpeg" width="400"/> 

Cloth on plane

<img src="website/part3/plane.jpeg"  width="400"/>

<br/>

## Part 4: Handling self-collisions

<img src="website/part4/density5_0.jpeg" width="400"/>  <img src="website/part4/density5_1.jpeg"  width="400"/>  <img src="website/part4/density5_2.jpeg" width="400"/>  <img src="website/part4/density5_3.jpeg"  width="400"/>


<br/>

## Part 5: Shaders

### Blinn-Phong Shading
<img src="website/part5/Blinn.jpeg"  width="400"/>

### Texture Shading
<img src="website/part5/texture.jpeg"  width="400"/>

### Displacement and Bump Mapping

<img src="website/part5/Displacement128.jpeg"  width="400"/>  <img src="website/part5/Bump128.jpeg"  width="400"/>

### Environment-mapped Reflections

<img src="website/part5/env.jpeg"  width="400"/>
