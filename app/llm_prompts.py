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
