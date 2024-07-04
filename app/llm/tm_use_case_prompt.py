"""
This is a prompt for the LLM to generate use cases for the Investigamer CFA.
"""


prompt = """
Function: GenerateKYCTestScenario

Input Parameters:
1. showAuxiliaryData: boolean (true/false)
2. decisionOutcome: string ("escalate" or "close")
3. difficultyLevel: string ("easy", "medium", "hard")
4. accountType: string ("retail", "business")
5. suspiciousPattern: string ("none", "fast-in-fast-out", "large-atm-withdrawals", "high-volume-suspicious-countries")

Constants:
- ATM_WITHDRAWAL_ALERT_THRESHOLD: 10000 (in euros, accumulative within a short time)
- SUSPICIOUS_COUNTRIES: [List of countries known for financial risk]
- WELL_KNOWN_INTERNATIONAL_COMPANIES: [List of real, well-known international companies]

Generate a KYC/TM test scenario for the Dutch financial context based on the following rules and input parameters:

1. Persona Generation:
   - Name: [Generate Dutch first and last name]
   - Age: [25-75]
   - Occupation: [Relevant Dutch job title, matching accountType]
   - Family status: [Single/Married/Divorced/Widowed]
   - Brief background: [3-5 sentences, including randomly determined traits like frequent traveler, young professional, family person, etc.]
   - Previously flagged: [Randomly determine based on difficultyLevel, more likely for higher difficulties]

2. Financial Profile:
   - Monthly income: [€2,000 - €10,000 for retail, €5,000 - €50,000 for business]
   - Savings balance: [€1,000 - €100,000 for retail, €10,000 - €500,000 for business]
   - Investment portfolio: [Yes/No, if Yes: €5,000 - €500,000 for retail, €50,000 - €2,000,000 for business]

3. Transaction Data:
   - Generate 6 months of detailed daily transaction data
   - Include transactions with believable local Dutch merchants for day-to-day expenses
   - For retail accounts: Focus on personal expenses (groceries, dining, entertainment, etc.)
   - For business accounts: Include business-related expenses and payments, using real company names
   - If persona is a frequent traveler, include relevant foreign transactions (e.g., restaurants in visited countries)
   - For freelance business accounts: Vary salary amounts and payment intervals
   - Include regular patterns for all relevant expense categories
   - Inject suspicious transactions/patterns based on difficultyLevel and suspiciousPattern:
     * Easy: 2-3 suspicious activity
     * Medium: 4-5 suspicious activities
     * Hard: 5-10 suspicious activities or complex patterns
   - Randomly determine frequency of suspicious activities based on difficultyLevel
   - If suspiciousPattern is specified, incorporate the following behaviors:
     a. "fast-in-fast-out":
        - Large deposits followed by rapid withdrawals or transfers
        - Minimal time between incoming and outgoing transactions
        - Include high incoming payment before cash withdrawals
     b. "large-atm-withdrawals":
        - Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD
        - Withdrawals from different locations in short time periods
     c. "high-volume-suspicious-countries":
        - Frequent transactions with entities in SUSPICIOUS_COUNTRIES
        - Varying transaction amounts to avoid consistent patterns
        - Use real, well-known international company names for these transactions

4. Suspicious Activity:
   - Types: [Large deposit, Unusual withdrawal, Frequent small transactions, International transfer, Cash deposits, etc.]
   - Ensure adherence to ATM_WITHDRAWAL_ALERT_THRESHOLD for cash withdrawals/deposits
   - Amount and frequency should deviate from normal patterns
   - For large transactions, ensure proportionality to monthly income
   - Timing: Distribute within the 6-month period
   - Incorporate the specified suspiciousPattern if provided
   - For cash withdrawals, consider travel patterns in the persona's background
   - For cash deposits, treat as more suspicious than withdrawals

5. Context and Explanation:
   - Provide a coherent explanation for the suspicious activity
   - Include relevant Dutch cultural, economic, or regulatory factors
   - Align the explanation with the given decisionOutcome
   - If a suspiciousPattern is specified, include relevant details in the context
   - Incorporate the persona's background story into the explanation

6. Analyst Decision:
   - Correct action: Use the provided decisionOutcome
   - Key factors to consider: [List 3-5 non-repetitive, critical points, including aspects of the suspiciousPattern if specified]
   - For complex patterns, ensure the factors reflect the intricacy of the situation

7. Difficulty Level:
   - Use the provided difficultyLevel
   - Assign a score: Easy (1-3), Medium (4-7), Hard (8-10)
   - For hard difficulty, ensure patterns are complex and not immediately obvious

8. Auxiliary Data (if showAuxiliaryData is true):
   Include 6-month averages for the following categories:
   - Daily expenses (groceries, dining out)
   - Housing (rent/mortgage, utilities)
   - Transportation
   - Healthcare
   - Entertainment
   - Savings/Investments
   - International transfers
   - Cash withdrawals/deposits

9. Quality Assurance:
   - Ensure all data is realistic and consistent for the Dutch context
   - Verify that suspicious activities align with the given decisionOutcome and suspiciousPattern
   - Confirm that the scenario difficulty matches the provided difficultyLevel
   - Check that cash withdrawals/deposits respect the ATM_WITHDRAWAL_ALERT_THRESHOLD
   - If a suspiciousPattern is specified, ensure it is prominently featured in the transaction data
   - Verify that the transaction data feels realistic, mimicking a real bank app's level of detail
   - For business accounts, ensure the use of real, well-known international company names where appropriate

Output Format:
Generate a JSON object containing:
- Persona details (including background story and previous flagging status)
- Financial profile
- 6-month transaction data (always included, with local merchant names and day-to-day expenses)
- Suspicious activity details (including specified suspiciousPattern if any)
- Context and explanation
- Analyst decision criteria (non-repetitive and appropriately complex)
- Difficulty level and score
- Auxiliary data (12-month category averages, if showAuxiliaryData is true)

Ensure all numerical data is formatted consistently (e.g., use of decimal points, thousands separators)
"""
