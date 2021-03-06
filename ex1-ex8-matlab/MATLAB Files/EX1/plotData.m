function plotData(x, y)
clc
clear all
%PLOTDATA Plots the data points x and y into a new figure 
%   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
%   population and profit.
data = load('D:\Machine Learning Coursera\ML-Coursera\ex1-ex8-matlab\ex1data1.txt','r');
% format = '%f %f';
% textscan(data,format);

x = data(:, 1)
y = data(:, 2)
m = length(y)
plot(x, y, 'rx', 'MarkerSize', 10); % Plot the data
ylabel('Profit in $10,000s'); % Set the y􀀀axis label
xlabel('Population of City in 10,000s');
% open a new figure window

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the training data into a figure using the 
%               "figure" and "plot" commands. Set the axes labels using
%               the "xlabel" and "ylabel" commands. Assume the 
%               population and revenue data have been passed in
%               as the x and y arguments of this function.
%
% Hint: You can use the 'rx' option with plot to have the markers
%       appear as red crosses. Furthermore, you can make the
%       markers larger by using plot(..., 'rx', 'MarkerSize', 10);





% ============================================================

end
