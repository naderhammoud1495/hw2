# hw2
Python Code that receives a country name and it returns Country’s Full Name Capital Common Language Currency Name and Currency rate.

#Installation

pip install flask

pip install requests

#Run the code

git clone https://github.com/naderhammoud1495/hw2.git

docker build --tag hw2 .

docker run hw2

docker run --publish 5000:5000 hw2

then open http://127.0.0.1:5000/country_name and enter the country name in the url
