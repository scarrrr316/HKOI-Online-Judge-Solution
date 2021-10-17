program task01005;
Var input,output:String;
i,k:integer;
begin
    readln(input);
    k:=0;
    Delete(input,length(input)-3,4);
    output:=input;
    for i:=0 to length(input) do
        begin
        output[k+1]:=input[length(input)-i];
        k:=k+1;
        end;
    write(output,'.mp3');
end.