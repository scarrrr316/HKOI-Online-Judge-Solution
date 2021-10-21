uses sysUtils;
var
    a, b, c : ansiString;
    i, longerLength, shorterLength, thisSum, toAdd : integer;
    carry : boolean;
    
begin
    readln(a);
    readln(b);
    
    if length(a) >= length(b) then
    begin
        longerLength  := length(a);
        shorterLength := length(b);
    end
    else
    begin
        longerLength  := length(b);
        shorterLength := length(a);
    end;
        
    // Pad leading zero for shorter string
    for i := 1 to (longerLength - shorterLength) do
        if length(a) > length(b) then
            b := '0' + b
        else
            a := '0' + a;
    
    // Prepare output variable   
    c := '';
    for i := 1 to longerLength+1 do c := c + ' ';
    
    // Actual addition process
    carry := false;
    for i := longerLength downto 0 do
    begin
        thisSum := StrToIntDef(a[i],0 ) + StrToIntDef(b[i], 0);
        if carry then
            thisSum := thisSum + 1;
        
        toAdd := thisSum;
        if thisSum >= 10 then
        begin
            carry := true;
            toAdd := toAdd - 10;
        end
        else
            carry := false;
            
        c[i+1] := IntToStr(toAdd)[1];
    end;
    
    if c[1] = '0' then
        c := copy(c, 2, length(c)-1);
    writeln(c);
end.
