**Tensor is a container which stores numbers. A special data case.**


**Scalar** - It is a number, and it is called 0D Tensor
```
import numpy as np
a = np.array(4)
a.ndim # this will give 0, dimenstion of the tensor is 0
```
**Multidimensional Number representaiton is Tenso**r

Tensor Classification :
**1.1D Tensor / Vector**
	[1,2,3,4] - Vector, 1D array or a 1D Tensor.
	**No of axis = rank = Dimension**
	[1,2] - This is a 1D Tensor but a 2 dimenstion Vector
```
b = np.array([1,2,4])
```
	
	A combination of scalars is a vector, a combination of vectors is a matrix and tensor comes out on the top. to create a tensor we will dimensions.
	
**2.2D Tensors**
	[1,2,3] [4,5,6] [7,8,9]
```
matrix = np.array([[1,2,3,],[4,5,6]])
matrix.ndim # outputs a 2
```
**3.ND Tensor**

**Rank, Axes and Shape**
1.No of Axes = Rank = No of dim
**Examples**
1.1D Tensor
	Students (1000)
	CGPA | IQ | STATE | PLACEMENT
	8.1	 , 91, 0, 1
	3D Vector - [8.1,91,0,1] - 3D vector, 1D Tensor
	In 1D tensor only one student can be knonwn 

![Screenshot 2024-09-14 at 1.35.28 PM.png](../../_resources/Screenshot%202024-09-14%20at%201.35.28 PM.png)

The output is [1, 0, 1,  ..... ] - 1Dimension Tensor

2.2D Tensors - 
In here the We have matrix, with multiple vectors, forming a matrix, 
![Screenshot 2024-09-14 at 1.37.27 PM.png](../../_resources/Screenshot%202024-09-14%20at%201.37.27 PM.png)

Matrix, is a 2D Tensor, which is combination of 10000 or someother combination of 1D Tensor

3.3D Tensors
	NLP - is an example
		Example  :
			Hi Nititsh
			Hi Rahul
			Hi Ankit 
		Conversion of the string to vectors is called vectorization.
		Hi | Nitish | Rahul | Ankit
		1 | 0 | 0 | 0 ---> this represents Hi 
		0 | 1 | 0 | 0 ---> this represents Nitish
		0 | 0 | 1 | 0 ---> this represents Rahul
	Hi Nitish ---> [[1,0,0,0],[0,1,0,0]]  - this is combination of 2D Tensors
![Screenshot 2024-09-14 at 1.47.24 PM.png](../../_resources/Screenshot%202024-09-14%20at%201.47.24 PM.png)

Shape --->  (3, 2,4) --> 24 items

**Timeseries Data** - like share market data,

For example, i am tracking the Highest and lowest of Stock value for 354 days that means i have a 2D Tensor,  [365,2]
Now if we introduce an another parameter like the values over a 10 years range then our 3D Tensor will be
[10,365,2]
![Screenshot 2024-09-14 at 1.51.55 PM.png](../../_resources/Screenshot%202024-09-14%20at%201.51.55 PM.png)

4.4D Tensor - Images based data
	Images - CV 
	Images is a collection of pixels,
	Red layer has (1200,800) rows and columns
	and we have three channels(R,G,B) (3,1200,800)
	and 
5.5D Tensors
Videos are a collection of framse
Ex: 60 sec of video and 30 fp, and 480P(480*720) (3 channesls)
(3,1800,480,720) and 60 seconds
(60,1800,,480,720) this suggests that the storage is a lot, but we don't have this much, we will have video encoders for this purpose