# Neural Networks can learn Anything ?

Not true because we don't have resources, and data, we need more data,

## why ?

# We need math 

Keywords: weight, bias, activation, relu(rectified linear unit), 

## RELU , x if x>=0 or 0



# Neural networks are universal function approximator

# Because Functions describe the world

Maths is beautiful

Neural Networks are maths compiled program execution

Functions are base of all the ml and dl

If we have x and y can we find function , reverse of finding y given function


![Screenshot 2024-08-16 at 7.41.27 PM.png](../../_resources/Screenshot%202024-08-16%20at%207.41.27 PM.png)


Hence function approximator is that which predicts funciton by x and y.


Neural networks are universal function approximator

Neuron is just a function.
weights and bias are the parameters of the function



![Screenshot 2024-08-16 at 7.43.24 PM.png](../../_resources/Screenshot%202024-08-16%20at%207.43.24 PM.png)

Neuron is an equation with output from other layers , weights and bias

Neural networks are combinaton of various neurons with there functions and give an approximate funciton

This isn't enough sum of these individual networks will result in a linear equation, what we want is a non-linear funciton from these linear sumations 

## hence activation funciton
RELU is good here

## RELU function

![Screenshot 2024-08-16 at 7.48.00 PM.png](../../_resources/Screenshot%202024-08-16%20at%207.48.00 PM.png)
by changing weights in relu and bias we can try, because when a liner funcion meets RELU it's limited to be positive 
Let us see how it works

## The following is before RELU
![Screenshot 2024-08-16 at 7.47.08 PM.png](../../_resources/Screenshot%202024-08-16%20at%207.47.08 PM.png)
### After RELU 


![Screenshot 2024-08-16 at 7.50.27 PM.png](../../_resources/Screenshot%202024-08-16%20at%207.50.27 PM.png)

In Neural network, neurons  compliments each other

## Backpropagation is used to find the weights and bias

This is the great way, with deep learning we will do Funciton approximator.

Turing Complete, they can solve any computer language.

 

Neuron and neural network is great 
Hence without great deal of data, even with best algorithms we can't find the funcion ;
ex : let us say we have two points, and we can draw a line through those and over , our funciton is done, that's note good any two points can be learn, hence the function we approximated is no use, imagine 3 data points, the more amout. of data with actual relations can be classified to be a funciton,

Curve Fitting is the bending the line to fit a non-linear curve

Neuron takes many input and one output

We will put inputs in a matrix and perform a dot product with weights, for bias we take 1 in the input array and bias in the weigth

![Screenshot 2024-08-16 at 8.09.35 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.09.35 PM.png)



![Screenshot 2024-08-16 at 8.10.36 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.10.36 PM.png)

Loss should be minimized.
Backpropagation.

If we have have dimensional problems, Ex.images.


![Screenshot 2024-08-16 at 8.12.00 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.12.00 PM.png)

Noramalizing the input is one of the thing we can do to improve the model[-1,1]
LeakyReLu() can show negatives value

sigmoid function compresses into (0,1)
tanh funciton compresses into (-1,1) -> we will convert (0,1)

True Mandelbrot: two values to one value

Alternative Methods : besides neural networks
like: Taylor series, 

In taylor series , the input features are called Taylor features

![Screenshot 2024-08-16 at 8.19.19 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.19.19 PM.png)
instead of one weights, we can use a neural network ,
Taylor series is a good even we want to approximate around a point

Now, Fourier series comes into picture for range 

![Screenshot 2024-08-16 at 8.22.10 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.22.10 PM.png)


![Screenshot 2024-08-16 at 8.22.56 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.22.56 PM.png)

For fourier series: the input series is called Fourier features and the input will twice of the taylor because we have sin and cos

Discrete Fourier transform : is also good



![Screenshot 2024-08-16 at 8.24.16 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.24.16 PM.png)

Hence we can used with maths algorithms.
Two dimensional fourier is used for this , because images deals with 2 

![Screenshot 2024-08-16 at 8.25.16 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.25.16 PM.png)



![Screenshot 2024-08-16 at 8.26.07 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.26.07 PM.png)

For 5D series , its impossible just think about


![Screenshot 2024-08-16 at 8.26.47 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.26.47 PM.png)
## Hence we have Curse of Dimensionality
Thats why quantum mechanics are the world changer
And the solution upto some level is the following image

![Screenshot 2024-08-16 at 8.27.54 PM.png](../../_resources/Screenshot%202024-08-16%20at%208.27.54 PM.png)

Methods of approximation, this is greatly complex

Ex:MNISTdata

Fourier data is prone to overfitting , this not good for higher images analysis
source: https://youtu.be/TkwXa7Cvfr8?feature=shared
