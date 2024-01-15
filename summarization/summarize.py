import sys
# sys.path.insert(0, '/Users/rohanjoshi/anaconda3/envs/news_engine_product/lib/python3.8/site-packages')
# sys.path.insert(0, '/Users/rohanjoshi/Projects/learn/NewsEngine/src')
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


# from search.article import Article
from summarization.prompt_template import PromptTemplateHelper

from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
import textwrap

# def summarize_single_report(report, request_task):
def summarize_single_report(report):
    
    # llm_2 = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106", openopenai_api_key="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")
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    # llm_chain = LLMChain(llm=llm, prompt=prompt)
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-1106-preview")


    # import pdb; pdb.set_trace();
    


    # import pdb; pdb.set_trace();
    # text_to_summarize = article.content
    output_script = ""
    split_rep = report.split("\n## ")
    output_title = None
    output_summary = ""
    num_of_chunks = 4
    list_of_chunks = []
    list_of_chunks.append("\n## ".join(split_rep[:len(split_rep)//num_of_chunks]))
    list_of_chunks.append("\n## ".join(split_rep[len(split_rep)//num_of_chunks:2*len(split_rep)//num_of_chunks]))
    list_of_chunks.append("\n## ".join(split_rep[2*len(split_rep)//num_of_chunks: 3*len(split_rep)//num_of_chunks ]))
    list_of_chunks.append("\n## ".join(split_rep[3*len(split_rep)//num_of_chunks:  ]))

        

    count = 0
    for report in list_of_chunks:

        count += 1


        

        text_to_summarize = report
        text_splitter = CharacterTextSplitter()
        texts = text_splitter.split_text(text_to_summarize)
        # import pdb; pdb.set_trace();
        docs = [Document(page_content = t) for t in texts]
        
        
        # levels_to_summarize = ["beginner"]
        # output = {}
        # for level in levels_to_summarize:
        if count ==1:
            SCRIPT_PROMPT = PromptTemplate(
                # template=PromptTemplateHelper.get_text_prompt_template(request_task=request_task), 
                template=PromptTemplateHelper.get_text_prompt_template(), 
                input_variables=["text"])
        elif count ==2:
            SCRIPT_PROMPT = PromptTemplate(
                # template=PromptTemplateHelper.get_text_prompt_template(request_task=request_task), 
                template=PromptTemplateHelper.prompt_continuation_wo_end_template, 
                input_variables=["text"])
        elif count ==3:
            SCRIPT_PROMPT = PromptTemplate(
                # template=PromptTemplateHelper.get_text_prompt_template(request_task=request_task), 
                template=PromptTemplateHelper.prompt_continuation_wo_end_template, 
                input_variables=["text"])
        else:
            SCRIPT_PROMPT = PromptTemplate(
                # template=PromptTemplateHelper.get_text_prompt_template(request_task=request_task), 
                template=PromptTemplateHelper.prompt_continuation_template, 
                input_variables=["text"])
            
            
        SUMMARY_PROMPT = PromptTemplate(
            template=PromptTemplateHelper.get_summary_prompt_template(subject="the subject", level= "beginner"), 
            input_variables=["text"])
            
            
        # get_title_prompt_template
        TITLE_PROMPT = PromptTemplate(
            template=PromptTemplateHelper.get_title_prompt_template(subject="the subject", level= "beginner"), 
            input_variables=["text"])

                

        # chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt = PROMPT, combine_prompt=PROMPT)
        # print("PROMPT =",PROMPT)
        llm_chain = LLMChain(llm=llm, prompt=SCRIPT_PROMPT)

        # Define StuffDocumentsChain
        script_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

        # docs = loader.load()

        script = script_chain.run(docs)
        print("Script = \n",script)

        output_script += script+"\n"
            

            
        summary_llm_chain = LLMChain(llm=llm, prompt=SUMMARY_PROMPT)

        # Define StuffDocumentsChain
        summary_chain = StuffDocumentsChain(llm_chain=summary_llm_chain, document_variable_name="text")

        # docs = loader.load()


        output_summary = summary_chain.run(docs)

        # print("output_summary = ",output_summary)

        summarized_text = output_summary
        output_summary += summarized_text + "\n"

        # question_prompt_tempalte = """Based on the information below, what are some really interesting questions that a beginner in economics would ask. 
        # {text} 
        # """
        title_llm_chain = LLMChain(llm=llm, prompt=TITLE_PROMPT)

        # Define StuffDocumentsChain
        title_chain = StuffDocumentsChain(llm_chain=title_llm_chain, document_variable_name="text")
        
        title = title_chain.run(docs)
        # print("Title = ",title)
        if output_title is None:
            output_title = title

        

    import pdb; pdb.set_trace();
    
    output = {'title': output_title, 'summary': output_summary, 'script': output_script}
    # print(question_text)
    # output[level] = {}
    # output[level]['questions'] = questions
    # output[level]['summary'] = summarized_text
    # output[level]['script'] = script
    # output[level]['title'] = title
    # article.summary[level] = {}
    # article.summary[level]['questions'] = questions
    # article.summary[level]['summary'] = summarized_text
    # article.summary[level]['script'] = script
    # article.summary[level]['title'] = title
    return output
    
# def summarize_all_articles_into_one(articles_list, level='intermediate'):

#     # print("Only summarizing intermediate level posts")

#     output_text = ""

#     for article in articles_list:
#         output_text += article.summary[level]['summary']+"\n"
    

#     return output_text
