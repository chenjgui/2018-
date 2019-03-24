%%

for j = 311:930
    for i = 1:930
        B(j,i) = sum(abs(alldataset(j,:) - alldataset(i,:)));
    end
end
[B1,INDEX] =sort(B,2);

% for k = 311:930
%     if INDEX(k,2)<310&&INDEX(k,3)<310
%         C(k)=k;
%     end
% end