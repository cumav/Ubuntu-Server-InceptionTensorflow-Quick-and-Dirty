# Ubuntu Inception Tensorflow Quick-and-Dirty

Fast way to deploy Tensorflow Inception apps on Digital ocean.
Works on Ubuntu 16.04.(tested on Digital Ocean)
How to get started:
- train your model. For more on that check out the "Tensorflow for poets" tutorial. https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0
- run the Shell Script. If that doesnt work try to install modules manually.
- after everything is installed, clone this repository and paste your retrained_labels.txt and retrained_graph.pb into the projects folder
- If you have more than two classes then change classify.py from  "<-- Change from here -->"
- Open terminal -> cd into the projects folder -> then: >$ nohup python3 classify.py
- App should be live now. Visit your ip at port=8080 if you want to change that change "host='0.0.0.0', port=8080"
- Check out this example: http://178.62.205.212:8080/
