all:
	$(MAKE) clean wheel install

clean:
	rm -rf build dist dense* 

wheel:
	ln -sf ../../GLU-Net dense
	pip install --user --upgrade setuptools wheel
	python setup.py sdist bdist_wheel

install:
	pip install --upgrade --force-reinstall dist/dense-1.0.0-py3-none-any.whl

