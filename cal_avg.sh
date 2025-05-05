read -p "Enter python marks " pmarks
read -p "Enter linux Marks " lmarks
read -p "Enter DBMS Marks " dmarks

sum=$((pmarks+lmarks+dmarks))
avg=$((sum/3))
echo "Average marks is $avg"

if(($avg > 70 && $avg <=100));
then
echo "Your grade is A+"
elif(($avg >60 && $avg<=70));
then
echo "Your grade is A"
elif(($avg > 50 && $avg <=60));
then
echo "Your grade is B"
elif(($avg >40 && $avg<=50));
then 
echo "Your grade is C"
else
echo "Your grade is F"
fi
