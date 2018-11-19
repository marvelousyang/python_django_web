# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import os
model_dir = '/home/lee/Downloads/inception'
image = '/home/lee/Downloads/yangyang.jpeg'
def create_graph():
    with tf.gfile.FastGFile(os.path.join(
            model_dir,'classify_image_graph_def.pb'),'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def,name='') 
create_graph()
image_data = tf.gfile.FastGFile(image,'rb').read()

#继承object
class NodeLookup(object):
    #类中方法第一个参数必须是self
    def __init__(
        self,label_lookup_path=None,
        uid_lookup_path=None):
        if not label_lookup_path:
            #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。 
            label_lookup_path = os.path.join(
                model_dir,'imagenet_2012_challenge_label_map_proto.pbtxt'
            )
        if not uid_lookup_path:
            uid_lookup_path = os.path.join(
                model_dir,'imagenet_synset_to_human_label_map.txt'
            )
        self.node_lookup = self.load(label_lookup_path,uid_lookup_path)
    
    def load(self,label_lookup_path,uid_lookup_path):
        #tf.gfile与os相似
        if not tf.gfile.Exists(uid_lookup_path):
            tf.logging.fatal('File does not exist %s',uid_lookup_path)
        if not tf.gfile.Exists(label_lookup_path):
            tf.logging.fatal('file does not exist %s',label_lookup_path)
        #还有FastGFile,无阻塞
        uid_human_file = tf.gfile.GFile(uid_lookup_path)
        uid_human_list = uid_human_file.readlines()
        #创建空字典
        uid_to_human = {}
        for line in uid_human_list:
            #line.strip()会把'\\n'（空行）替换为''
            line = line.strip('\n')
            items = line.split('\t')
            uid_to_human[items[0]] = items[1]

        class_string_file = tf.gfile.GFile(label_lookup_path)
        class_string_list = class_string_file.readlines()
        node_id_to_uid = {}
        for line in class_string_list:
            if line.startswith('  target_class:'):
                target_class = int(line.split(': ')[1])
            if line.startswith('  target_class_string:'):
                target_class_string = line.split(': ')[1]
                node_id_to_uid[target_class] = target_class_string[1:-2]
        node_id_to_name= {}
        for key,value in node_id_to_uid.items():
            if value not in uid_to_human:
                tf.logging.fatal('failed to locate:%s',value)
            name = uid_to_human[value]
            node_id_to_name[key] = name
        return node_id_to_name
    
    def id_to_string(self,node_id):
        print node_id
        if node_id not in self.node_lookup:
            return 'none'
        return self.node_lookup[node_id]

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('softmax:0')
    # 输入图像（jpg格式）数据，得到softmax概率值（一个shape=(1,1008)的向量）
    predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0':image_data})
    # 将结果转为1维数据
    predictions = np.squeeze(predictions)
    # 新建类：ID --> English string label.
    node_lookup = NodeLookup()
    top_5 = predictions.argsort()[-5:][::-1]
    for node_id in top_5:
        human_string = node_lookup.id_to_string(node_id)
        score = predictions[node_id]
        print('%s (score= %.5f)' % (human_string,score))
       