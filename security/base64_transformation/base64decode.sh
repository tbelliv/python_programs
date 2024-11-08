#content of base64.txt in a var
text=$(<b64_1550406728131.txt)

#decode content 50 times
for ((i = 0; i < 50; i++)); do
   text=$(echo "$text" | base64 --decode)
done

#decoded result
echo "$text"
