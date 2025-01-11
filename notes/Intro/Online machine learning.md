In this we train model using increment model data input.
with **miny batches of data**.
They **predict and learn**. And as new data is being introduced it will learn on new data and uses old data too.

When to consider online Learning?

1.Where the concept drift
	If the nature of the model is volatile, like stocks, seasonal markets, and so on

2. Cost Effective

3.Faster solution

How to Implement?

**Skitlearn** by design supports batch learning but can be used for batch learning

1. ***River*** is the best library for streaming data.
2. **VomPal Rabbit**

**Learning Rate:**
	Its important our model is trained not too fast and not too slow.
	
**Out of Core Learning:**
	The data is so huge , that we can't load the data, Hence we will convert them into small datasets and send it to the model in batch models.
	This is called **out of core learning** because here we are using batch learning to split the data and use online learing to create the model.
	
Disadvantages:
	1.Tricky to use
	2. Risky as these are new models.
	The solution is to create active detection to enhance the securityh
	