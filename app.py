from flask import Flask, render_template,request,send_file,jsonify
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jithinjose@localhost:5432/download_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

#creates table 'downloads'
class downloadTracker(db.Model):

	__tablename__ = 'downloads'

	id = db.Column(db.Integer,primary_key = True)
	downloadCount = db.Column(db.Integer,nullable = False, unique = False, default=0)


	def __repr__(self):
		return f'<downloadTracker {self.id}{self.downloadCount}>'

'''class visitorTracker(db.Model):
	__tablename__ = 'visitors'

	id = db.Column(db.Integer,primary_key = True)
	visitCount = db.Column(db.Integer, nullable = False, unique = False)

	def __repr__(self):
		return f'<visitorTracker {self.id}{self.visitCount}>'
		'''

db.create_all()
# Home page
@app.route('/')
def index():
	#num = visitorTracker(visitCount=1)
	#db.session.add(num)
	#db.session.commit()
	return render_template('index.html')
'''
@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
'''
# page to download app
@app.route('/download')
def second_page():
	return render_template('download.html')

# page to display analytics
@app.route('/analytics')
def third_page():
	count = downloadTracker.query.filter_by(id=1).first()
	return render_template('analytics.html',data=count.downloadCount)

# This function makes file available to download. Also, stores the number of downloads in database.
@app.route('/uploads/', methods=['GET','POST'])
def download():
	num = downloadTracker.query.filter_by(id=1).first()
	num.downloadCount+=1
	db.session.commit()
	return send_file('music_demo.zip',as_attachment=True)
