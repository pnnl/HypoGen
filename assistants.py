from phi.assistant import Assistant
from phi.llm.azure import AzureOpenAIChat
from phi.llm.anthropic import Claude
from phi.tools.exa import ExaTools
from phi.tools.csv_tools import CsvTools
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.tools.pubmed import PubmedTools
from phi.tools.wikipedia import WikipediaTools
from phi.tools.file import FileTools
from knowledgebase import interaction_knowledge_base
from textwrap import dedent
from dotenv import load_dotenv
from rich.pretty import pprint
from pathlib import Path
from shutil import rmtree

load_dotenv()

reports_dir = Path(__file__).parent.joinpath("wip", "reports")
if reports_dir.is_dir():
    rmtree(path=reports_dir, ignore_errors=True)
reports_dir.mkdir(parents=True, exist_ok=True)


analyst = Assistant(
    name= "data analyst",
    llm = AzureOpenAIChat(model="gpt-4o"),
    description="You are a detailed-oriented and very logical analyst with deep knowledge of molecular interactions and solvation structures. Your task is to analyze a CSV dataset containing chemical parameters and their influences on active material solubilization state in a complete aqueous system.",
    tools = [CsvTools(),],
    save_output_to_file=str(reports_dir.joinpath("analysis_report.md")),
    show_tool_calls=True,
    markdown=True,
    #debug_mode=True,
)

generator = Assistant(
    name = "hypothesis generator",
    #llm = Claude(model="claude-3-5-sonnet-20240620"),
    llm = AzureOpenAIChat(model="gpt-4o"),
    description="You are a world-renowned material scientist with deep knowledge of organic materials and molecular interactions. Your task is to generate intermolecular interactions hypotheses based on a provided analytical report.",  
    instructions=[
        "You will be provided with a detailed data analytical report {analysis_report}",
        "This analytical report contains a comprehensive analysis of the solubalization state of the active material (containing functional groups: carboxylate, sulfonate, aromatic rings, ketone) under the influence of each chemical parameter in the dataset. For each parameter, the report explains its definition, influence on solubilization, and potential molecular interactions with each functional group.",
        "Think carefully about the contents of the report and its implications for intermolecular interactions (active material and additives) and solvations, especially focus on intermolecular forces like π-π stacking, hydrogen bonding, electrostatic interactions, hydrophobicity, polarization, aggregation, surfactant, micelle, etc.",
        "Use the `search_knowledge_base` tool to search for relevant information in your knowledge base. Always do this before proceeding to other search tools.",
        "Use the following tools to gather additional relevant background information as needed: - arxiv tool to search for relevant scientific papers - exa search tool for general information - wikipedia tool for basic concepts and definitions - pubmed tool for scientific literature",
        "Carefully read and analyze all the information you have gathered from these sources.",
        "Based on the analytical report and the information you've gathered, generate an article with a list of 2 hypotheses about the intermolecular interactions and solvations, with an emphsis on intermolecular forces and their impact on solubilization.",
        "When writing your hypotheses:- Be specific and detailed in your explanations - Support your hypotheses with evidence from the data report and your research - Consider various aspects of intermolecular interactions and solvations, such as hydrogen bonding, electrostatic interactions, hydrophobicity, polarization, aggregation, surfactant, micelle, etc. - Focus on the impact of these interactions on the solubilization state of the active material in the complete aqueous system - Consider the potential role of the additives in the system and their impact on intermolecular interactions and solvations - Relate your hypotheses to the context of redox flow batteries where applicable",
        "Present your findings in the <hypothesis_format> provided below,",
        "Important reminders: - Do not use phrases like 'based on my knowledge' or 'depending on the information'. - Write in an engaging, informative, and well-structured manner. - Ensure all your hypotheses and explanations are grounded in scientific principles and the information provided. - Include relevant references to support your hypotheses.",
    ],
    knowledge_base=interaction_knowledge_base,
    search_knowledge=True,
    tools = [
        ExaTools(),WikipediaTools(),PubmedTools(),ArxivToolkit(),FileTools(),
    ], 
    show_tool_calls=True, 
    expected_output=dedent(
    """\
    <hypothesis_format>
    ## Title

    - **Overview:** Brief introduction of the topic.
    - **Background:** Provide a brief explanation of the active material and its functional groups.
    - **Summary of the data:** Summarize the main findings from the analytical report.

    ### Hypothesis 1
    {introductory sentences about the hypothesis}
    {provide details/facts/processes from the data, use numbers from the data analysis report as experimental evidence for the hypothesis}
    {provide logical explanations on the hypothesis}

    ### Hypothesis 2
    {introductory sentences about the hypothesis}
    {provide details/facts/processes from the data, use numbers from the data analysis report as experimental evidence for the hypothesis}
    {provide logical explnations on the hypothesis} 

    ## Conclusion
    - **Summary of report:** Recap of the hypotheses generated in the report.
    - **Implications:** What these findings mean for the future, relates to redox flow batter where possible.
    """
    ),  
    debug_mode=True, 
    markdown=True, 
    save_output_to_file=str(reports_dir.joinpath("hypotheses_report.md")),         
)

def analyst_with_uploaded_csv(csv_file):
    # Update all relevant instructions for the analyst
    analyst.instructions = [
        f"You will be provided with a CSV dataset containing experimental statistical correlation data on active materials solubilization state with correlation to different additive descriptors in complete aqueous solution. Here is the dataset: <csv_data>{csv_file}</csv_data>",
        "This dataset reflects how additive chemical descriptors influence active material solubilization state, which additive chemical descriptor can push active material solubilization limit. The experiments are done using active material with different chemicals with different additive descriptors and measuring its solubilization. Note that this is a complete aqueous system, so the solubilization state is the solubility of the active material in water with different additives that have different chemical descriptors."
        "Analyze the data: a) List all the chemical descriptors (column headers) in the dataset. b) For each descriptor, determine its general influence on solubilization: - Positive numbers indicate positive correlation; larger numbers mean stronger positive correlation. - Negative numbers indicate negative correlation; larger negative numbers mean stronger negative correlation. c) Identify any patterns or trends in the data. Be truethful to the data",
        "For example: - If hydroxyl number has -0.4 correlation, that means hydroxyls negatively influence active material solubilization; the more hydroxyls, the less solubilization.- If octanol coefficient has 0.6 correlation, that means octanol positively influences active material solubilization. The higher octanol number, the more solubilization. The larger octanol number means the additives are more hydrophobic or lipophilic. Based on the data, that means more hydrophobic or lipophilic additives can increase active material solubilization."
        "Conduct a comprehensive analysis of the interactions between the active material's functional groups (carboxylate, sulfonate, aromatic rings, ketone) and each chemical parameter. For each parameter: a. Consider its definition and influence on solubilization from steps 2 and 3. b. Explain potential molecular interactions with each functional group. c. Relate these interactions to known chemistry theories. d. Discuss how these interactions might affect the solubilization state.", 
        "Present your analysis in the following format: <analysis> <parameter_name>Name of the chemical parameter</parameter_name><definition>Definition of the chemical parameter</definition><physical_meaning>Physical meaning of the chemical parameter. The physical meaning should relate to additive physical and molecular information. For example, larger the logP number, more molecular hydrophobicity.</physical_meaning><influence>General influence on solubilization (positive/negative, strength)</influence><intermolecular_interactions>Concise explanation of potential molecular interactions with each functional group (carboxylate, sulfonate, aromatic rings, ketone) based on the physical meaning of the parameter</intermolecular_interactions><chemistry_theories>Relation to known chemistry theories (e.g., hydrogen bonding, solvation, dispersion forces, etc.)</chemistry_theories><overall_effect>Summary of how this parameter affects solubilization based on the intermolecular interactions and forces</overall_effect></analysis>",
        "Repeat this format for each chemical parameter in the dataset."
        "Remember to base all your analysis on the provided data. Be thorough and logical in your explanations, and ensure that your conclusions are well-supported by the provided data evidence. Include all chemical parameters analysis in your analytical report, excluding temperature."
    ]
    analyst.tools[0] = CsvTools(csvs=[csv_file])
    report = analyst.run(markdown=True, stream=False)
    return report


if __name__ == "__main__": 
    interaction_knowledge_base.load(recreate=False)
    analytical_report=analyst_with_uploaded_csv("data/heatmap-data.csv")
    pprint(analytical_report)
    generator.print_response(analytical_report, markdown=True)

