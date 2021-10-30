program Cesar;

const
  alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_';
  len = 34;
label
  m_1, m_2;
var
  s0,s1,s: string;
  key,i,n,p: integer;
  c: char;
procedure Encrypt(s: string;k: integer;var es:string); // Процедура шифрования
var
  n,i,p: integer;
  c:char;
begin
  n:=length(s);                                       // Количество символов во введенной строке 
  es:=s;
  for i:=1 to n do begin                              // Перебор каждого символа во введенной строке
    c:=s[i];
    p:=pos(c,alf); p:=p+k;
    if p>len then p:=p-len;                           // Если номер символа + шаг сдвига переходят через конец алфавита
    es[i]:=alf[p];                                    // Шифрование символа
  end;
end;
procedure Decrypt(s:string;k:integer;var ds:string);  // Процедура дешифрования
var
  n,i,p:integer;
  c: char;
begin
  n:=length(s); 
  ds:=s;
  for i:=1 to n do begin                               // Перебор каждого символа во введенной строке
    c:=s[i];
    p:=pos(c,alf)-k; 
    if p<=0 then p:=p+len;                             // Если номер символа + шаг сдвига переходят через начало алфавита
    ds[i]:=alf[p];                                     // Дешифрование символа
  end;
end;

begin
  m_2: writeln('Введите фразу строчными русскими буквами (вместо пробела используйте клавишу "_"): ');
  readln(s0);
  n:=length(s0); 
  for i:=1 to n do                                    // Контроль наличия иных символов во введенной строке, кроме указанных
    begin                               
    c:=s0[i];
    p:=pos(c,alf);
    if  p=0 then 
      begin
         writeln('Oшибка, повторите ввод фразы!');
         goto m_2
      end;
     end;
  m_1: writeln('Введите шаг сдвига: целое положительное число для шифрования или целое отрицательное число для дешифрования ');
  readln(s);
        val(s,key,i);                                 //Контроль ввода числа
        if  i<>0 then 
          begin 
          writeln('Oшибка, повторите ввод!'); 
          goto m_1
          end; 
        if key=0 then begin writeln('Oшибка, повторите ввод!'); goto m_1 end else        // Контроль: шаг сдвига не равен 0
        begin
            if key>0 then begin writeln('Выполняется шифрование  '); Encrypt(s0,key,s1) end
            else begin writeln('Выполняется дешифрование  ');Decrypt(s0,-key,s1)end;
            writeln('Результат:  ',s1)
        end;
end.
