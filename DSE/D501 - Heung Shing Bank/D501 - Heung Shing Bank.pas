var
    f : textFile;
    i, n, this : integer;
    b : longInt;
    
begin
    assign(f, 'account.txt');
    reset(f);
    b := 0;
    
    readln(f, n);
    for i := 1 to n do
    begin
        readln(f, this);
        b := b + this;
    end;
    
    writeln(b);
end.
