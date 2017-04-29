from bottle import route, run, template,get, post, request , static_file
import tensorflow as tf, sys
import urllib 
import sys
import collections

@route('/')
def root():
    return static_file('start.html', root='.')

@route('/upload', method='POST')
def do_upload():
    try:
        try:
            tf.reset_default_graph()
        except:
            pass
        jpgPic = request.forms.get('jpgPic')
        image_data = urllib.urlopen(jpgPic).read()
        
        label_lines = [line.rstrip() for line in tf.gfile.GFile("retrained_labels.txt")]
        with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
                    
            predictions = sess.run(softmax_tensor, \
                                   {'DecodeJpeg/contents:0': image_data})
            # Here only binary classification. If more labels then add predictions [0][x] snd label_lines[x]
            prediction1 = str((str("%.2f" %((predictions [0][1])*100)) +"%"+ " " + str(label_lines[1])))
            prediction2   = str((str("%.2f" %((predictions [0][0])*100)) +"%"+ " " + str(label_lines[0])))
        tf.reset_default_graph()

    except:
        prediction1 = "none"
        prediction2 = "none"
    
    return template('<h3>{{prediction2}} and {{prediction1}}</h3>', prediction2 = prediction2, prediction1 = prediction1)


run(host='0.0.0.0', port=8080)

