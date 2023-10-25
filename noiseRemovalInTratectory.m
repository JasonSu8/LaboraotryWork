% step 1
path = 'D:/AAA/trajectory.mat';

trajectory = load(path);

xx = trajectory(1, :);
yy = trajectory(2, :);

% step 2
leftBoundary = 111;
rightBoundary = 222;
lowerBoundary = 333;
upperBoundary = 444;

doorWidth = 55;

xCenter = (leftBoundary + rightBoundary) / 2;
yCenter = (upperBoundary + lowerBoundary) / 2;

% step 3
xx((xx > leftBoundary) | (xx < rightBoundary) | (yy > lowerBoundary) | (yy < upperBoundary)) = nan;
yi((xx > leftBoundary) | (xx < rightBoundary) | (yy > lowerBoundary) | (yy < upperBoundary)) = nan;

xx(isnan(xx)) = interp1(find(~isnan(xx)), xx(~isnan(xx)), find(isnan(xx)), 'linear');
yy(isnan(yy)) = interp1(find(~isnan(yy)), yy(~isnan(yy)), find(isnan(yy)), 'linear');

% step 4
for i = 1:(length(xx) - 1)
    if ~isnan(xx(i)) && ~isnan(xx(i + 1)) && (((xx(i) > xCenter) && (xx(i + 1) < xCenter)) || ((xx(i) < xCenter) && (xx(i + 1) > xCenter)))
        yn = (xCenter - xx(i)) / (xx(i + 1) - xx(i)) * (yy(i + 1) - yy(i)) + yy(i);
        if ((yn < (yCenter - doorWidth / 2)) || (yn > (yCenter + doorWidth / 2))) && ((i + 2) <= length(xx))
            for j = (i + 2):length(xx)
                if ~isnan(xx(j)) && (((xx(i) < xCenter) && (xx(j) < xCenter)) || ((xx(i) > xCenter) && (xx(j) > xCenter)))
                    xx((i + 1):(j - 1)) = nan;
                    yy((i + 1):(j - 1)) = nan;
                    break;
                end
                if ~isnan(xx(j)) && (((xx(i) > xCenter) && (xx(j) < xCenter)) || ((xx(i) < xCenter) && (xx(j) > xCenter)))
                    yn = (xCenter - xx(i)) / (xx(j) - xx(i)) * (yy(j) - yy(i)) + yy(i);
                    if ((yn > (yCenter - doorWidth / 2)) && (yn <= (yCenter + doorWidth / 2)))
                        xx((i + 1):(j - 1)) = nan;
                        yy((i + 1):(j - 1)) = nan;
                        break;
                    end
                end
            end
        end
    end
end

xx(isnan(xx)) = interp1(find(~isnan(xx)), xx(~isnan(xx)), find(isnan(xx)), 'linear');
yy(isnan(yy)) = interp1(find(~isnan(yy)), yy(~isnan(yy)), find(isnan(yy)), 'linear');
