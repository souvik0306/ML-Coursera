num_iters = 1500;
alpha = 0.01;
data = load('D:\Machine Learning Coursera\ex1-ex8-matlab\ex1data1.txt');
y = data(:, 2);
theta = zeros(2, 1);
m = length(y);
x = [ones(m, 1), data(:,1)]; 

fprintf('\nRunning Gradient Descent ...\n')
theta = rough(x, y, theta, alpha, num_iters);

fprintf('Theta found by gradient descent:\n');
fprintf('%f\n', theta);

