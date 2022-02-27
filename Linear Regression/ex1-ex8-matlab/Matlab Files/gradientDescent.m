
function [theta, J_history] = gradientDescent(x, y, theta, alpha, num_iters)
clc
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha
for iter = 1:num_iters
    
% Initialize some useful values
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1);
    Prediction =  x * theta;
    temp1 = alpha/m * sum((Prediction - y));
    temp2 = alpha/m * sum((Prediction - y) .* x(:,2));
       
    theta(1) = theta(1) - temp1;
    theta(2) = theta(2) - temp2;
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(x, y, theta);

end

end
