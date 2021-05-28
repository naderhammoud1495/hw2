# hw2

Python Code that receives a country name and it returns Country’s Full Name Capital Common Language Currency Name and Currency rate.

## Installation
```bash
pip install flask

pip install requests
```
## Run the code
```bash
git clone https://github.com/naderhammoud1495/hw2.git

cd hw2

python main.py
```

## To create image and run with docker
```bash
docker build -t hw2 .

docker run -i -t -d -p 5000:5000 hw2

then open http://127.0.0.1:5000/country_name and enter the country name in the url
```
