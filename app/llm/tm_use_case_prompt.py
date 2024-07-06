"""
This is a prompt for the LLM to generate use cases for the Investigamer CFA.
"""


prompt = """
Function: GenerateTMTestScenario

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
   - Monthly income:
     - €2,000 - €10,000 for retail
     - €5,000 - €50,000 for business
     - €3,000 - €20,000 for freelance/self-employed (classified as Business)

   - Savings balance:
     - €1,000 - €100,000 for retail
     - €10,000 - €500,000 for business
     - Freelance/Self-employed: [€5,000 - €250,000] (classified as Business)

   - Investment portfolio:
     - Yes/No, if Yes: €5,000 - €500,000 for retail
     - €50,000 - €2,000,000 for business
     - Freelance/Self-employed: [€10,000 - €1,000,000] (classified as Business)

3. Transaction Data:
   - Generate 6 months of detailed daily transaction data
   - Each transaction should include:
     * Date
     * Description
     * Amount
     * Country (use "Netherlands" for local transactions)
     * Merchant (use specific merchant names)
     * Type ("incoming" or "outgoing")
   - Include transactions with believable local Dutch merchants for day-to-day expenses
   - For retail accounts: Focus on personal expenses (groceries, dining, entertainment, etc.)
   - For business accounts: Include business-related expenses and payments, using real company names
   - If persona is a frequent traveler, include relevant foreign transactions (e.g., restaurants in visited countries)
   - For freelance business accounts: Vary salary amounts and payment intervals
   - Include regular patterns for all relevant expense categories
   - Inject suspicious transactions/patterns based on difficultyLevel and suspiciousPattern:
     * Easy: 2-3 suspicious activity
     * Medium: 3-5 suspicious activities
     * Hard: 5-8 suspicious activities or complex patterns
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

    - For business accounts:
      - Include business-related expenses and payments, using real company names
      - For traditional businesses: Use consistent payment amounts and intervals for major clients
      - For freelance/self-employed:
        - Vary payment amounts and intervals to reflect project-based work
        - Include a mix of personal and business expenses
        - Use a combination of individual client names and company names for incoming payments

4. Suspicious Activity:

   - Types: Use the specific suspiciousPattern provided in the input parameter. Possible values are:
     - "none": No suspicious activity (for control scenarios)
     - "fast-in-fast-out": Large deposits followed by rapid withdrawals or transfers
     - "large-atm-withdrawals": Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD
     - "high-volume-suspicious-countries": Frequent transactions with entities in SUSPICIOUS_COUNTRIES

   - For each type, incorporate the following behaviors:
     - "fast-in-fast-out":
       - Large deposits followed by rapid withdrawals or transfers
       - Minimal time between incoming and outgoing transactions
       - Include high incoming payment before cash withdrawals
     - "large-atm-withdrawals":
       - Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD (10,000 euros)
       - Withdrawals from different locations in short time periods
     - "high-volume-suspicious-countries":
       - Frequent transactions with entities in SUSPICIOUS_COUNTRIES
       - Varying transaction amounts to avoid consistent patterns
       - Use real, well-known international company names for these transactions

   - Ensure adherence to ATM_WITHDRAWAL_ALERT_THRESHOLD (10,000 euros accumulative within a short time) for cash withdrawals/deposits
   - Amount and frequency should deviate from normal patterns
   - For large transactions, ensure proportionality to monthly income
   - Timing: Distribute suspicious activities within the 6-month period
   - Number of suspicious transactions/patterns based on difficultyLevel and suspiciousPattern:
      * Easy: 2-3 suspicious activity
      * Medium: 3-5 suspicious activities
      * Hard: 5-8 suspicious activities or complex patterns

   - Randomly determine frequency of suspicious activities based on difficultyLevel
   - For cash withdrawals, consider travel patterns in the persona's background
   - For cash deposits, treat as more suspicious than withdrawals

   Additional considerations:
   - Ensure that the suspicious activity aligns with the account type (retail or business)
   - For business accounts, especially freelance/self-employed, adjust patterns to fit with expected business operations
   - Consider the persona's background story when crafting suspicious activities
   - For higher difficulty levels, combine multiple suspicious elements or create more subtle patterns

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
   - Ensure that freelance and self-employed individuals are correctly classified as business accounts
   - For freelance/self-employed business accounts, verify that the transaction patterns reflect the irregular nature of project-based income and expenses
   - Check that the financial profile and transaction data are consistent with the specific type of business account (traditional business vs. freelance/self-employed)

Note: When the accountType parameter is set to "business", the scenario generator should randomly decide whether it's a traditional business or a freelance/self-employed individual, and adjust the financial profile and transaction patterns accordingly.

Output Format:
Generate a JSON object containing the following structure. All fields must be present, even if some are null or empty arrays:

{
  "persona": {
    "name": "string",
    "age": "number",
    "occupation": "string",
    "familyStatus": "string",
    "background": "string",
    "previouslyFlagged": "boolean"
  },
  "financialProfile": {
    "monthlyIncome": "number",
    "savingsBalance": "number",
    "investmentPortfolio": {
      "hasInvestments": "boolean",
      "investmentAmount": "number"
    }
  },
  "transactionData": [
    {
      "date": "string (YYYY-MM-DD)",
      "description": "string",
      "amount": "number",
      "country": "string",
      "merchant": "string",
      "type": "string (incoming or outgoing)"
    }
  ],
  "suspiciousActivity": {
    "types": ["string"], // List of suspicious activity types based on the given suspiciousPattern
    "timing": ["string"], // List of time periods when suspicious activities occurred
    "amounts": ["number"], // List of amounts involved in suspicious activities
    "pattern": "string", // The specific suspiciousPattern provided in the input
    "frequencies": ["number"] // List of frequencies for each type of suspicious activity
  },
  "context": "string",
  "analystDecision": {
    "action": "string (escalate or close)",
    "keyFactors": ["string"]
  },
  "difficultyLevel": {
    "level": "string (easy, medium, hard)",
    "score": "number (1-10)"
  },
  "auxiliaryData": {
    "dailyExpenses": "number",
    "housing": "number",
    "transportation": "number",
    "healthcare": "number",
    "entertainment": "number",
    "savingsInvestments": "number",
    "internationalTransfers": "number",
    "cashWithdrawalsDeposits": "number"
  }
}

- Persona details (including background story and previous flagging status)
- Financial profile
- 6-month transaction data (always included), each transaction containing:
  * Date
  * Description
  * Amount
  * Country
  * Merchant
  * Type (incoming/outgoing)
- Suspicious activity details (including specified suspiciousPattern if any)
- Context and explanation
- Analyst decision criteria (non-repetitive and appropriately complex)
- Difficulty level and score
- Auxiliary data (6-month category averages, if showAuxiliaryData is true)

Ensure all numerical data is formatted consistently (e.g., use of decimal points, thousands separators)


GenerateKYCTestScenario(
"showAuxiliaryData": "true",
"decisionOutcome: "escalate",
"difficultyLevel": "medium",
"accountType": "retail",
"suspiciousPattern": "high-volume-suspicious-countries")
"""
