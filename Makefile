install:
	mkdir -p /usr/local/samp
	cp samp.py blog.db /usr/local/samp
	chmod a+w /usr/local/samp
	chmod a+w /usr/local/samp/blog.db
	echo -e "To run,\n    cd /usr/local/samp\n    python3 samp.py"
