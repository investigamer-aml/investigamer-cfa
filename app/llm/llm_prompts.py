import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from sqlalchemy.orm import sessionmaker

from dbb.models import NewsArticle, UseCases

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def generate_news_article_prompt(use_case_description, risk_factors):
    """
    Generates a prompt for creating a news article based on a dynamic use case description and risk factors.

    Args:
    use_case_description (str): A detailed description of the customer, transactions, and regulatory context.
    risk_factors (dict): A dictionary containing the risk analysis results.

    Returns:
    str: A prompt formatted for input to the OpenAI API.
    """
    prompt = f"""
    # Prompt for Generating a News Article Based on a Use Case Description

    # Background:
    # The aim is to create a realistic news article for educational purposes in the financial sector.
    # This simulation helps finance professionals understand risk assessment and compliance in real-world scenarios.

    # Use Case Overview:
    # {use_case_description}

    # Risk Factor Analysis:
    """
    # Dynamically generate the risk factor analysis part of the prompt based on the input dictionary
    for key, value in risk_factors.items():
        prompt += f"- **{key}**: {value}\n"

    prompt += """
    # Task:
    # Generate a news article that:
    # - **Headline**: Clearly summarizes the key issue.
    # - **Introduction**: Provides a brief overview of the situation.
    # - **Body**: Discusses the detailed transaction patterns, regulatory concerns, and implications.
    # - **Conclusion**: Highlights potential consequences and stresses the importance of diligent compliance.

    # Desired Output:
    # A comprehensive, engaging, and informative article suitable for publication in a professional financial newsletter or website.
    """

    return prompt


def generate_news_article_for_use_case(use_case, session):
    """
    Generates a news article for a given use case using OpenAI's API and inserts it into the database.

    Args:
        use_case (UseCases): The use case instance from the database.
        session: The SQLAlchemy session for database transactions.

    Returns:
        int: The ID of the newly created news article.
    """
    prompt = generate_news_article_prompt(use_case.description, use_case.risk_factors)
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", messages=messages, temperature=0, max_tokens=1500
    )
    article_content = response.choices[0].message.content

    # Create and insert new news article into the database
    new_article = NewsArticle(content=article_content, use_case=use_case)
    session.add(new_article)
    session.commit()
    return new_article.id


def update_news_articles(session):
    """
    Iterates through all use cases, generates news articles, inserts them into the news_articles table,
    and updates the news_article foreign key in the use_cases table.

    Args:
        session: The SQLAlchemy session for database transactions.
    """
    use_cases = session.query(UseCases).all()
    for use_case in use_cases:
        try:
            news_article_id = generate_news_article_for_use_case(use_case, session)
            # Link the generated news article with the use case
            use_case.news_article_id = news_article_id
            session.commit()
        except Exception as e:
            print(f"Error processing use case {use_case.id}: {e}")
            session.rollback()


"""
Function: GenerateKYCTestScenario

Input Parameters:
1. showAuxiliaryData: boolean (true/false)
2. decisionOutcome: string ("escalate" or "close")
3. difficultyLevel: string ("easy", "medium", "hard")

Constants:
- ATM_WITHDRAWAL_LIMIT: 5000 (in euros)

Generate a KYC/TM test scenario for the Dutch financial context based on the following rules and input parameters:

1. Persona Generation:
   - Name: [Generate Dutch first and last name]
   - Age: [25-75]
   - Occupation: [Relevant Dutch job title]
   - Family status: [Single/Married/Divorced/Widowed]
   - Brief background: [2-3 sentences]

2. Financial Profile:
   - Monthly income: [€2,000 - €10,000]
   - Savings balance: [€1,000 - €100,000]
   - Investment portfolio: [Yes/No, if Yes: €5,000 - €500,000]

3. Transaction Data:
   - Generate 6 months of detailed transaction data
   - Include regular patterns for all expense categories
   - Inject suspicious transactions/patterns based on difficultyLevel:
     * Easy: 1 suspicious activity
     * Medium: 2 suspicious activities
     * Hard: 3-4 suspicious activities or complex patterns

4. Suspicious Activity:
   - Types: [Large deposit, Unusual withdrawal, Frequent small transactions, International transfer, etc.]
   - Ensure adherence to ATM_WITHDRAWAL_LIMIT for cash withdrawals
   - Amount and frequency should deviate from normal patterns
   - Timing: Distribute within the 6-month period

5. Context and Explanation:
   - Provide a coherent explanation for the suspicious activity
   - Include relevant Dutch cultural, economic, or regulatory factors
   - Align the explanation with the given decisionOutcome

6. Analyst Decision:
   - Correct action: Use the provided decisionOutcome
   - Key factors to consider: [List 3-5 critical points]

7. Difficulty Level:
   - Use the provided difficultyLevel
   - Assign a score: Easy (1-3), Medium (4-7), Hard (8-10)

8. If showAuxiliaryData is true, include:
   - 12-month historical averages for income, expenses, and savings
   - Monthly trends for main transaction categories

9. Quality Assurance:
   - Ensure all data is realistic and consistent for the Dutch context
   - Verify that suspicious activities align with the given decisionOutcome
   - Confirm that the scenario difficulty matches the provided difficultyLevel
   - Check that all cash withdrawals respect the ATM_WITHDRAWAL_LIMIT

Output Format:
Generate a JSON object containing:
- Persona details
- Financial profile
- 6-month transaction data
- Suspicious activity details
- Context and explanation
- Analyst decision criteria
- Difficulty level and score
- Auxiliary data (if showAuxiliaryData is true)

Ensure all numerical data is formatted consistently (e.g., use of decimal points, thousands separators)
"""
