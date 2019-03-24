%% 计算的是测试集中肽链和所有肽链之间的灰色关联度
%% [Y] = mapminmax(PSEACC1,0,1);
%% 参数pusi pusi=0.5;
%% deta值，取绝对值
for k = 1:165  %930
    for i = 1:731
        A(i,:) = abs(PSEACC1(i,:) - PSEACC1S5(k,:));  
        %A(i,:) = abs( PSEACC1S5(k,:) - PSEACC1(i,:));
    end
%% 取最大最小值
    detamax = max(A(:));
    detamin = min(A(:));
%% jiama值
    for a= 1:731
        for j= 1:26
            jiama(a,j) = (detamin+0.5*detamax)/(A(a,j)+0.5*detamax);
        end
    end
%% 最终
    for b = 1:731
        yita(k,b)=sum(jiama(b,:))/26;
    end
end
