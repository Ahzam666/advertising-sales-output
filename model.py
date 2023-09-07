import pickle
import streamlit as st

pickle_file_path = 'model.pkl'

# Load the model from the pickle file
with open(pickle_file_path, 'rb') as file:
    my_model = pickle.load(file)


def main():
    st.title('Advertisement')
    TV = st.number_input('TV')

    RADIO = st.number_input('RADIO')
    Social_media = st.number_input('Social media')
    influencer_mega = st.selectbox('mega', [1,0])
    influencer_micro = st.selectbox('micro', [1,0])
    influencer_nano = st.selectbox('nano', [1,0])
    if st.button('Predict'):
        makeprediction = my_model.predict([[TV,RADIO,Social_media,influencer_mega,influencer_micro,influencer_nano]])
        output = round(makeprediction[0],2)
        st.success(f'sales is {output}')
if __name__ =='__main__':
    main()