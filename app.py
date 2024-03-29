import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,post_type):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a linkedin post for {post_type}. The details of the post are: {input_text}
        write within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["post_type","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(post_type=post_type,input_text=input_text,no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="LinkedInk",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate post 🚀")

input_text=st.text_input("Enter the post details")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    post_type=st.selectbox('Make a post for',
                            ('new job','new project','new achievement'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,post_type))