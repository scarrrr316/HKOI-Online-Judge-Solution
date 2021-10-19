program D101;
var
   phoneno:String;
begin
    readln(phoneno);
    if (phoneno[1] > '3') then
        writeln('Mobile')
    else
        writeln('Fixed');
end.

// program D101;
// var
//    phoneno:String;
// begin

//     readln(phoneno);
//     if (phoneno[1] = '2') or (phoneno[1] = '3') then
//         writeln('Fixed');
//     if (phoneno[1] = '5') or (phoneno[1] = '6') or (phoneno[1] = '9') then
//         writeln('Mobile')
// end.