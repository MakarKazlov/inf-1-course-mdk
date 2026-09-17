#!/bin/bash
echo "Введите количество файлов N "
read N
for i in $(seq 1 $N)
do
    touch "file$i.txt"
    num1=$RANDOM
    num2=$RANDOM
    result=$(( num1 + num2 ))

    echo $num1 + $num2 = $result > file$i.txt
    cat file$i.txt
done



