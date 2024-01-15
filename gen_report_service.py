from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from gpt_researcher import GPTResearcher
import asyncio
from fastapi import FastAPI, BackgroundTasks
from sse_starlette.sse import EventSourceResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import asyncio
from gpt_researcher import GPTResearcher
from pydantic import BaseModel
from summarization import summarize_single_report
from dotenv import load_dotenv
import os
load_dotenv()

# Access environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
serpapi_key = os.getenv('SERPER_API_KEY')


report_type = "research_report"
async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return report


class QueryItem(BaseModel):
    query: str
    # description: str | None = None
    # price: float
    # tax: float | None = None


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/generate_report/")
async def create_report(query: QueryItem):
    # global report_type
    # print("query.query = ",query.query)
    # print("type = ",query)

    
    report = await get_report(query.query, report_type)
    return {"report": report}

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

if __name__ == '__main__':
    report = """# Analysis of High-Profile Startup Failures: A Post-Mortem of Billion-Dollar Losses


The startup ecosystem is a high-stakes environment where innovation, market fit, and capital converge to create new industry leaders or cautionary tales of failure. Despite the allure of success and the potential for exponential growth, the reality is that many startups face an uphill battle, with a significant number failing to achieve their objectives. This report delves into the stories of five companies that, despite raising over a billion dollars in funding, ultimately succumbed to various challenges. We will explore the factors that contributed to their downfall and consider strategic alternatives that might have altered their outcomes.


## WeWork: The Co-Working Space That Overreached


WeWork, once a darling of the startup world, raised more than $11 billion before its initial public offering (IPO) and filed for bankruptcy in November 2023 (Business Insider, 2023). The company's rapid expansion, fueled by the vision of creating a global network of co-working spaces, was met with enthusiasm by investors. However, WeWork's aggressive growth strategy, coupled with questionable governance practices and a lack of a clear path to profitability, led to its undoing.


### What Went Wrong


1. **Overvaluation and Overexpansion**: WeWork's valuation soared to $47 billion at its peak, driven by the narrative of being a tech company rather than a real estate venture. This led to unchecked expansion and investment in ventures that were not core to its business model.

2. **Governance Issues**: The company's governance came under scrutiny, with concerns about the CEO's behavior and potential conflicts of interest, which eroded investor confidence.

3. **Unsustainable Business Model**: WeWork's long-term lease obligations contrasted with the short-term leases it offered to customers, creating a mismatch that exposed the company to significant risk if demand waned.


### Strategic Alternatives


- **Focus on Core Business**: WeWork could have focused on consolidating its position in key markets and ensuring profitability in its core co-working business before diversifying.

- **Improve Governance**: Implementing robust governance practices and addressing conflicts of interest would have been crucial in maintaining investor trust.

- **Financial Prudence**: A more conservative approach to expansion, with a focus on sustainable growth and profitability, might have prevented the liquidity crisis that led to bankruptcy.


## Zume: The Robotic Pizza Venture That Couldn't Deliver


Zume, a pizza startup that raised nearly $500 million, shut down in June 2023 after struggling to make its pizza automation technology work (Business Insider, 2023). The company aimed to revolutionize the food delivery industry with robots that could prepare pizzas en route to customers.


### What Went Wrong


1. **Technological Challenges**: Zume's core technology, which involved cooking pizzas in transit with robotic assistance, faced significant operational hurdles that proved difficult to overcome.

2. **Market Misjudgment**: The company may have overestimated the market's readiness for such a high level of automation in food preparation and delivery.

3. **Burn Rate**: Zume's high cash burn rate, driven by technology development and operational costs, outpaced its revenue generation, leading to financial instability.


### Strategic Alternatives


- **Pilot Programs**: Zume could have initiated smaller-scale pilot programs to refine its technology and business model before scaling up.

- **Diversification of Offerings**: Expanding the menu to include items that did not require complex automation might have provided additional revenue streams.

- **Partnerships**: Forming strategic partnerships with existing food delivery services could have reduced operational costs and facilitated market entry.


## Convoy: The "Uber for Trucking" That Ran Out of Road


Convoy, a freight startup hailed as the "Uber for trucking," raised over $1 billion but shut down in November 2023 (Business Insider, 2023). The company sought to disrupt the freight industry by connecting shippers with truckers through its app, optimizing logistics and reducing empty miles.


### What Went Wrong


1. **Competitive Market**: The freight industry is highly competitive, with established players and other startups vying for market share.

2. **Operational Complexity**: Managing the logistics of freight matching is complex, and Convoy may have underestimated the challenges involved.

3. **Economic Downturn**: The broader economic downturn likely affected the demand for freight services, impacting Convoy's revenue and growth prospects.


### Strategic Alternatives


- **Niche Focus**: Convoy could have targeted specific segments of the freight market where it could offer distinct advantages over competitors.

- **Incremental Growth**: A more gradual approach to scaling, focusing on building a solid customer base and operational efficiency, might have been more sustainable.

- **Cost Management**: Tighter control over expenses, particularly during economic uncertainty, could have extended Convoy's runway and allowed for strategic pivots.


## Quibi: The Short-Form Streaming Service That Fell Short


Quibi, founded by industry veterans, raised $1.75 billion with the promise of revolutionizing short-form, serialized video content (TMS Outsource, 2023). Despite high production values and a substantial marketing push, Quibi failed to attract a large audience and shut down within six months of its launch.


### What Went Wrong


1. **Content Format Mismatch**: Quibi's focus on short-form content designed for mobile viewing did not resonate with viewers as expected.

2. **Timing**: Launching in April 2020, Quibi faced the unforeseen challenge of the COVID-19 pandemic, which altered potential users' media consumption habits.

3. **Monetization Issues**: The subscription-based model, coupled with a lack of compelling content to justify the cost, led to low subscriber numbers.


### Strategic Alternatives


- **Content Strategy Reevaluation**: Quibi could have tested different content formats and lengths to determine what resonated with audiences before fully committing to its model.

- **Flexible Monetization**: Introducing a freemium model with ad-supported content might have attracted a broader user base and provided a more gradual path to monetization.

- **Strategic Partnerships**: Collaborating with established streaming platforms could have provided Quibi with a ready-made audience and reduced customer acquisition costs.


## Theranos: The Blood-Testing Biotech That Bled Out


Theranos, founded by Elizabeth Holmes, claimed to have developed revolutionary blood-testing technology that could perform a wide range of tests with just a few drops of blood. The company raised over $700 million but was eventually exposed for fraudulent practices, leading to its collapse (CNBC, 2020).


### What Went Wrong


1. **Technological Misrepresentation**: Theranos's technology was not capable of performing the tests it claimed, leading to regulatory and legal issues.

2. **Cultural Issues**: A culture of secrecy and fear prevented employees from raising concerns about the technology's capabilities.

3. **Leadership Misconduct**: The company's leadership, particularly Holmes, engaged in deceptive practices to secure funding and partnerships.


### Strategic Alternatives


- **Transparency**: Theranos could have been transparent about the capabilities and limitations of its technology, allowing for a more honest assessment of its potential.

- **Ethical Leadership**: A leadership team committed to ethical practices and open communication might have prevented the fraudulent activities that led to the company's downfall.

- **Regulatory Compliance**: Ensuring that the technology met regulatory standards before commercialization could have averted the legal challenges that contributed to Theranos's demise.


## Conclusion


The failure of these startups, despite significant funding, underscores the complexity of building a successful company. Factors such as market fit, operational execution, governance, and financial management play critical roles in determining a startup's fate. While hindsight provides clarity on what could have been done differently, the reality is that each company faced unique challenges that required nuanced solutions. The lessons learned from these failures can inform future entrepreneurs and investors as they navigate the high-risk, high-reward world of startups.


## References


Business Insider. (2023). Failed venture capital startups burnt $27 billion - PitchBook. Retrieved from https://www.businessinsider.com/failed-venture-capital-startups-burnt-27-billion-pitchbook-2023-12


CNBC. (2020). 5 of the biggest tech start-up failures ever. Retrieved from https://www.cnbc.com/2020/09/01/worst-tech-start-up-failures-cb-insights.html
"""
    output =  summarize_single_report(report)
