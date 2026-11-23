var
i, j, c, x, y, t : longint;
a : array[1..1000] of longint;
begin
j := 1;
c := 1;
for i := 1 to 1000 do begin
a[i] := j;
if c - 1 = 0 then begin
j := j + 1;
c := j + 1;
end;
c := c - 1;
end;
read(x, y);
t := 0;
for i := x to y do
t := t + a[i];
write(t);
end.