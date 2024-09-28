from flask import Flask,request,redirect,session,render_template
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd
from twilio.rest import Client
account_sid = 'AC6c39178118552e384808d7e43192ea6f'
auth_token = '2804f6ae18af9e2d3e38e8cb587b7ad6'
client = Client(account_sid, auth_token)


df=pd.DataFrame()
df2=pd.DataFrame()
app =Flask(__name__)
app.config['SECRET_KEY']='ashwini@111'
@app.route('/')
def home():
	mylist=[]
	df1=pd.read_csv('i.csv')
	for i in range(len(df1)):
		mylist.append(df1['message'][i])
	return render_template('home1.html',list=mylist)                                    #table=df1.to_html())

@app.route('/whatsapp',methods=['GET','POST'])
def whatsapp_reply():
	global df
	global df2
	#print(request.get_data())
	mes=request.get_data()
	i=str(mes)
	o=i.split("=")
	u=str(o[8])
	p=u.split('&')
	lk=str(p[0])
	k1=lk.split('+')
	mesk=str(k1[0])
	#mesf=str(k1[1])
	#number thisukovali 
	u1=str(o[6])
	p1=u1.split('&')
	lk1=str(p1[0])
	phf=''.join(lk1)
	print(phf)
	#append to dataframe
	res=''

	if mesk=='hi' or mesk== "Hi":
		mesf=str(k1[1])
		d={
		'message':mesf,
		'phone':phf
		}
		df=df._append(d,ignore_index=True)
		#df.to_csv('i.csv')
		print(mesf)
		res=MessagingResponse()
		print('this print',res)
		res.message(f'hi si/medam your sl no-{mesf} after finish please reply ok or get my car thank you services by avyuktha softwares')
	if mesk=='get'or mesk=='ok':
		for i in range(len(df)):
			if df['phone'].iloc[i]==phf:
				d={
		      'message':df['message'].iloc[i],
		      'phone':df['phone'].iloc[i]
		      }
				df2=df2._append(d,ignore_index=True)
				df2.to_csv('i.csv')
				message = client.messages.create(
  				from_='whatsapp:+14155238886',
 			 	body='comedy movie chuda vachu kadhara',
  				to=f'whatsapp:{phf}'
				)
				break	

	return str(res)
@app.route('/page')
def page():
	ms=session.get('ms')
	print(ms)
	

if __name__=="__main__":
	app.run(debug=True)




