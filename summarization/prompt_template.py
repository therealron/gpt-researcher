

class PromptTemplateHelper:
    # beginner_

    
    prompt_template = """Based on the information below, write an elaborate personalized script that clearly goes through the entire report as if it is covered on a 10 minute show run by two friends, a curious chap named Zylo and an expert named Jaxi. You will be provided a section of a very long report, so create the script such that we can easily edit the show, by continuing it with another clip of another section, so don't make anyone end the show by saying anything like "That's all we have for today" or "thank you for joining". Ensure that all points are covered, but just end as though the conversation is still not finished. Zylo will ask questions that a beginner would ask and through their conversation, provide the whole information but don't include things like 'click here to learn more'. Make sure to go through the entire report even if it means that the script will be too long. This show will be heard by a listener, so make Zylo greet them. Start the script as  
    'Zylo: Hello everyone, and a warm welcome to the Zylo and Jaxi Show!' Continue the opening sentence by providing some context about the info with an engaging headline. Make it a clear, elaborate and intriguing script.
    {text}
    
    Script:
    
    """

    prompt_continuation_template = """Based on the information below, write an elaborate personalized script that clearly goes through the entire report as if it is covered on a 10 minute show run by two friends, a curious chap named Zylo and an expert named Jaxi. Zylo will ask questions that a beginner would ask and through their conversation, provide the whole information but don't include things like 'click here to learn more'. Make sure to go through the entire report even if it means that the script will be too long. This show will be a continuation of another show, so don't make Zylo greet the listener or make it awkward. Start the conversation as though it is a continuation of a discussion of the report and they are starting the discussion of a new section now. Make it a clear, elaborate and intriguing script. Make Jaxi gracefully end the show and invite the listeners to request a new podcast for a topic of their choice. 
    {text}
    
    Script:
    
    """
    prompt_continuation_wo_end_template = """Based on the information below, write an elaborate personalized script that clearly goes through the entire report as if it is covered on a 10 minute show run by two friends, a curious chap named Zylo and an expert named Jaxi. Zylo will ask questions that a beginner would ask and through their conversation, provide the whole information but don't include things like 'click here to learn more'. Make sure to go through the entire report even if it means that the script will be too long. This show will be a continuation of another show, so don't make Zylo greet the listener or make it awkward. Start the conversation as though it is a continuation of a discussion of the report and they are starting the discussion of a new section now. Make it a clear, elaborate and intriguing script. 
     Don't end the show, because we will continue the show with another clip so just ensure that Jaxi gets the last word but doesn't give a hint of ending the show. 
    {text}
    
    Script:
    
    """

    prompt_concise_template = """Based on the information below, write a short script that concisely summarizes the main points of this information as if it is covered on a show run by two friends, a curious chap named Zylo and an expert named Jaxi. You used to be a hollywood script write and are now hired to write news scripts to make them concise and interesting. Zylo will ask questions that a beginner would ask and through their conversation, summarize the whole information but don't include things like 'click here to learn more'. This show will be heard by a listener, so make Zylo greet them. Start the script as  
    'Zylo: Hello everyone, and a warm welcome to the Zylo and Jaxi Show!' Continue the opening sentence by providing some context about the info with an engaging headline. Make it a short, concise and intriguing script.
    {text}
    Script:
    
    """

    headline_prompt_template = """Based on the information below, create a 3 or 4 word title that is engaging, in very simple terms but not click-bait.   
    {text}
    Headline:
    """


    summary_prompt_template = """Based on the information below, write a concise summary in bullet points. Write like in the style of a high-signal, twitter user who writes in simple terms, and straight to the point.
    {text}
    Summary:
    """

    summary_prompt_3_points_template = """Based on the information below, write a concise summary in 3 points. Number each point from 1-3. Each point should be 10-12 words only. Write like in the style of a high-signal, twitter user who writes in simple terms, and straight to the point.
    {text}
    Summary:
    """
    

    question_prompt_template = """Based on the information below, what are some really interesting questions that a {level} in {subject} would ask. 
    {text} 
    """

    @staticmethod
    def get_text_prompt_template(
        # subject: str,
        # level: str
        # request_task: str
    ):

        # return PromptTemplateHelper.prompt_template.format(request=request_task, text="{text}")
        return PromptTemplateHelper.prompt_template.format(text="{text}")

    @staticmethod
    def get_text_prompt_continuation_template(
        # subject: str,
        # level: str
    ):
        return PromptTemplateHelper.prompt_continuation_template.format( text="{text}")
    
    @staticmethod
    def get_summary_prompt_template(
        subject: str,
        level: str
    ):
        return PromptTemplateHelper.summary_prompt_template.format(subject= subject, level=level, text="{text}")
    
    
    
    @staticmethod
    def get_title_prompt_template(
        subject: str,
        level: str
    ):
        return PromptTemplateHelper.headline_prompt_template.format(subject= subject, level=level, text="{text}")

    @staticmethod 
    def get_question_prompt_template(
        subject: str,
        level: str,
    ):
        return PromptTemplateHelper.question_prompt_template.format(subject= subject, level=level, text="{text}")


# class AllArticleSummarizerHelper:


if __name__ == '__main__':
    
    print(PromptTemplate.get_text_prompt_template("economics", "advanced"))