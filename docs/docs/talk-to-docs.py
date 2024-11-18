from gpt_researcher import GPTResearcher
import asyncio


async def get_report(query: str, report_source: str) -> str:
    researcher = GPTResearcher(query=query, report_source=report_source)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report


if __name__ == "__main__":
    query = "分析使用 gpt-researcher 的时候，用 cli 和 pip package 的方式，都如何选择 local 文件夹作为数据源。用中文输出结果"
    report_source = "local"  # "local" or "web"

    report = asyncio.run(get_report(query=query, report_source=report_source))
    print(report)
