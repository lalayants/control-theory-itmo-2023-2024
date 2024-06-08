sys = tf([1], [1 0 0 0]);
pd = tf([-3 -10 0], [1]);
f = feedback(sys, -pd);
[Gm,Pm,Wcg,Wcp]=margin(f);
deg2rad(180+Pm)/Wcg