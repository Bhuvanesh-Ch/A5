
from flask import Flask, request, jsonify, render_template
import pickle
import helper

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    q1=int_features[0]
    q2=int_features[1]
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        output='Duplicate'
    else:
        output='Not Duplicate'
   

    return render_template('index.html', prediction_text='The given questions are  {}'.format(output))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    #For direct API calls trought request
'''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
'''
if __name__ == "__main__":
    app.run(debug=True)





'''import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')


'''