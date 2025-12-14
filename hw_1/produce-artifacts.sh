
echo 'hello from stdin' | ./1.nl.py 1.nl.py ~/.bashrc - > artifacts/1.txt
# echo 'hello from stdin' | nl -b a 1.nl.py ~/.bashrc - > artifacts/1-nl.txt

./2.tail.py 2.tail.py ~/.bashrc > artifacts/2.txt

./3.wc.py 3.wc.py ~/.bashrc 2.tail.py 1.nl.py > artifacts/3.txt