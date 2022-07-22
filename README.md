# ML-Coursera

## Neural Network Week 4 - 

### Quiz 1 - 

<ol>
  <li>TRUE - 
    <ul>
      <li>Any logical function over binary-valued (0 or 1) inputs x1 and x2 can be (approximately) represented using some neural network.
</li>
      <li>The activation values of the hidden units in a neural network, with the sigmoid activation function applied at every layer, are always in the range (0, 1).	</li>
    </ul>
  </li>
  <li>NAND</li>
  <li>This correctly uses the first row of Θ(2) and includes the "+1" term of a(2)0</li>
  <li>Remains Same</li>
</ol>

### Quiz 2- 
1. Δ (2):=Δ (2)+δ (3)∗(a (2) ) T
2. reshape(thetaVec(16:39),4,6)
3. 12.0012
4. TRUE - <ul>
      <li>For computational efficiency, after we have performed gradient checking to verify that our backpropagation code is correct, we usually disable gradient checking before using backpropagation to train the network.</li>
      <li>Using gradient checking can help verify if one's implementation of backpropagation is bug-free.	</li>
    </ul>
    
5. TRUE - <ul>
      <li>If we are training a neural network using gradient descent, one reasonable "debugging" step to make sure it is working is to plot J(Θ) as a function of the number of iterations, and make sure it is decreasing (or at least non-increasing) after each iteration.</li>

      <li>Suppose you are training a neural network using gradient descent.  Depending on your random initialization, your algorithm may converge to different local optima (i.e., if you run the algorithm twice with different random initializations, gradient descent may converge to two different solutions).</li>
    </ul>

### Machine Learning System Design Quiz Week 6 - 
1. Precision = 0.087 | F1 Score = 0.095
2. TRUE - <ul>
      <li>The features x contain sufficient information to predict y accurately.  (For example, one way to verify this is if a human expert on the domain can confidently predict y when given only x).</li>

      <li>We train a learning algorithm with a large number of parameters (that is able to learn/represent fairly complex functions).</li>
    </ul>
3. The classifier is likely to now have higher recall. when threshold in reduced from 0.5 to 0.1.
4. TRUE - <ul>
      <li>A good classifier should have both a high precision and high recall on the cross validation set.</li>

      <li>If you always predict non-spam (output y=0), your classifier will have 99% accuracy on the training set, and it will likely perform similarly on the cross validation set.</li>

      <li>If you always predict non-spam (output y=0), your classifier will have an accuracy of 99%.</li>
    </ul>
5. TRUE - <ul>
      <li>Using a very large training set makes it unlikely for model to overfit the training data.</li>

    <li>The "error analysis" process of manually examining the examples which your algorithm got wrong can help suggest what are good steps to take (e.g., developing new features) to improve your algorithm's performance
</li>

</ul>

## Tips - 

| High Bias (Underfit)      | High Variance (Overfit) |
| :-----------: | :-----------: |
| High Training Error      | Low Training Error       |
| High Cross Validation Error   | High Cross Validation Error        |

  <image src="https://github.com/souvik0306/ML-Coursera/blob/main/ex1-ex8-matlab/MATLAB%20Files/EX4/Media/Bias%20Variance.png" width="450" height="350">
  
## Gradient Descent - 

  <image src="https://github.com/souvik0306/ML-Coursera/blob/main/Linear%20Regression/Gradient%20Descent.gif" width="450" height="350">

## Logistic Regression -

  <image src="https://github.com/souvik0306/ML-Coursera/blob/main/ex1-ex8-matlab/MATLAB%20Files/EX2/Media/Logistic%20Regression%20Plot%202.jpg" width="450" height="350">
  
  <image src="https://github.com/souvik0306/ML-Coursera/blob/main/ex1-ex8-matlab/MATLAB%20Files/EX2/Media/Logistic%20Regression%20Plot%201.jpg" width="450" height="350">
