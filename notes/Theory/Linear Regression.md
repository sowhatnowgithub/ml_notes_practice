## LINEAR REGRESSION
Keywords for quick reference
Residuals are the data points
-> least squares , If we take a line and sum the squares of the points from this line ,
That line which sum of the squares is less is called least squares
link :  https://www.youtube.com/watch?v=PaFPbb66DxQ
->R^2 , this will tell us the variance of the x by y-> R^2 = (VAR(mean)-VAR(fit))/VAR(mean)
```
SS = sum of squares = data^2
SS(mean) = sum of squares wrt mean= (data-mean)^2
SS(fit) = sum of squares wrt least squar line = (data -line)^2
VAR = variance = (sumation of data^2)/n
where n is no of obesrvations

VAR(mean)  = (sumation of (data-mean)^2)/n

VAR(fit) = sumation of (data-line)^2 / n

R^2 = 1-(VAR(fit)/VAR(mean))
```
this implies the y is effected by x by this percentage (R^2 *100) % 
That is if we know x , we can be sure to know (R^2*100)% of y
in other words our varitation is now zero 

if We make VAR(fit) = 0, that is the all data points lie on the line , hence (data-line)=0

That is we know x, we know 100% of y

This also has limitations if we VAR(mean) = VAR(fit) , R^2 is zero this is actually possible if the line we considered that is least squares line is near to mean of the data

The best things is we can take any variable lines and if we can calculate the SS(mean)
and SS(fit)

For example lets us say y depends on x and z
then we will have plane instead of line
y = 0.1 + 0.7x + 2z

link : https://www.youtube.com/watch?v=7ArmBVF2dCs

The interesting part is even if the parameters increase its not worse than two parameters
If something makes the ss(fit) bigger the least squares will make it zero 

The more random events leads to ss(fit) becoming smaller resulting in better R^2

Hence people use adjusted R^2

R^2 is awesome but if we have only two points , SS(fit) will be zero but any two random points will lead the same result, because we can always find a line passing through two points


For this P-value 

---->P-value for R^2 comes from the something called "F"
```
F = The variation in mouse size explained by weight/The variation in mouse size not explained by weight
```

Numerator is same for both the F and R^2 are same

The demoniator of the F is  different as the dotted lines residuals which are not explained by weight

imagine this if we have a linear relation between y and x , we can tell one from other Now if we have some deviation from the true equation , that deviaton (variation in other words variance) is present ,this is called residuals 
Now we have to understand that this residuals cannot be understood by the R^2, hence we define F to understand the imporatnce of residuals in finding the prediction

![Screenshot 2024-08-15 at 7.19.00 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.19.00 PM.png)



![Screenshot 2024-08-15 at 7.22.59 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.22.59 PM.png)

--> F

![Screenshot 2024-08-15 at 7.23.39 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.23.39 PM.png)

SS(fit) is the sum of the squares of the residuals 

Pfit - Pmean -->
Pfit is the number of parameters in the fit line
ex : y = (intercept of y) + slope*x
we have two parameters
Pfit = 2

Pmean is the number of parameters in the mean line
ex: y = (intercep of y = mean)
Pmean = 1

In example = Pfit - Pmean = 1, thus numerator explains the extra parameter ,

Denominator  : Why divide the SS(fit) by (n-Pfit) instead of just n?

the more parameters we have the more data u need to estimate,

A large number in the numerator sugggests us that we can predict by the parameters
A small number in the denominator suggests that the stuff we couldn't explain with the given parameters is small 

Hence F should be large
But how to calculate P-value from F?

We create multiple F values using multiple random data , and plot it in histogram , 

If large F / large number
Now P-value is the more extreme value divided by all the values

![Screenshot 2024-08-15 at 7.34.27 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.34.27 PM.png)



![Screenshot 2024-08-15 at 7.34.40 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.34.40 PM.png)



![Screenshot 2024-08-15 at 7.35.20 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.35.20 PM.png)



![Screenshot 2024-08-15 at 7.35.45 PM.png](../../_resources/Screenshot%202024-08-15%20at%207.35.45 PM.png)


Given Data ,
Linear regression :
	1) Quantifies the relationship in the data(R^2)
		this needs to large
	2) Determines how reliable that relationship is (this is the P-value we calculate with F)
	 This needs to be small
	 
	 