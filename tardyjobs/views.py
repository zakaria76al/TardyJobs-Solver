from flask import Flask, request, render_template, send_file
from sys import maxsize
from itertools import permutations
import copy
import random
import time
import pandas as pd
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from tardyjobs.appFunctions import dynamicP1
from tardyjobs.appFunctions import dynamicP2
from tardyjobs.appFunctions import amh as algmh
from tardyjobs.appFunctions import gvnsP1
from tardyjobs.appFunctions import gvnsP2
from tardyjobs.appFunctions import gantt
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import rstr

def saveFile(dataFile, fileName):
		#fileName = os.path.join(app.config['UPLOAD_FOLDER'], dataFile.filename.split('.')[0]+".txt")
		dataFile.save(fileName)

UPLOAD_FOLDER = "/app/tardyjobs/files/uploads/"


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/files/<path:filename>', methods=['get','post'])
def downloadfilename(filename):
	return send_file("files/" + filename, as_attachment=True)

@app.route('/dynamic', methods=['get','post'])
def dynamic():
	if request.method == 'POST':
		dataFile = request.files['dataFile']
		if(dataFile.filename == ''):
			return render_template('solver.html?file=noFile')
		fileName = os.path.join(app.config['UPLOAD_FOLDER'], dataFile.filename)
		saveFile(dataFile, fileName)
		problem = request.form['problem']
		if problem == "p1":
			data = pd.read_csv(fileName, sep="\t", header=None)
			A = data.values.tolist()
			P = A[1]
			D = A[2]
			tasks = list(range(1, len(P) + 1))
			coutRes, tasksRes = dynamicP1.f(tasks,P,D)
			imgName = gantt.ganttP1(tasksRes, P, D)
		elif problem == "p2":
			data = pd.read_csv(fileName, sep="\t", header=None)
			A = data.values.tolist()
			P = A[1]
			D = A[2]
			H = A[3]
			B = A[4]
			tasks = list(range(1, len(P) + 1))
			coutRes, tasksRes = dynamicP2.f(tasks,P,D,H,B)
			imgName = gantt.ganttP2(tasksRes, P, D, H, B)

		return render_template('results.html', resultat=tasksRes, cout=coutRes, gantt=imgName)
	else:
		return render_template('solver.html', mtd='dynamic')

@app.route('/gvns', methods=['get','post'])
def gvns():
	if request.method == 'POST':
		dataFile = request.files['dataFile']
		if(dataFile.filename == ''):
			return render_template('solver.html?file=noFile')
		fileName = os.path.join(app.config['UPLOAD_FOLDER'], dataFile.filename)
		saveFile(dataFile, fileName)
		problem = request.form['problem']
		if problem == "p1":
			data = pd.read_csv(fileName, sep="\t", header=None)
			A = data.values.tolist()
			P = A[1]
			D = A[2]
			tasks = list(range(1, len(P) + 1))
			coutRes, tasksRes = gvnsP1.GVNS(tasks,P,D)
			print("\n\n")
			print(tasksRes)
			imgName = gantt.ganttP1(tasksRes, P, D)
		elif problem == "p2":
			data = pd.read_csv(fileName, sep="\t", header=None)
			A = data.values.tolist()
			P = A[1]
			D = A[2]
			H = A[3]
			B = A[4]
			tasks = list(range(1, len(P) + 1))
			coutRes, tasksRes = gvnsP2.GVNS(tasks,P,D,H,B)
			imgName = gantt.ganttP2(tasksRes, P, D, H, B)
		return render_template('results.html', resultat=tasksRes , P=P, cout=coutRes, gantt=imgName)
	else:
		return render_template('solver.html', mtd='gvns')

@app.route('/amh', methods=['get','post'])
def amh():
	if request.method == 'POST':
		dataFile = request.files['dataFile']
		if(dataFile.filename == ''):
			return render_template('solver.html?file=noFile')
		fileName = os.path.join(app.config['UPLOAD_FOLDER'], dataFile.filename)
		saveFile(dataFile, fileName)
		problem = request.form['problem']
		if problem == "p1":
			data = pd.read_csv(fileName, sep="\t", header=None)
			A = data.values.tolist()
			P = A[1]
			D = A[2]
			tasks = list(range(1, len(P) + 1))
			coutRes, tasksRes = algmh.amhSolver(tasks,P,D)
			imgName = gantt.ganttP1(tasksRes, P, D)
		else:
			return render_template('solver.html', mtd='amh', error='true')

		return render_template('results.html', resultat=tasksRes , P=P, cout=coutRes, gantt=imgName)
	else:
		return render_template('solver.html', mtd='amh')

@app.route('/upload', methods=['get','post'])
def upload():
	if request.method == 'POST':
		return render_template('upload.html')
	else:
		return render_template('solver.html')
