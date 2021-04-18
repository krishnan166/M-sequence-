clear all;
%Enter the length of sequence
len=input('Enter  the length of sequence: ');
%Enter the polynomail
poly=input('Enter the polynomial: ');
%Enter initial state
ini= input('Enter initial state: ');
ff= log2(len+1); % find No flip flop for ex log(16+1)=4
% pn sequence genrator
a= zeros(len,ff); % create all possible combination zeroes
a(1,(1:ff))= ini;% first row initial state
for i = 1:(len-1)
x = 0;
for j = 2:(ff+1)
if (poly (1,j) == 1)

 val=a(i,(j-1));
x = xor (x,a(i,(j-1)));
end

end
a ((i+1),1:ff) = circshift(a(i,1:ff),[0 1]);
a ((i+1),1) = x;
end
for i = 1:len
h(1,i) = a(i,ff);
end
disp('M sequence generated :');
disp(h)
