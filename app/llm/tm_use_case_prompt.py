"""
This is a prompt for the LLM to generate use cases for the Investigamer CFA.
"""


prompt = """
# KYC/TM Test Scenario Generator Prompt
Version: 1.0.0

## Table of Contents
1. [Function Definition and Input Parameters](#1-function-definition-and-input-parameters)
2. [Usage Examples](#2-usage-examples)
3. [Constants](#3-constants)
4. [Persona Generation](#4-persona-generation)
5. [Financial Profile](#5-financial-profile)
6. [Transaction Data](#6-transaction-data)
   6.1 [General Guidelines](#61-general-guidelines)
   6.2 [Statistical Guidelines](#62-statistical-guidelines)
   6.3 [Dutch Cultural Elements](#63-dutch-cultural-elements)
7. [Suspicious Activity](#7-suspicious-activity)
8. [Context and Explanation](#8-context-and-explanation)
9. [Analyst Decision](#9-analyst-decision)
10. [Difficulty Level and Scoring](#10-difficulty-level-and-scoring)
11. [Auxiliary Data](#11-auxiliary-data)
12. [Quality Assurance](#12-quality-assurance)
13. [Output Format](#13-output-format)
14. [Error Handling](#14-error-handling)

## 1. Function Definition and Input Parameters

Function: GenerateTMTestScenario

Input Parameters:
1. showAuxiliaryData: boolean (true/false)
2. decisionOutcome: string ("escalate" or "close")
3. difficultyLevel: string ("easy", "medium", "hard")
4. accountType: string ("retail", "business")
5. suspiciousPattern: string ("fast-in-fast-out", "large-atm-withdrawals", "high-volume-suspicious-countries")

<important>
Input Parameter Validation:
- Validate each input parameter against its allowed values.
- If any parameter is invalid, immediately halt the scenario generation process and return an error message (see [Error Handling](#14-error-handling)).
</important>

<note>
When accountType is "business", randomly select one of the following subtypes:
1. Traditional Business (80% probability)
2. Freelance/Self-employed (20% probability)
</note>

## 2. Usage Examples

Here are some example inputs and outputs to demonstrate how the GenerateTMTestScenario function should be used:

### Example 1: Easy Retail Scenario

Input:
```json
{
  "showAuxiliaryData": true,
  "decisionOutcome": "close",
  "difficultyLevel": "easy",
  "accountType": "retail",
  "suspiciousPattern": "large-atm-withdrawals"
}
```

Output:
```json
{
  "persona": {
    "name": "Emma de Vries",
    "age": 32,
    "occupation": "Teacher",
    "familyStatus": "Single",
    "background": "Emma is a primary school teacher in Amsterdam. She enjoys traveling during school holidays and is saving up for a home purchase.",
    "previouslyFlagged": false
  },
  "financialProfile": {
    "monthlyIncome": 3500,
    "savingsBalance": 25000,
    "investmentPortfolio": {
      "hasInvestments": true,
      "investmentAmount": 10000
    }
  },
  "transactionData": [
    {
      "date": "2023-01-15",
      "description": "Salary deposit",
      "amount": 3500,
      "country": "Netherlands",
      "merchant": "Amsterdam School District",
      "type": "incoming"
    },
    {
      "date": "2023-01-20",
      "description": "ATM withdrawal",
      "amount": -1000,
      "country": "Netherlands",
      "merchant": "ING ATM Leidseplein",
      "type": "outgoing"
    }
    // ... more transactions ...
  ],
  "suspiciousActivity": {
    "types": ["large-atm-withdrawals"],
    "timing": ["Mid-January 2023", "Early February 2023"],
    "amounts": [1000, 1200],
    "pattern": "large-atm-withdrawals",
    "frequencies": [2]
  },
  "context": "Emma de Vries, a 32-year-old teacher, made two unusually large ATM withdrawals in January and February. However, these coincide with the winter school break, and she has a history of increased cash usage during travel periods.",
  "analystDecision": {
    "action": "close",
    "keyFactors": [
      "Withdrawals align with known travel period",
      "Amount is significant but not extreme for travel expenses",
      "No other suspicious patterns in transaction history"
    ]
  },
  "difficultyLevel": {
    "level": "easy",
    "score": 2
  },
  "auxiliaryData": {
    "dailyExpenses": 800,
    "housing": 1200,
    "transportation": 150,
    "healthcare": 100,
    "entertainment": 300,
    "savingsInvestments": 500,
    "internationalTransfers": 0,
    "cashWithdrawalsDeposits": 400
  }
}
```

### Example 2: Hard Business Scenario

Input:
```json
{
  "showAuxiliaryData": false,
  "decisionOutcome": "escalate",
  "difficultyLevel": "hard",
  "accountType": "business",
  "suspiciousPattern": "high-volume-suspicious-countries"
}
```

Output:
```json
{
  "persona": {
    "name": "Luuk van der Meer",
    "age": 45,
    "occupation": "CEO",
    "familyStatus": "Married",
    "background": "Luuk is the CEO of a medium-sized import/export company based in Rotterdam. The company has been expanding its operations in emerging markets over the past year.",
    "previouslyFlagged": true
  },
  "financialProfile": {
    "monthlyIncome": 25000,
    "savingsBalance": 150000,
    "investmentPortfolio": {
      "hasInvestments": true,
      "investmentAmount": 500000
    }
  },
  "transactionData": [
    {
      "date": "2023-03-01",
      "description": "Payment from Global Trade Ltd",
      "amount": 75000,
      "country": "United Arab Emirates",
      "merchant": "Global Trade Ltd",
      "type": "incoming"
    },
    {
      "date": "2023-03-05",
      "description": "Transfer to Overseas Logistics Co",
      "amount": -50000,
      "country": "Malaysia",
      "merchant": "Overseas Logistics Co",
      "type": "outgoing"
    }
    // ... more transactions ...
  ],
  "suspiciousActivity": {
    "types": ["high-volume-suspicious-countries"],
    "timing": ["Throughout March 2023", "Mid-April 2023", "Late May 2023"],
    "amounts": [75000, 50000, 100000, 80000, 60000],
    "pattern": "high-volume-suspicious-countries",
    "frequencies": [5]
  },
  "context": "Luuk van der Meer's import/export company has seen a significant increase in high-value transactions with entities in countries flagged as high-risk. While this aligns with the company's stated expansion into emerging markets, the volume and frequency of these transactions have raised concerns.",
  "analystDecision": {
    "action": "escalate",
    "keyFactors": [
      "High volume of transactions with high-risk countries",
      "Significant increase in transaction amounts compared to historical data",
      "Previous flagging history on the account",
      "Inconsistent pattern in the flow of funds",
      "Lack of clear business purpose for some transactions"
    ]
  },
  "difficultyLevel": {
    "level": "hard",
    "score": 9
  }
}
```

<note>
These examples demonstrate how the function generates scenarios of varying complexity for different account types and suspicious patterns. The actual output may vary due to the random elements in scenario generation.
</note>

## 3. Constants

- ATM_WITHDRAWAL_ALERT_THRESHOLD: 10000 (in euros, accumulative within a short time)
- SUSPICIOUS_COUNTRIES: [List of countries known for financial risk]
- WELL_KNOWN_INTERNATIONAL_COMPANIES: [List of real, well-known international companies]

## 4. Persona Generation

- Name: [Generate Dutch first and last name]
- Age: [25-75]
- Occupation:
  - If accountType is "retail": [Generate relevant Dutch job title]
  - If accountType is "business":
    - For Traditional Business: [Generate job title such as "Business Owner", "CEO", "Managing Director"]
    - For Freelance/Self-employed: [Generate job title such as "Freelance Designer", "Self-employed Consultant", "Independent Contractor"]
- Family status: [Single/Married/Divorced/Widowed]
- Brief background: [3-5 sentences, including randomly determined traits like frequent traveler, young professional, family person, etc.]
- Previously flagged: [Randomly determine based on difficultyLevel, more likely for higher difficulties]

## 5. Financial Profile

- Monthly income:
  - Retail: [€2,000 - €10,000]
  - Business (Traditional): [€5,000 - €50,000]
  - Business (Freelance/Self-employed): [€3,000 - €20,000]

- Savings balance:
  - Retail: [€1,000 - €100,000]
  - Business (Traditional): [€10,000 - €500,000]
  - Business (Freelance/Self-employed): [€5,000 - €250,000]

- Investment portfolio:
  - Retail:
    - Presence: Yes/No
    - If Yes: [€5,000 - €500,000]
  - Business (Traditional): [€50,000 - €2,000,000]
  - Business (Freelance/Self-employed): [€10,000 - €1,000,000]

## 6. Transaction Data

### 6.1 General Guidelines

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
- If persona is a frequent traveler, include relevant foreign transactions
- For freelance business accounts: Vary salary amounts and payment intervals
- Include regular patterns for all relevant expense categories
- Inject suspicious transactions/patterns based on difficultyLevel and suspiciousPattern

#### Transaction Frequency and Volume Guidelines

   a. Retail Accounts:
      - Daily transactions: 0-3 per day
      - Weekly large transactions: 1-2 per week
      - Monthly recurring transactions: 2-5 per month
      - Quarterly transactions: 1-2 per quarter
      - Total transactions per month: 40-80

   b. Business Accounts (Traditional):
      - Daily transactions: 3-8 per day
      - Weekly large transactions: 1-3 per week
      - Monthly recurring transactions: 5-10 per month
      - Quarterly transactions: 2-3 per quarter
      - Total transactions per month: 80-160

   c. Business Accounts (Freelance/Self-employed):
      - Daily transactions: 1-4 per day
      - Weekly large transactions: 1-2 per week
      - Monthly recurring transactions: 4-8 per month
      - Quarterly transactions: 1-2 per quarter
      - Total transactions per month: 50-125

<note>
- Adjust the number of transactions based on the account's financial profile
- For higher difficulty levels, increase the number of transactions by 10-20%
- Ensure that the transaction volume aligns with the suspicious activity patterns when applicable
- Incorporate seasonal variations in transaction frequency and volume
- Consider weekend vs. weekday patterns
- Distribute transactions across the 6-month period using a weighted random approach
- Ensure recurring transactions occur on consistent dates each month
- Avoid generating transactions on inappropriate days
</note>

### 6.2 Statistical Guidelines

1. Transaction Amount Distributions:
   a. Retail Accounts:
      SMALL_TRANS_RETAIL = {range: [0, 50], percentage: [50, 60]}
      MEDIUM_TRANS_RETAIL = {range: [50, 500], percentage: [30, 40]}
      LARGE_TRANS_RETAIL = {range: [500, Infinity], percentage: [5, 15]}

   b. Business Accounts (Traditional):
      SMALL_TRANS_BUSINESS = {range: [0, 500], percentage: [30, 40]}
      MEDIUM_TRANS_BUSINESS = {range: [500, 5000], percentage: [40, 50]}
      LARGE_TRANS_BUSINESS = {range: [5000, Infinity], percentage: [15, 25]}

   c. Business Accounts (Freelance/Self-employed):
      SMALL_TRANS_FREELANCE = {range: [0, 100], percentage: [40, 50]}
      MEDIUM_TRANS_FREELANCE = {range: [100, 1000], percentage: [35, 45]}
      LARGE_TRANS_FREELANCE = {range: [1000, Infinity], percentage: [10, 20]}

2. Transaction Type Distribution:
   INCOMING_TRANS_PERCENTAGE = [40, 60]
   OUTGOING_TRANS_PERCENTAGE = [60, 40]

3. Recurring Transaction Patterns:
   FIXED_RECURRING_RETAIL = {percentage: [5, 10]}
   FIXED_RECURRING_BUSINESS = {percentage: [3, 7]}
   VARIABLE_RECURRING_RETAIL = {percentage: [3, 7]}
   VARIABLE_RECURRING_BUSINESS = {percentage: [2, 5]}

4. Day of Week Distribution:
   a. Retail Accounts:
      WEEKDAY_TRANS_RETAIL = {percentage: [60, 70]}
      WEEKEND_TRANS_RETAIL = {percentage: [30, 40]}

   b. Business Accounts:
      WEEKDAY_TRANS_BUSINESS = {percentage: [80, 90]}
      WEEKEND_TRANS_BUSINESS = {percentage: [10, 20]}

5. International Transaction Frequency:
   INTERNATIONAL_TRANS_RETAIL = {percentage: [2, 10]}
   INTERNATIONAL_TRANS_BUSINESS = {percentage: [5, 25]}

6. Cash Transaction Frequency:
   CASH_TRANS_RETAIL = {percentage: [5, 15]}
   CASH_TRANS_BUSINESS = {percentage: [1, 10]}

7. Transaction Description Variety:
   MIN_UNIQUE_MERCHANTS_RETAIL = 50
   MIN_UNIQUE_MERCHANTS_BUSINESS = 100

8. Balance Fluctuations:
   // Ensure balance stays within realistic ranges and shows natural growth/decline

9. Seasonal Variations:
   SEASONAL_INCREASE = {percentage: [10, 30]}

10. Correlation with Persona:
    // Ensure transaction patterns align with persona's occupation, age, and background

<note>
- Percentages are represented as ranges [min, max]
- All monetary values are in euros
- Adjust ranges as needed to fit specific scenarios and suspicious activity patterns
- For business accounts, adapt guidelines based on whether it's traditional or freelance/self-employed
</note>

### 6.3 Dutch Cultural Elements

1. Dutch Holidays and Events:
   - NEW_YEARS_DAY = "January 1"
   - KINGS_DAY = "April 27"
   - LIBERATION_DAY = "May 5"
   - SINTERKLAAS = "December 5"
   - CHRISTMAS = ["December 25", "December 26"]

2. Common Dutch Banks:
   - ING_BANK = "ING"
   - RABOBANK = "Rabobank"
   - ABN_AMRO = "ABN AMRO"
   - SNS_BANK = "SNS Bank"
   - REVOLUT = "Revolut Bank"
   - BUNQ = "Bunq"
   - TRIODOS_BANK = "Triodos Bank"

3. Popular Dutch Retailers:
   - ALBERT_HEIJN = "Albert Heijn"
   - JUMBO = "Jumbo"
   - HEMA = "HEMA"
   - BOL_COM = "bol.com"
   - COOLBLUE = "Coolblue"
   - MEDIA_MARKT = "Media Markt"
   - ACTION = "Action"
   - LIDL = "Lidl"
   - DIRK = "Dirk"
   - BLOKKER = "Blokker"
   - KRUIDVAT = "Kruidvat"
   - SPAR = "Spar"

4. Dutch Payment Methods:
   - IDEAL = "iDEAL"
   - PIN_TRANSACTION = "PIN transaction"
   - TIKKIE = "Tikkie"

5. Dutch Financial Practices:
   - DUTCH_VAT = 0.21  // 21% VAT rate
   - MORTGAGE_INTEREST_DEDUCTION = True  // Common tax benefit
   - HEALTH_INSURANCE_MANDATORY = True
   - PENSION_CONTRIBUTION = 0.15  // Typical pension contribution around 15% of salary

6. Geographic Elements:
   - RANDSTAD = ["Amsterdam", "Rotterdam", "The Hague", "Utrecht"]
   - BORDER_COUNTRIES = ["Germany", "Belgium"]

7. Dutch Education System:
   - DUTCH_UNIVERSITIES = ["University of Amsterdam", "Utrecht University", "Leiden University", "Delft University of Technology", "Erasmus University Rotterdam", "Vrije Universiteit Amsterdam", "Tilburg University", "Radboud University", "Maastricht University"]
   - STUDENT_FINANCE = "DUO"

8. Transportation:
   - OV_CHIPKAART = "OV-chipkaart"
   - NS_RAILWAYS = "NS"
   - GVB = "GVB"

9. Housing:
   - RENTAL_PLATFORMS = ["Funda", "Pararius", "Huurwoningen", "Kamernet"]
   - HOUSING_CORPORATIONS = ["Vestia", "Ymere", "Eigen Haard", "Woonstad Rotterdam", "De Key"]

10. Utility Providers:
    - ENERGY_PROVIDERS = ["Vattenfall", "Eneco", "Essent", "Greenchoice", "Budget Energie"]
    - WATER_COMPANIES = ["Vitens", "Evides", "PWN", "Waternet", "Brabant Water"]

<important>
When generating scenarios, weave these elements into transaction descriptions, persona backgrounds, and contextual details to create authentic Dutch financial scenarios.
</important>

## 7. Suspicious Activity

- Types: Use the specific suspiciousPattern provided in the input parameter:
  - "fast-in-fast-out": Large deposits followed by rapid withdrawals or transfers
  - "large-atm-withdrawals": Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD
  - "high-volume-suspicious-countries": Frequent transactions with entities in SUSPICIOUS_COUNTRIES

- Behaviors for each type:
  - "fast-in-fast-out":
    * Large deposits followed by rapid withdrawals or transfers
    * Minimal time between incoming and outgoing transactions
    * Include high incoming payment before cash withdrawals
  - "large-atm-withdrawals":
    * Multiple ATM withdrawals near or exceeding the ATM_WITHDRAWAL_ALERT_THRESHOLD (10,000 euros)
    * Withdrawals from different locations in short time periods
  - "high-volume-suspicious-countries":
    * Frequent transactions with entities in SUSPICIOUS_COUNTRIES
    * Varying transaction amounts to avoid consistent patterns
    * Use real, well-known international company names for these transactions

- Number of suspicious transactions/patterns based on difficultyLevel:
  * Easy: 2-3 suspicious activities
  * Medium: 3-5 suspicious activities
  * Hard: 5-8 suspicious activities or complex patterns

<important>
- Ensure adherence to ATM_WITHDRAWAL_ALERT_THRESHOLD for cash withdrawals/deposits
- Amount and frequency should deviate from normal patterns
- For large transactions, ensure proportionality to monthly income
- Distribute suspicious activities within the 6-month period
- Randomly determine frequency of suspicious activities based on difficultyLevel
- For cash withdrawals, consider travel patterns in the persona's background
- For cash deposits, treat as more suspicious than withdrawals
</important>

<note>
Additional considerations:
- Ensure that the suspicious activity aligns with the account type (retail or business)
- For business accounts, especially freelance/self-employed, adjust patterns to fit with expected business operations
- Consider the persona's background story when crafting suspicious activities
- For higher difficulty levels, combine multiple suspicious elements or create more subtle patterns
</note>

## 8. Context and Explanation

- Provide a coherent explanation for the suspicious activity
- Include relevant Dutch cultural, economic, or regulatory factors
- Align the explanation with the given decisionOutcome
- Include details relevant to the specified suspiciousPattern
- For easy difficulty, make the pattern more obvious in the explanation
- For higher difficulties, introduce more complexity and potential mitigating factors in the explanation
- Incorporate the persona's background story into the explanation

## 9. Analyst Decision

- Correct action: Use the provided decisionOutcome
- Key factors to consider: [List 1-5 non-repetitive, critical points, including aspects of the suspiciousPattern if specified]
- For easy difficulty, make the decision factors more straightforward
- For hard difficulty, ensure the factors reflect the intricacy of the situation and include potential mitigating circumstances

## 10. Difficulty Level and Scoring

- Use the provided difficultyLevel
- Assign a score: Easy (1-3), Medium (4-7), Hard (8-10)
- For hard difficulty, ensure patterns are complex and not immediately obvious

Scoring Guidelines:
- Easy (1-3):
  * Score 1: Very obvious suspicious pattern, minimal transaction complexity
  * Score 2: Clear suspicious pattern, slight increase in transaction volume
  * Score 3: Noticeable suspicious pattern, introduction of minor complexities
- Medium (4-7):
  * Score 4: Suspicious pattern requires some analysis, increased transaction volume
  * Score 5: Pattern is less obvious, requires correlation between multiple transactions
  * Score 6: Introduction of potential mitigating factors, higher complexity in transaction patterns
  * Score 7: Multiple subtle instances of suspicious pattern, requires thorough investigation
- Hard (8-10):
  * Score 8: Complex implementation of suspicious pattern, high volume of transactions
  * Score 9: Very subtle pattern implementation, potential legitimate explanations present
  * Score 10: Extremely complex scenario, multiple intertwined patterns, highest level of analysis required


Scoring Process:
1. Base Score: Start with the middle score of the difficulty level (Easy: 2, Medium: 5, Hard: 9)
2. Adjust based on:
   - Number of suspicious transactions (+1 for more, -1 for fewer)
   - Complexity of the pattern implementation (+1 for more complex, -1 for simpler)
   - Presence of mitigating factors or potential legitimate explanations (+1 if present)
   - Volume and complexity of overall transactions (+1 for higher, -1 for lower)
3. Ensure the final score remains within the range for the chosen difficulty level



Usage in Scenario Generation:
- Use the score to fine-tune the complexity of the generated scenario
- Higher scores within each difficulty level should correspond to:
  * More sophisticated implementation of the suspicious pattern
  * Increased overall transaction volume and complexity
  * More nuanced context and potential explanations
  * More challenging analyst decision factors


## 11. Auxiliary Data

Include 6-month averages for the following categories (if showAuxiliaryData is true):
- Daily expenses (groceries, dining out)
- Housing (rent/mortgage, utilities)
- Transportation
- Healthcare
- Entertainment
- Savings/Investments
- International transfers
- Cash withdrawals/deposits

Calculation Methods:
a. Daily Expenses: Sum all transactions labeled as groceries or dining out over 6 months, divide by 180
b. Housing: Sum all housing-related expenses over 6 months, divide by 6
c. Transportation: Sum all transportation-related expenses over 6 months, divide by 6
d. Healthcare: Sum all healthcare-related expenses over 6 months, divide by 6
e. Entertainment: Sum all entertainment-related expenses over 6 months, divide by 6
f. Savings/Investments: Calculate net increase in savings and investment accounts over 6 months, divide by 6
g. International Transfers: Sum absolute value of all international transfers over 6 months, divide by 6
h. Cash Withdrawals/Deposits: Sum absolute value of all cash withdrawals and deposits over 6 months, divide by 6


General Formula: Monthly Average = (Sum of all relevant transactions over 6 months) / 6

- Ensure averages are consistent with the persona's financial profile and transaction patterns
- For business accounts, adjust calculations to reflect business-specific patterns
- For categories with irregular expenses, consider using a weighted average


## 12. Quality Assurance


- Ensure all data is realistic and consistent for the Dutch context
- Verify that suspicious activities align with the given decisionOutcome and suspiciousPattern
- Confirm that the scenario difficulty matches the provided difficultyLevel
- Check that cash withdrawals/deposits respect the ATM_WITHDRAWAL_ALERT_THRESHOLD
- Verify that the suspiciousPattern is prominently featured in the transaction data
- Ensure the transaction data feels realistic, mimicking a real bank app's level of detail
- For business accounts, use real, well-known international company names where appropriate
- Verify that freelance and self-employed individuals are correctly classified as business accounts
- Check that transaction patterns for freelance/self-employed accounts reflect the irregular nature of project-based income and expenses
- Ensure the financial profile and transaction data are consistent with the specific type of business account


## 13. Output Format

Generate a JSON object containing the following structure. All fields must be present, even if some are null or empty arrays:

```json
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
    "types": ["string"],
    "timing": ["string"],
    "amounts": ["number"],
    "pattern": "string",
    "frequencies": ["number"]
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
    "dailyExpenses": "number (monthly average)",
    "housing": "number (monthly average)",
    "transportation": "number (monthly average)",
    "healthcare": "number (monthly average)",
    "entertainment": "number (monthly average)",
    "savingsInvestments": "number (monthly average)",
    "internationalTransfers": "number (monthly average)",
    "cashWithdrawalsDeposits": "number (monthly average)"
  }
}
```

<note>
Field Descriptions:
1. persona: Persona details including background story and previous flagging status
2. financialProfile: Financial profile details
3. transactionData: 6-month transaction data (always included)
4. suspiciousActivity: Suspicious activity details including specified suspiciousPattern
5. context: Detailed explanation of the scenario, including suspicious activities and their context
6. analystDecision: Analyst decision criteria (non-repetitive and appropriately complex)
7. difficultyLevel: Difficulty level and score
8. auxiliaryData: 6-month category averages (only if showAuxiliaryData is true)
</note>

## 14. Error Handling

If any input parameter is invalid, return a JSON object with the following structure:

```json
{
  "error": "Invalid input parameters",
  "invalidParameters": [
    {
      "parameter": "string (name of the invalid parameter)",
      "providedValue": "string or boolean (the invalid value provided)",
      "allowedValues": ["array of allowed values for this parameter"],
      "errorMessage": "string (specific error message for this parameter)"
    }
  ]
}
```

Specific error messages for each parameter:

   1. showAuxiliaryData:
      - Error: "showAuxiliaryData must be a boolean value (true or false)"

   2. decisionOutcome:
      - Error: "decisionOutcome must be either 'escalate' or 'close'"

   3. difficultyLevel:
      - Error: "difficultyLevel must be 'easy', 'medium', or 'hard'"

   4. accountType:
      - Error: "accountType must be either 'retail' or 'business'"

   5. suspiciousPattern:
      - Error: "suspiciousPattern must be 'fast-in-fast-out', 'large-atm-withdrawals', or 'high-volume-suspicious-countries'"

If multiple parameters are invalid, include all of them in the invalidParameters array.

Example of an error response:

```json
{
  "error": "Invalid input parameters",
  "invalidParameters": [
    {
      "parameter": "difficultyLevel",
      "providedValue": "extreme",
      "allowedValues": ["easy", "medium", "hard"],
      "errorMessage": "difficultyLevel must be 'easy', 'medium', or 'hard'"
    },
    {
      "parameter": "suspiciousPattern",
      "providedValue": "unusual-transfers",
      "allowedValues": ["fast-in-fast-out", "large-atm-withdrawals", "high-volume-suspicious-countries"],
      "errorMessage": "suspiciousPattern must be 'fast-in-fast-out', 'large-atm-withdrawals', or 'high-volume-suspicious-countries'"
    }
  ]
}
```

<important>
Ensure that the function checks all parameters and reports all errors, not just the first one encountered. This allows users to correct all issues at once.
</important>

## 14. Data Sanitization Guidelines

To protect privacy and prevent the exposure of sensitive information, follow these guidelines when generating scenario data:

1. Personal Names:
   - Use a predefined list of common Dutch first names and surnames
   - Avoid using real names of individuals, especially for suspicious activities
   - Example: Instead of "John Doe", use "Jan de Vries"

4. Account Numbers:
   - Never use real account numbers
   - Generate fictitious account numbers that follow the correct format for Dutch banks
   - Example: For IBAN, use "NL99 BANK 0123 4567 89" where BANK is a placeholder for the bank's code

5. Addresses:
   - Use real street names but fictitious house numbers
   - For suspicious activities, use generic addresses like "Hoofdstraat 123, Amsterdam"

6. Phone Numbers:
   - Generate fictitious phone numbers that follow Dutch number formats
   - For mobile: +31 6 1234 5678
   - For landline: +31 20 123 4567 (where 20 is the area code for Amsterdam)

7. Email Addresses:
   - Create fictitious email addresses using common providers
   - Example: j.devries@emailprovider.nl

8. Identification Numbers:
   - Never use real identification numbers (e.g., BSN, passport numbers)
   - Generate fictitious numbers that follow the correct format but would fail validation checks


Consistency: Ensure that once a sanitized name or identifier is used for an entity, it is used consistently throughout the scenario.
When using placeholder data, make sure it's clearly distinguishable as fictional to prevent any confusion with real entities.


## 15. Performance Considerations

When implementing the KYC/TM Test Scenario Generator, consider the following performance aspects:

1. Computational Complexity:
   - The overall complexity is O(n), where n is the number of transactions generated.
   - Expect the runtime to increase linearly with the number of transactions and the difficulty level.

2. Expected Runtime:
   - Easy scenarios: Typically < 1 second
   - Medium scenarios: Typically 1-3 seconds
   - Hard scenarios: Typically 3-7 seconds
   Note: Actual runtimes may vary based on the implementation and hardware used.

3. Memory Usage:
   - Memory usage is primarily determined by the number of transactions generated.
   - Estimate: Approximately 1KB per transaction, plus overhead for persona and context data.

4. Scaling Considerations:
   - For bulk scenario generation, consider implementing parallel processing.
   - If generating large numbers of scenarios, implement batching to manage memory usage.

5. Database Interactions:
   - If using a database to store predefined data (e.g., company names, bank lists), ensure efficient querying.
   - Consider caching frequently used data to reduce database load.

6. Random Number Generation:
   - Use a high-quality random number generator to ensure scenario variability.
   - Be aware that extensive use of randomization may impact performance.

7. Difficulty Level Impact:
   - Higher difficulty levels require more complex logic and may take longer to generate.
   - Easy: ~100-200 transactions
   - Medium: ~200-400 transactions
   - Hard: ~400-800 transactions

8. Optimization Tips:
   - Precompute and cache common elements (e.g., date ranges, recurring transaction templates).
   - Use efficient data structures (e.g., hash maps for quick lookups of predefined data).
   - Implement lazy evaluation where possible, especially for auxiliary data calculations.


Performance Monitoring: Implement logging and monitoring to track generation times and resource usage. This will help identify bottlenecks and opportunities for optimization.


<important>
Ensure all numerical data is formatted consistently (e.g., use of decimal points, thousands separators)
</important>


GenerateKYCTestScenario(
"showAuxiliaryData": "true",
"decisionOutcome: "escalate",
"difficultyLevel": "medium",
"accountType": "retail",
"suspiciousPattern": "high-volume-suspicious-countries")
"""
