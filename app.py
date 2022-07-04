from flask import Flask,render_template,request,make_response,jsonify,session,redirect
app = Flask(__name__)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import pickle


#-----------------------------------------------DATABASE-------------------------------------------------------------------
import sqlite3
conn = sqlite3.connect('mysqlite.db',check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS register
             (username text,email text,password text)''')			
conn.commit()
conn.close()


#----------------------------------------------------------------------------------------------------------------------------




@app.route('/',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        data=request.get_json()
        if data['which_condiction']=="signup":
            print("signup")
            conn = sqlite3.connect('mysqlite.db',check_same_thread=False)
            c = conn.cursor()
            c.execute("SELECT * FROM register")
            for query_result in c.fetchall():
                if data['username'] in query_result:
                    return "exists"
                else:  
                    pass   
            password = bytes(data['password'], 'utf-8')
            password = hashing(password)
            data['password']=password
            c.execute("""INSERT INTO register (username,email,password) values (?,?,?)""",(data['username'],data['email'],data['password']))
            conn.commit()
            return "success"
        elif data['which_condiction']=="login":
            print("login")
            conn = sqlite3.connect('mysqlite.db',check_same_thread=False)
            c = conn.cursor()
            c.execute("SELECT * FROM register WHERE username=?", ( data['username'],))
            result = c.fetchall()
            if len(result)==0:     
                return "no"
            for i in result:
                if verify_pass(i[2],data['password']):
                    return "success"
                else:
                    return "error"

    return render_template("login.html")


@app.route('/home',methods=['GET','POST'])
def Home():
    if request.method == 'POST':
        data=request.get_json()

        a=int(data['event_month'])
        b=int(data['fatality_count'])
        c=int(data['injury_count'])
        d=int(data['population'])
        e=float(data['longitude'])
        f=float(data['latitude'])
        g=int(data['landslide_category_complexity'])
        h=int(data['landslide_category_creep'])
        i=int(data['landslide_category_debris_flow'])
        j=int(data['landslide_category_earth_fall'])
        k=int(data['landslide_category_earth_flow'])
        l=int(data['landslide_category_lahar'])
        m=int(data['landslide_category_rock_fall'])
        n=int(data['landslide_category_slide'])
        o=int(data['landslide_category_snow_avalanche'])
        p=int(data['landslide_size_large'])
        q=int(data['landslide_size_medium'])
        r=int(data['landslide_size_small'])
        s=int(data['landslide_size_unknown'])

        new_val=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]
        loaded_model = pickle.load(open("model.pkl", 'rb'))
        en=loaded_model.predict([new_val])

        if en==0:
            return("Construction")
        elif en==1:
            return("Earthquake")
        elif en==2:
            return("Flooding")
        elif en==3:
            return("Mining")
        elif en==4:
            return("Monsoon")
        elif en==5:
            return("Rain")
        elif en==6:
            return("Snow")
        elif en==7:
            return("Tropical_Cyclone")

    return render_template("home.html")





def hashing(password):
    pw_hash = bcrypt.generate_password_hash(password)
    return pw_hash
def verify_pass(password,password1):
    return bcrypt.check_password_hash(password,password1)


if __name__=="__main__":
    app.run()
    app.run(debug=True)