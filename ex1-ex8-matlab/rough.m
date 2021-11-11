
function [theta, J_history] = rough(x, y, theta, alpha, num_iters)
clc
for iter = 1:num_iters
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1);
    Prediction =  x * theta;
    temp1 = alpha/m * sum((Prediction - y));
    temp2 = alpha/m * sum((Prediction - y) .* x(:,2));
       
    theta(1) = theta(1) - temp1;
    theta(2) = theta(2) - temp2;
    J_history(iter) = computeCost(x, y, theta);

end

end


