from gpt_researcher import GPTResearcher
import asyncio


async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return report

if __name__ == "__main__":
    # query = "Talk about companies that raised more than a billion dollars but still failed. What are possible reasons that they failes? In cases where its possible, what could the founder have done differently?"
    query = "Name 5 companies that failed even after raising more than a billion dollars. For each of them, explain what went wrong and what they could have done differently."
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    import pdb; pdb.set_trace();
    print("Report\n--------\n",report)