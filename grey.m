%% ������ǲ��Լ�����������������֮��Ļ�ɫ������
%% [Y] = mapminmax(PSEACC1,0,1);
%% ����pusi pusi=0.5;
%% detaֵ��ȡ����ֵ
for k = 1:165  %930
    for i = 1:731
        A(i,:) = abs(PSEACC1(i,:) - PSEACC1S5(k,:));  
        %A(i,:) = abs( PSEACC1S5(k,:) - PSEACC1(i,:));
    end
%% ȡ�����Сֵ
    detamax = max(A(:));
    detamin = min(A(:));
%% jiamaֵ
    for a= 1:731
        for j= 1:26
            jiama(a,j) = (detamin+0.5*detamax)/(A(a,j)+0.5*detamax);
        end
    end
%% ����
    for b = 1:731
        yita(k,b)=sum(jiama(b,:))/26;
    end
end
