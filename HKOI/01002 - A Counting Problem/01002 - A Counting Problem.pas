var
  search : ansiString;
  target : string[200];
  count, loc : integer;
    
begin
    readln(search);
    readln(target);
    
    count := 0;
    loc := pos(target, search);
    while (loc <> 0) do
    begin
        count := count + 1;
        search[loc] := chr(7);
        
        loc := pos(target, search);
    end;
    writeln(count);
end.
