
pip steps:

pip install -r web\requirements.txt
pip freeze > requirements.txt


conda steps:
conda create -n pisite python=2.7
activate pisite
...
conda env export -f environment.yml
