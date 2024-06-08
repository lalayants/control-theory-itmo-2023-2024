clear;
close all;
T = 0.077;
k = 114.49;
k_p = 50;
TF = k_p * tf([k], [T, 1]) * tf([1], [1, 0]);
TF = TF / (1 + TF);
bode(TF)
h = bodeplot(TF);
setoptions(h,'FreqUnits','Hz','PhaseVisible','off');