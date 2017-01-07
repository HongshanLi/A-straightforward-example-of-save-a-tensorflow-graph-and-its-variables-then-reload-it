# A-straightforward-example-of-save-a-tensorflow-graph-and-its-variables-then-reload-it
Since I haven't found a straightforward example demonstraing how to save a tensorflow graph and its assoicated variables
and resused it in another program. I decided to experiment a few things. The code is the result. I hope it is straightforward enough.
Traditionally, I believe one has to save the graph and its variables seperately, and load them seperately.
But since APIr.011, they included some handy functions:
tf.train.export_meta_graph()
tf.train.import_meta_graph()
which makes exporting and importing a graph and its variable really easy.
