echo "rebuild ppwtest virtual env"
rm -rf dist/*
poetry build
conda env remove -y -n ppwtest
conda create -n ppwtest --clone py38

eval "$(conda shell.bash hook)"
conda activate ppwtest
# pip_="$(conda info --base)/envs/ppwtest/bin/pip"

# $pip_ install dist/*.whl --force-reinstall

echo "install ppw to ppwtest"
pip install dist/*.whl --force-reinstall

echo "go to /tmp folder and prepare folder"
cd /tmp

if [ $# == 1 ]; then
    rm -rf /tmp/$1
fi

rm -rf /tmp/ppwtest

echo "running ppw"
ppw

# change to /tmp/
cd /tmp/$1

