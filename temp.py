from gpt_researcher import GPTResearcher
import asyncio


async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return report

if __name__ == "__main__":
    query = "When people say that the fed is increasing interest rates, what does it mean? Create a report about these interest rates?"
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    import pdb; pdb.set_trace();
    print("Report\n--------\n",report)