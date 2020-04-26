# develop a classifier for the 5 Celebrity Faces Dataset
from random import choice
from numpy import load
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from matplotlib import pyplot

from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
import keras
from keras.models import load_model
import tensorflow as tf



def extract_face(filename, required_size=(160, 160)):
	# load image from file
	image = Image.open(filename)
	# convert to RGB, if needed
	image = image.convert('RGB')
	# convert to array
	pixels = asarray(image)
	# create the detector, using default weights
	detector = MTCNN()
	# detect faces in the image
	results = detector.detect_faces(pixels)
	# extract the bounding box from the first face
	x1, y1, width, height = results[0]['box']
	# bug fix
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	# extract the face
	face = pixels[y1:y2, x1:x2]
	# resize pixels to the model size
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array



def get_embedding(model, face_pixels):
	# scale pixel values
	model = load_model('facenet_keras.h5')
	face_pixels = face_pixels.astype('float32')
	# standardize pixel values across channels (global)
	mean, std = face_pixels.mean(), face_pixels.std()
	face_pixels = (face_pixels - mean) / std
	# transform face into one sample
	samples = expand_dims(face_pixels, axis=0)
	# make prediction to get embedding
	yhat = model.predict(samples)
	return yhat[0]


def load_ram():
	# load the facenet model
	config = tf.ConfigProto( device_count = {'GPU': 1 , 'CPU': 56} )
	sess = tf.Session(config=config)
	keras.backend.set_session(sess)
	global model
	model = load_model('facenet_keras.h5')
	print('Loaded Model')
	# load faces
	data = load('5-celebrity-faces-dataset.npz')
	testX_faces = data['arr_2']
	# load face embeddings
	data = load('5-celebrity-faces-embeddings.npz')
	trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
	# normalize input vectors
	in_encoder = Normalizer(norm='l2')
	trainX = in_encoder.transform(trainX)
	testX = in_encoder.transform(testX)
	# label encode targets
	global out_encoder
	out_encoder = LabelEncoder()
	out_encoder.fit(trainy)
	trainy = out_encoder.transform(trainy)
	testy = out_encoder.transform(testy)
	# fit model
	model = SVC(kernel='linear', probability=True)
	model.fit(trainX, trainy)
	



def match_pathpack(selection):
	face_pixels = extract_face(selection)
	print(face_pixels)
	print("no problem")
	embedding = get_embedding(model, face_pixels)
	print("problem goes here")
	random_face_emb = embedding
	# prediction for the face
	samples = expand_dims(random_face_emb, axis=0)
	yhat_class = model.predict(samples)
	yhat_prob = model.predict_proba(samples)
	# get name
	class_index = yhat_class[0]
	class_probability = yhat_prob[0,class_index] * 100
	predict_names = out_encoder.inverse_transform(yhat_class)
	print('Predicted: %s (%.3f)' % (predict_names[0], class_probability - 6))
	# plot for fun
	output = predict_names[0]+" ("+str(round(class_probability - 6,2))+" %)"
	return output


def match_video(selection):
	face = Image.open(selection)
	pixels = asarray(face)
	required_size=(160, 160)
	image = Image.fromarray(pixels)
	image = image.resize(required_size)
	face_array = asarray(image)
	print(face_array)
	embedding = get_embedding(model, face_array)
	random_face_emb = embedding
	# prediction for the face
	samples = expand_dims(random_face_emb, axis=0)
	yhat_class = model.predict(samples)
	yhat_prob = model.predict_proba(samples)
	# get name
	class_index = yhat_class[0]
	class_probability = yhat_prob[0,class_index] * 100
	predict_names = out_encoder.inverse_transform(yhat_class)
	print('Predicted: %s (%.3f)' % (predict_names[0], class_probability - 6))
	# plot for fun
	output = predict_names[0]+" ("+str(round(class_probability - 6,2))+" %)"
	return output
