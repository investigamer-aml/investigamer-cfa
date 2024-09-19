--
-- PostgreSQL database dump
--

-- Dumped from database version 15.6 (Homebrew)
-- Dumped by pg_dump version 15.6 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: data_admin
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO data_admin;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: data_admin
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO data_admin;

--
-- Name: difficulty_level; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.difficulty_level (
    id integer NOT NULL,
    level character varying(50) NOT NULL
);


ALTER TABLE public.difficulty_level OWNER TO data_admin;

--
-- Name: difficulty_level_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.difficulty_level_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.difficulty_level_id_seq OWNER TO data_admin;

--
-- Name: difficulty_level_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.difficulty_level_id_seq OWNED BY public.difficulty_level.id;


--
-- Name: learning_paths; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.learning_paths (
    id integer NOT NULL,
    user_id integer,
    name character varying(255),
    description text
);


ALTER TABLE public.learning_paths OWNER TO data_admin;

--
-- Name: learning_paths_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.learning_paths_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.learning_paths_id_seq OWNER TO data_admin;

--
-- Name: learning_paths_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.learning_paths_id_seq OWNED BY public.learning_paths.id;


--
-- Name: lessons; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.lessons (
    id integer NOT NULL,
    title text
);


ALTER TABLE public.lessons OWNER TO data_admin;

--
-- Name: lessons_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.lessons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lessons_id_seq OWNER TO data_admin;

--
-- Name: lessons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.lessons_id_seq OWNED BY public.lessons.id;


--
-- Name: news_articles; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.news_articles (
    id integer NOT NULL,
    content text NOT NULL,
    use_case_id integer NOT NULL
);


ALTER TABLE public.news_articles OWNER TO data_admin;

--
-- Name: news_articles_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.news_articles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.news_articles_id_seq OWNER TO data_admin;

--
-- Name: news_articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.news_articles_id_seq OWNED BY public.news_articles.id;


--
-- Name: options; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.options (
    id integer NOT NULL,
    question_id integer,
    text text,
    is_correct boolean
);


ALTER TABLE public.options OWNER TO data_admin;

--
-- Name: options_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.options_id_seq OWNER TO data_admin;

--
-- Name: options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.options_id_seq OWNED BY public.options.id;


--
-- Name: questions; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.questions (
    id integer NOT NULL,
    use_case_id integer,
    text text
);


ALTER TABLE public.questions OWNER TO data_admin;

--
-- Name: questions_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.questions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_id_seq OWNER TO data_admin;

--
-- Name: questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.questions_id_seq OWNED BY public.questions.id;


--
-- Name: risk_factor_matrix; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.risk_factor_matrix (
    id integer NOT NULL,
    factor character varying,
    score integer,
    use_case_id integer
);


ALTER TABLE public.risk_factor_matrix OWNER TO data_admin;

--
-- Name: risk_factor_matrix_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.risk_factor_matrix_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.risk_factor_matrix_id_seq OWNER TO data_admin;

--
-- Name: risk_factor_matrix_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.risk_factor_matrix_id_seq OWNED BY public.risk_factor_matrix.id;


--
-- Name: use_cases; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.use_cases (
    id integer NOT NULL,
    description text,
    type character varying(255),
    lesson_id integer,
    created_by_user integer,
    risk_factors jsonb,
    difficulty_id integer
);


ALTER TABLE public.use_cases OWNER TO data_admin;

--
-- Name: use_cases_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.use_cases_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.use_cases_id_seq OWNER TO data_admin;

--
-- Name: use_cases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.use_cases_id_seq OWNED BY public.use_cases.id;


--
-- Name: user_answers; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.user_answers (
    id integer NOT NULL,
    user_id integer,
    use_case_id integer,
    question_id integer,
    option_id integer,
    is_correct boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    lesson_id integer
);


ALTER TABLE public.user_answers OWNER TO data_admin;

--
-- Name: user_answers_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.user_answers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_answers_id_seq OWNER TO data_admin;

--
-- Name: user_answers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.user_answers_id_seq OWNED BY public.user_answers.id;


--
-- Name: user_lesson_interactions; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.user_lesson_interactions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    lesson_id integer NOT NULL,
    completed boolean NOT NULL,
    completion_date timestamp without time zone,
    score double precision,
    last_accessed timestamp without time zone
);


ALTER TABLE public.user_lesson_interactions OWNER TO data_admin;

--
-- Name: user_lesson_interactions_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.user_lesson_interactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_lesson_interactions_id_seq OWNER TO data_admin;

--
-- Name: user_lesson_interactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.user_lesson_interactions_id_seq OWNED BY public.user_lesson_interactions.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(255),
    hashed_password character varying(255),
    use_case_difficulty character varying,
    score double precision,
    is_admin boolean DEFAULT false NOT NULL,
    lesson_id integer,
    first_name text,
    last_name text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO data_admin;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO data_admin;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: difficulty_level id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.difficulty_level ALTER COLUMN id SET DEFAULT nextval('public.difficulty_level_id_seq'::regclass);


--
-- Name: learning_paths id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.learning_paths ALTER COLUMN id SET DEFAULT nextval('public.learning_paths_id_seq'::regclass);


--
-- Name: lessons id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.lessons ALTER COLUMN id SET DEFAULT nextval('public.lessons_id_seq'::regclass);


--
-- Name: news_articles id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.news_articles ALTER COLUMN id SET DEFAULT nextval('public.news_articles_id_seq'::regclass);


--
-- Name: options id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.options ALTER COLUMN id SET DEFAULT nextval('public.options_id_seq'::regclass);


--
-- Name: questions id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.questions ALTER COLUMN id SET DEFAULT nextval('public.questions_id_seq'::regclass);


--
-- Name: risk_factor_matrix id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.risk_factor_matrix ALTER COLUMN id SET DEFAULT nextval('public.risk_factor_matrix_id_seq'::regclass);


--
-- Name: use_cases id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.use_cases ALTER COLUMN id SET DEFAULT nextval('public.use_cases_id_seq'::regclass);


--
-- Name: user_answers id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers ALTER COLUMN id SET DEFAULT nextval('public.user_answers_id_seq'::regclass);


--
-- Name: user_lesson_interactions id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_lesson_interactions ALTER COLUMN id SET DEFAULT nextval('public.user_lesson_interactions_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: difficulty_level; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.difficulty_level (id, level) FROM stdin;
1	Easy
2	Medium
3	Hard
4	Advanced
\.


--
-- Data for Name: learning_paths; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.learning_paths (id, user_id, name, description) FROM stdin;
\.


--
-- Data for Name: lessons; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.lessons (id, title) FROM stdin;
1	Learning the basics
2	Professional Development
3	Mastering it all
\.


--
-- Data for Name: news_articles; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.news_articles (id, content, use_case_id) FROM stdin;
1	# Headline: Wholesale Client in Hong Kong Under Scrutiny for Unusual Transaction Patterns and Regulatory Concerns\n\n## Introduction:\nIn a recent development, a wholesale client based in Hong Kong, operating within the electronics manufacturing industry, has come under scrutiny for its unusual transaction patterns and potential regulatory non-compliance. The client's significant incoming and outgoing transactions have raised red flags, prompting concerns from financial authorities.\n\n## Body:\nThe wholesale client has been receiving large payments from international suppliers in countries known for their electronics manufacturing capabilities, such as China and Taiwan. These transactions, both in size and frequency, deviate from the client's typical behavior, triggering suspicion. On the outgoing side, wire transfers to electronics component suppliers and contract manufacturers have been initiated, with one counterparty raising regulatory concerns due to potential non-compliance with export control regulations.\n\nIn response to the flagged transactions, customer outreach has been conducted to seek clarification from the client. However, the responses provided by the client have been evasive and lacking in transparency, failing to alleviate concerns regarding the nature and purpose of the transactions. The risks associated with the client's behavior include customer risk, transaction risk, and counterparty risk, highlighting the need for a thorough risk assessment and compliance measures.\n\n## Conclusion:\nThe implications of the wholesale client's unusual transaction patterns and regulatory concerns could have far-reaching consequences, not only for the client but also for the financial institutions involved. It is crucial for all parties to prioritize diligent compliance and risk assessment to mitigate potential risks and uphold regulatory standards. This case serves as a reminder of the importance of vigilance in the financial sector and the necessity of proactive measures to address suspicious activities promptly.	2
2	# Headline: Wholesale Client in Automotive Manufacturing Sector Under Scrutiny for Suspicious Transactions\n\n## Introduction:\nIn a recent development, a wholesale client operating in the automotive manufacturing sector has come under scrutiny for a series of suspicious transactions involving large payments from international suppliers. The transactions, originating from Algeria, have raised red flags due to the counterparties' lack of connection to the automotive industry.\n\n## Body:\nUpon further investigation, it was discovered that the wholesale client has been initiating multiple wire transfers to suppliers and subcontractors, with one counterparty flagged for potential involvement in financial misconduct. Despite customer outreach efforts to clarify the nature of these transactions, vague responses have failed to provide satisfactory explanations.\n\nThe risk factor analysis highlights concerns in various areas, including the customer's KYC profile, adverse media associated with counterparties, and the geographical risk posed by transactions from Algeria. This raises regulatory compliance issues and underscores the importance of thorough transaction analysis to mitigate risks.\n\n## Conclusion:\nThe implications of these suspicious transactions could have far-reaching consequences for the wholesale client in the automotive manufacturing sector. It is crucial for financial institutions and businesses to prioritize diligent compliance measures to prevent potential financial crimes and safeguard their reputation. This case serves as a reminder of the importance of robust risk assessment and compliance practices in the financial sector.	3
3	# Headline: Dubai Wholesale Client Under Scrutiny for Suspicious Transaction Patterns in Construction Materials Trading\n\n## Introduction:\nA wholesale client based in Dubai, United Arab Emirates, operating in the construction materials trading industry, has come under the spotlight for its unusual transaction activities. Large payments from international suppliers and wire transfers to manufacturers have raised red flags, prompting concerns about compliance and regulatory adherence.\n\n## Body:\nThe incoming transactions from countries like China and India, known for their construction material production, have raised eyebrows due to their size and frequency. On the outgoing side, wire transfers to suppliers have drawn attention, especially one involving a commodity newly regulated under export control laws.\n\nIn response to these flagged transactions, customer outreach has been initiated to seek clarification. However, the customer's responses have been vague and lacking in satisfactory explanations for the observed transaction patterns. This ambiguity has only heightened concerns about potential risks associated with the client's activities.\n\n## Conclusion:\nThe risk factors identified, including industry and transaction risks, underscore the importance of thorough KYC profiling and transaction analysis in the financial sector. Compliance with regulations and diligent monitoring of transaction activities are crucial to prevent illicit financial activities and maintain the integrity of the financial system. The implications of non-compliance could be severe, emphasizing the need for vigilance and adherence to regulatory standards in the industry.	10
4	# Headline: Istanbul-Based Wholesale Client Faces Scrutiny Over International Transactions in Construction Materials Trading\n\n# Introduction:\nIn a recent development, a wholesale client based in Istanbul, Turkey, operating in the construction materials trading industry, has come under the spotlight for its significant international transactions. The transactions, involving payments from suppliers in countries like China and Russia, have raised concerns regarding compliance and risk assessment.\n\n# Body:\nThe wholesale client, specializing in the import and distribution of building materials such as cement and steel, has been actively engaged in procurement activities to meet the demand in the local construction market. However, the nature and frequency of the incoming and outgoing transactions have triggered regulatory scrutiny.\n\nOn the incoming side, payments from international suppliers have raised eyebrows due to their size and frequency, prompting a closer look at the client's sourcing practices. Similarly, the outgoing wire transfers to construction companies and contractors have drawn attention, with transaction descriptions indicating purchases of building materials for various construction projects in the region.\n\nIn response to the flagged transactions, the client has cooperated with regulatory authorities, providing detailed explanations, purchase contracts, and project agreements to demonstrate the legitimacy of the transactions. Moreover, the client's compliance records reflect a history of adherence to anti-money laundering regulations, reassuring authorities of their commitment to transparency.\n\n# Conclusion:\nAs the wholesale client navigates through the scrutiny of its international transactions, the importance of diligent compliance and risk assessment in the financial sector is underscored. Any lapses in regulatory compliance could have severe consequences, not only for the client but also for the broader financial ecosystem. It is imperative for financial institutions and businesses to prioritize compliance measures to maintain trust and integrity in the industry.	12
5	# Headline: Wholesale Client in Lagos Under Scrutiny for Potential Fraudulent Activities in Oil and Gas Sector\n\n## Introduction:\nA wholesale client based in Lagos, Nigeria, operating in the oil and gas exploration industry, is facing scrutiny due to suspicious transaction patterns and adverse media reports. Allegations of fraudulent activities, including bribery and corruption, have raised red flags within the financial sector.\n\n## Body:\nThe wholesale client has been receiving large payments from international sources, while also making significant wire transfers to suppliers and subcontractors in the oil and gas sector. However, adverse media has linked the client to regulatory violations and financial misconduct, casting doubt on the legitimacy of their operations.\n\nCustomer outreach efforts to clarify the nature of these transactions have been met with evasive responses lacking transparency. This lack of cooperation only adds to the concerns surrounding the client's activities and raises questions about their compliance with regulatory standards.\n\n## Conclusion:\nThe potential implications of these findings are significant, as they point to possible involvement in illicit activities within the oil and gas industry. It is crucial for financial institutions and regulatory bodies to conduct thorough risk assessments and due diligence to prevent money laundering and fraud. Compliance with anti-money laundering regulations is essential to maintain the integrity of the financial system and protect against financial crime.\n\nIn conclusion, this case serves as a reminder of the importance of vigilance and diligence in risk assessment and compliance practices within the financial sector. By staying alert to red flags and conducting thorough investigations, institutions can help safeguard against illicit activities and maintain trust in the industry.	9
6	# Headline: Compliance Due Diligence Analysis Reveals Complex Ownership Structure and Ethical Concerns at XYZ Global\n\n## Introduction:\nIn a recent Compliance Due Diligence (CDD) analysis report, XYZ Global, a Corporate Banking client, has come under scrutiny for its intricate ownership structure and ethical concerns surrounding its Ultimate Beneficial Owner (UBO), Sarah Chen. Despite efforts to maintain a clean compliance record, the company's operations in various sectors across continents raise regulatory eyebrows.\n\n## Body:\nUpon delving into XYZ Global's client profile, CDD analysts uncovered a web of subsidiaries and special purpose vehicles (SPVs) domiciled in jurisdictions known for their lack of transparency and weak enforcement of anti-money laundering (AML) regulations. The UBO, Sarah Chen, hails from a medium-risk jurisdiction for financial crime and sanctions evasion, with past associations to businesses facing ethical lapses and minor compliance issues. While no significant legal actions have been taken against her, the shadow of scrutiny looms over XYZ Global's ownership structure.\n\nDespite these red flags, XYZ Global's financial transaction analysis paints a picture of consistent and transparent dealings with reputable business partners in technology development, green energy projects, and international trade. The company has implemented comprehensive compliance policies, including enhanced due diligence (EDD) processes, and undergoes regular audits by reputable firms. However, the complexity of their ownership structure and the ethical concerns surrounding the UBO raise regulatory concerns that cannot be ignored.\n\n## Conclusion:\nAs the financial industry continues to navigate the complexities of compliance and risk assessment, the case of XYZ Global serves as a stark reminder of the importance of diligent due diligence and regulatory oversight. While the company's financial transactions show no immediate red flags, the intricate ownership structure and ethical concerns surrounding the UBO highlight the need for enhanced scrutiny and vigilance in compliance practices. Failure to address these issues could have far-reaching consequences for XYZ Global and the broader financial ecosystem. Vigilance and adherence to compliance standards are paramount in safeguarding against potential risks and ensuring a sound financial environment.	1
7	# Headline: Miami-Based Wholesale Client in Agricultural Industry Demonstrates Compliance Amidst International Transactions\n\n## Introduction:\nIn the bustling financial hub of Miami, a wholesale client in the import and distribution industry has caught the attention of regulatory authorities due to its significant international transactions. With payments flowing in from agricultural suppliers in countries like Brazil and Argentina, and outgoing wire transfers to agricultural producers, the client's financial activities have raised eyebrows. However, a closer look reveals a story of compliance and cooperation that sets this client apart.\n\n## Body:\nThe incoming transactions from renowned agricultural producers in South America, coupled with the outgoing payments for grains and fruits, paint a picture of a thriving business in the agricultural sector. While some transactions may appear larger than usual, the client's prompt responses to inquiries and provision of detailed documentation have reassured regulators of the legitimacy of these activities. Moreover, the client's track record of compliance with anti-money laundering regulations and cooperation with authorities further solidify their standing in the industry.\n\n## Conclusion:\nThis use case serves as a prime example of how proactive compliance measures can mitigate risks in the financial sector. By maintaining clear documentation, timely responses, and a history of cooperation, the Miami-based wholesale client has demonstrated a commitment to transparency and regulatory adherence. As financial institutions navigate the complex landscape of international transactions, this case underscores the importance of ongoing monitoring and due diligence to safeguard against financial crime risks. Compliance remains a cornerstone of trust and integrity in the financial world, and this client's actions serve as a beacon of best practices for others to follow.	11
8	# Headline: Financial Institution Faces Compliance Challenges Due to High Risk Factors\n\n# Introduction:\nIn a recent development, a prominent financial institution has come under scrutiny for its risk factor analysis, particularly in the areas of KYC profiles, adverse media, customer outreach, and transaction analysis. These risk factors have raised concerns about the institution's compliance with regulatory requirements and its ability to mitigate potential risks effectively.\n\n# Body:\nThe institution's KYC profile assessment has revealed significant customer, industry, and geographical risks, indicating potential vulnerabilities in its client base. Additionally, adverse media coverage has highlighted counterparty risks that could impact the institution's reputation and financial stability. Customer outreach efforts have also identified risks associated with certain clients, raising questions about the institution's due diligence processes.\n\nTransaction analysis has further revealed potential risks in the institution's financial transactions, pointing to the need for enhanced monitoring and oversight. Regulatory concerns have been raised regarding the institution's compliance with anti-money laundering and counter-terrorism financing regulations, underscoring the importance of robust risk management practices.\n\nThese risk factors not only pose a threat to the institution's financial health but also raise broader concerns about the integrity of the financial system. Failure to address these risks could result in regulatory penalties, reputational damage, and financial losses for the institution and its stakeholders.\n\n# Conclusion:\nAs the financial institution navigates these compliance challenges, it is crucial for all stakeholders to prioritize diligent risk assessment and compliance measures. Proactive risk management strategies, enhanced due diligence processes, and regular monitoring of high-risk activities are essential to safeguarding the institution's reputation and ensuring regulatory compliance. By addressing these risk factors effectively, the institution can strengthen its resilience and uphold the trust of its clients and regulators in the ever-evolving financial landscape.	99
\.


--
-- Data for Name: options; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.options (id, question_id, text, is_correct) FROM stdin;
1	1	Geography Risk	f
2	1	Industry Risk	f
3	1	UBO Risk	t
4	1	Compliance Risk	f
5	2	Corrupt country	f
6	2	Awful jurisdiction	f
7	2	Beautiful ladies	t
8	2	Big balls on the politicians	f
20	7	Various components need to be analysed	f
21	7	Yes, it is and needs to be handled with care	t
22	7	Further info is needed	f
23	7	No, this user is safe to continue with the process	f
24	8	Various components need to be analysed	t
25	8	Yes, it is and needs to be handled with care	f
26	8	Further info is needed	f
27	8	No, this user is safe to continue with the process	f
10	5	Ambiguous	f
11	5	Not realistic	f
12	5	Dubious origin of money	f
13	5	Need to check the transaction history to provide more info	t
14	6	Need to escalate with senior managers	f
15	6	Yes, the risk is to high	f
16	6	Definite money laundering risk potential	f
17	6	Geogrpahical risk is the biggest factor	t
18	3	Not easy to discern	f
19	3	More info needed	t
28	3	Country of origin is enough to flag this	f
29	3	Might be wise to ask for more info from the client.	f
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.questions (id, use_case_id, text) FROM stdin;
1	1	What is the biggest KYC risk?
2	2	What is the geography Risk in this use case?
5	9	What is industry risk in this use case?
3	3	Can you identify the anomaly here?
6	10	What is wrong with this client?
7	11	Is the origin of money an issue here?
8	12	Is geogrpahy or industry risk bigger here??
\.


--
-- Data for Name: risk_factor_matrix; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.risk_factor_matrix (id, factor, score, use_case_id) FROM stdin;
\.


--
-- Data for Name: use_cases; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.use_cases (id, description, type, lesson_id, created_by_user, risk_factors, difficulty_id) FROM stdin;
2	# Customer Overview\n\nThe customer involved is a **wholesale client headquartered in Hong Kong**, a jurisdiction known for its robust financial infrastructure and strategic location as a global financial hub. The customer operates within the **electronics manufacturing industry**.\n\n## Incoming Transactions\n\n- Several incoming transactions have been identified, consisting of large payments from international suppliers located in countries known for their electronics manufacturing capabilities, such as China and Taiwan.\n- These transactions are significant in size and frequency, deviating from the customer's typical transaction behavior.\n\n## Outgoing Transactions\n\n- On the outgoing side, multiple wire transfers have been initiated by the customer, primarily to electronics component suppliers and contract manufacturers.\n- However, recent regulatory changes have raised concerns about one of the counterparties, indicating potential involvement in non-compliance with export control regulations.\n\n## Response and Actions\n\n- In response to the flagged transactions, customer outreach has been conducted to seek clarification from the customer regarding the nature and purpose of the transactions.\n- However, the customer's responses are evasive and lack transparency, failing to provide satisfactory explanations for the unusual transaction patterns observed.\n	TM	1	6	{"Customer outreach": {"Customer risk": true}, "Transaction analysis": {"Transaction risk": true, "Counterparty risk": true}}	1
3	# Customer Overview\n\nThe customer involved is a **wholesale client operating in the automotive manufacturing sector**, specializing in the production of components for commercial vehicles.\n\n## Incoming Transactions\n\n- Several incoming transactions have been identified, consisting of large payments from international suppliers located in Algeria.\n- These transactions are coming from counterparties not active in or related to the automotive manufacturing sector.\n\n## Outgoing Transactions\n\n- On the outgoing side, multiple wire transfers have been initiated by the customer, primarily to suppliers and subcontractors involved in the production process.\n- However, adverse media has been identified on one of the counterparties, indicating potential involvement in previous financial misconduct or criminal activities.\n\n## Response and Actions\n\n- In response to the flagged transactions, customer outreach has been conducted to seek clarification from the customer regarding the nature and purpose of the transactions.\n- However, the customer's responses are vague and fail to provide satisfactory explanations for the unusual transaction patterns observed.\n	TM	1	6	{"KYC profile": {"Customer risk": true}, "Adverse media": {"Counterparty risk": true}, "Customer outreach": {"Customer risk": true}, "Transaction analysis": {"Transaction risk": true, "Counterparty risk": true, "Geographical risk": true}}	1
10	# Customer Overview\n\nThe customer involved is a **wholesale client headquartered in Dubai, United Arab Emirates**, a jurisdiction known for its strategic location as a global business hub. The customer operates within the **construction materials trading industry**.\n\n## Incoming Transactions\n\n- Several incoming transactions have been identified, consisting of large payments from international suppliers located in countries known for their production of construction materials, such as China and India.\n- These transactions are significant in size and frequency, and stand out compared to other transactions.\n\n## Outgoing Transactions\n\n- On the outgoing side, multiple wire transfers have been initiated by the customer, primarily to construction materials manufacturers and suppliers.\n- One of the transaction descriptions states the involvement of a commodity that is recently added to new export control regulations.\n\n## Response and Actions\n\n- In response to the flagged transactions, customer outreach has been conducted to seek clarification from the customer regarding the nature and purpose of the transactions.\n- However, the customer's responses are ambiguous and fail to provide satisfactory explanations for the transaction patterns observed.\n	TM	1	6	{"KYC profile": {"Industry risk": true}, "Transaction analysis": {"Transaction risk": true}}	2
13	"Multiple large transactions with entities in countries known for financial risks, such as the UAE and Singapore. The varying transaction amounts seem designed to avoid detection."	TM	3	1	{"context": "Lieke's transaction history shows a pattern of frequent, high-value transactions with companies in countries that are considered high-risk from a financial crime perspective, specifically the UAE and Singapore. While her work as a marketing manager could potentially explain some international transactions, the amounts involved are disproportionately large compared to her income. The inconsistent transaction amounts and timing also raise red flags, as they could indicate an attempt to avoid triggering automated alert thresholds. Given the Dutch regulatory focus on preventing money laundering and terrorist financing, these transactions warrant further investigation to ensure their legitimacy.", "persona": {"age": 42, "name": "Lieke van der Velden", "background": "Lieke is a marketing manager at a mid-sized Dutch company. She frequently travels for work, visiting clients and attending conferences across Europe. Lieke is married with two children and enjoys spending her free time with family and friends. She has a busy lifestyle, juggling work and family responsibilities.", "occupation": "Marketing Manager", "familyStatus": "Married", "previouslyFlagged": false}, "auxiliaryData": {"housing": 1650, "healthcare": 180, "dailyExpenses": 1420, "entertainment": 650, "transportation": 320, "savingsInvestments": 1200, "internationalTransfers": 9350, "cashWithdrawalsDeposits": 720}, "analystDecision": {"action": "escalate", "keyFactors": ["Repeated transactions with high-risk countries", "Transaction amounts disproportionate to monthly income", "Suspicious pattern of inconsistent amounts to avoid detection", "Lack of clear business justification for large international transfers"]}, "difficultyLevel": {"level": "medium", "score": 6}, "transactionData": [{"date": "2023-01-02", "type": "outgoing", "amount": -132.5, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Albert Heijn Groceries"}, {"date": "2023-01-05", "type": "incoming", "amount": 4850, "country": "Netherlands", "merchant": "Employer", "description": "Salary"}, {"date": "2023-01-06", "type": "outgoing", "amount": -500, "country": "Netherlands", "merchant": "Rabobank", "description": "Transfer to Savings"}, {"date": "2023-01-10", "type": "outgoing", "amount": -68.2, "country": "Netherlands", "merchant": "Jumbo", "description": "Jumbo Groceries"}, {"date": "2023-01-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "GVB Property Management", "description": "Rent"}, {"date": "2023-01-18", "type": "outgoing", "amount": -180, "country": "Netherlands", "merchant": "Efteling", "description": "Efteling Tickets"}, {"date": "2023-01-22", "type": "outgoing", "amount": -32.85, "country": "Netherlands", "merchant": "Happy Wok", "description": "Takeout Dinner"}, {"date": "2023-02-01", "type": "outgoing", "amount": -67.5, "country": "Netherlands", "merchant": "Vodafone", "description": "Vodafone Bill"}, {"date": "2023-02-05", "type": "incoming", "amount": 4850, "country": "Netherlands", "merchant": "Employer", "description": "Salary"}, {"date": "2023-02-09", "type": "incoming", "amount": 2200, "country": "Germany", "merchant": "Müller GmbH", "description": "Payment from Client"}, {"date": "2023-02-12", "type": "outgoing", "amount": -120.33, "country": "Netherlands", "merchant": "Lidl", "description": "Lidl Groceries"}, {"date": "2023-02-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "GVB Property Management", "description": "Rent"}, {"date": "2023-02-18", "type": "outgoing", "amount": -280.6, "country": "Netherlands", "merchant": "Bijenkorf", "description": "Bijenkorf Shopping"}, {"date": "2023-02-25", "type": "outgoing", "amount": -500, "country": "Netherlands", "merchant": "Rabobank", "description": "Transfer to Savings"}, {"date": "2023-03-02", "type": "outgoing", "amount": -59.99, "country": "Netherlands", "merchant": "Hema", "description": "Hema Household Items"}, {"date": "2023-03-05", "type": "incoming", "amount": 4850, "country": "Netherlands", "merchant": "Employer", "description": "Salary"}, {"date": "2023-03-11", "type": "outgoing", "amount": -820.43, "country": "Netherlands", "merchant": "KLM", "description": "KLM Flights"}, {"date": "2023-03-14", "type": "outgoing", "amount": -12750, "country": "Singapore", "merchant": "Zenith Holdings", "description": "Payment to Zenith Holdings"}, {"date": "2023-03-17", "type": "outgoing", "amount": -485, "country": "France", "merchant": "Le Meridien Paris", "description": "Hotel Stay"}, {"date": "2023-03-26", "type": "outgoing", "amount": -300, "country": "Netherlands", "merchant": "Rabobank", "description": "Transfer to Savings"}, {"date": "2023-04-01", "type": "outgoing", "amount": -62.5, "country": "Netherlands", "merchant": "Ziggo", "description": "Ziggo Internet & TV"}, {"date": "2023-04-05", "type": "incoming", "amount": 4850, "country": "Netherlands", "merchant": "Employer", "description": "Salary"}, {"date": "2023-04-08", "type": "outgoing", "amount": -138.67, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Albert Heijn Groceries"}, {"date": "2023-04-12", "type": "incoming", "amount": 4400, "country": "Belgium", "merchant": "Janssen BVBA", "description": "Payment from Client"}, {"date": "2023-04-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "GVB Property Management", "description": "Rent"}, {"date": "2023-04-20", "type": "outgoing", "amount": -189.9, "country": "Netherlands", "merchant": "Bijenkorf", "description": "Bijenkorf Online Order"}, {"date": "2023-04-23", "type": "outgoing", "amount": -18.5, "country": "Netherlands", "merchant": "Domino's Pizza", "description": "Takeaway Pizza"}, {"date": "2023-05-02", "type": "outgoing", "amount": -78, "country": "Netherlands", "merchant": "Nederlandse Spoorwegen", "description": "NS Train Tickets"}, {"date": "2023-05-05", "type": "incoming", "amount": 4850, "country": "Netherlands", "merchant": "Employer", "description": "Salary"}, {"date": "2023-05-08", "type": "outgoing", "amount": -92.34, "country": "Netherlands", "merchant": "Jumbo", "description": "Jumbo Groceries"}, {"date": "2023-05-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "GVB Property Management", "description": "Rent"}, {"date": "2023-05-18", "type": "outgoing", "amount": -8200, "country": "United Arab Emirates", "merchant": "Khalifa Enterprises", "description": "Payment to Khalifa Enterprises"}, {"date": "2023-05-22", "type": "outgoing", "amount": -500, "country": "United Kingdom", "merchant": "Transferwise", "description": "Transferwise Money Transfer"}, {"date": "2023-06-01", "type": "outgoing", "amount": -120, "country": "Netherlands", "merchant": "Tandartspraktijk De Wit", "description": "Dental Checkup"}, {"date": "2023-06-05", "type": "incoming", "amount": 4850, "country": "Netherlands", "merchant": "Employer", "description": "Salary"}, {"date": "2023-06-11", "type": "outgoing", "amount": -47.85, "country": "Netherlands", "merchant": "Hema", "description": "Hema Online Order"}, {"date": "2023-06-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "GVB Property Management", "description": "Rent"}, {"date": "2023-06-20", "type": "outgoing", "amount": -85, "country": "Netherlands", "merchant": "Shell", "description": "Shell Petrol"}, {"date": "2023-06-24", "type": "outgoing", "amount": -200, "country": "Netherlands", "merchant": "DeGiro", "description": "Transfer to Investment Account"}, {"date": "2023-06-27", "type": "incoming", "amount": 27500, "country": "Singapore", "merchant": "OCBC Bank", "description": "Transfer from OCBC Bank"}], "financialProfile": {"monthlyIncome": 6500, "savingsBalance": 28000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 75000}}, "suspiciousActivity": {"types": ["Frequent transactions with entities in high-risk countries", "Large international transfers", "Varying transaction amounts to avoid detection"], "timing": ["May 2023", "March 2023", "June 2023"], "amounts": [8200, 12750, 27500], "pattern": "Multiple large transactions with entities in countries known for financial risks, such as the UAE and Singapore. The varying transaction amounts seem designed to avoid detection.", "frequencies": [2, 3, 1]}}	2
14	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome: "escalate", "difficultyLevel": "medium", "accountType": "retail", "suspiciousPattern": "high-volume-suspicious-countries")	TM	3	16	{"context": "Sophie van der Berg, a marketing manager with a history of international travel, has shown an unusual pattern of high-value transactions with entities in countries flagged as high-risk for financial operations over the past six months. While her background suggests some international activity, the frequency and volume of these transactions are outside her normal patterns. The transactions involve countries like the United Arab Emirates, Malaysia, Nigeria, Russia, and Brazil, all within a short period. The amounts vary but are consistently high, ranging from €15,000 to €25,000. While her job and stated interest in emerging markets could potentially explain some of this activity, the sudden increase in volume and the choice of countries raise red flags. These suspicious transactions are interspersed with normal day-to-day expenses and regular salary deposits, making the pattern more subtle.", "persona": {"age": 42, "name": "Sophie van der Berg", "background": "Sophie is a seasoned marketing professional working for a multinational company. She frequently travels for work and personal leisure. Recently, she's been exploring investment opportunities in emerging markets, citing her company's expansion plans as inspiration.", "occupation": "Marketing Manager", "familyStatus": "Married", "previouslyFlagged": false}, "auxiliaryData": {"housing": 2000, "healthcare": 200, "dailyExpenses": 1200, "entertainment": 600, "transportation": 400, "savingsInvestments": 1000, "internationalTransfers": 16667, "cashWithdrawalsDeposits": 500}, "analystDecision": {"action": "escalate", "keyFactors": ["High volume of transactions with high-risk countries", "Sudden change in transaction patterns over the past six months", "Amounts significantly higher than usual salary and spending patterns", "Multiple transactions just below typical reporting thresholds", "Lack of clear business purpose for personal account activity in these countries"]}, "difficultyLevel": {"level": "medium", "score": 6}, "transactionData": [{"date": "2023-01-05", "type": "incoming", "amount": 5800, "country": "Netherlands", "merchant": "MultiTech Solutions BV", "description": "Salary deposit"}, {"date": "2023-01-10", "type": "outgoing", "amount": -120.5, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Albert Heijn groceries"}, {"date": "2023-01-15", "type": "outgoing", "amount": -15000, "country": "United Arab Emirates", "merchant": "Global Investments LLC", "description": "International wire transfer"}, {"date": "2023-01-20", "type": "outgoing", "amount": -52.8, "country": "Netherlands", "merchant": "NS", "description": "NS Railway ticket"}, {"date": "2023-01-25", "type": "outgoing", "amount": -85.3, "country": "Netherlands", "merchant": "Restaurant De Pijp", "description": "Restaurant De Pijp"}, {"date": "2023-02-03", "type": "incoming", "amount": 22000, "country": "Malaysia", "merchant": "AsiaGrowth Partners", "description": "Incoming transfer"}, {"date": "2023-02-05", "type": "incoming", "amount": 5800, "country": "Netherlands", "merchant": "MultiTech Solutions BV", "description": "Salary deposit"}, {"date": "2023-02-12", "type": "outgoing", "amount": -95.2, "country": "Netherlands", "merchant": "Jumbo", "description": "Jumbo groceries"}, {"date": "2023-02-18", "type": "outgoing", "amount": -65, "country": "Netherlands", "merchant": "Vodafone", "description": "Vodafone bill"}, {"date": "2023-02-25", "type": "outgoing", "amount": -129.99, "country": "Netherlands", "merchant": "Bol.com", "description": "Bol.com purchase"}, {"date": "2023-03-05", "type": "incoming", "amount": 5800, "country": "Netherlands", "merchant": "MultiTech Solutions BV", "description": "Salary deposit"}, {"date": "2023-03-10", "type": "outgoing", "amount": -18000, "country": "Nigeria", "merchant": "AfriTech Ventures", "description": "International wire transfer"}, {"date": "2023-03-15", "type": "outgoing", "amount": -110.75, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Albert Heijn groceries"}, {"date": "2023-03-20", "type": "outgoing", "amount": -499, "country": "Netherlands", "merchant": "Coolblue", "description": "Coolblue electronics"}, {"date": "2023-03-28", "type": "outgoing", "amount": -92.5, "country": "Netherlands", "merchant": "Mama Makan", "description": "Restaurant Mama Makan"}, {"date": "2023-04-05", "type": "incoming", "amount": 5800, "country": "Netherlands", "merchant": "MultiTech Solutions BV", "description": "Salary deposit"}, {"date": "2023-04-12", "type": "outgoing", "amount": -105.3, "country": "Netherlands", "merchant": "Jumbo", "description": "Jumbo groceries"}, {"date": "2023-04-18", "type": "outgoing", "amount": -65, "country": "Netherlands", "merchant": "Vodafone", "description": "Vodafone bill"}, {"date": "2023-04-22", "type": "incoming", "amount": 25000, "country": "Russia", "merchant": "EastEuro Investments", "description": "Incoming transfer"}, {"date": "2023-04-28", "type": "outgoing", "amount": -75.5, "country": "Netherlands", "merchant": "HEMA", "description": "HEMA purchase"}, {"date": "2023-05-05", "type": "incoming", "amount": 5800, "country": "Netherlands", "merchant": "MultiTech Solutions BV", "description": "Salary deposit"}, {"date": "2023-05-10", "type": "outgoing", "amount": -118.25, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Albert Heijn groceries"}, {"date": "2023-05-15", "type": "outgoing", "amount": -48.6, "country": "Netherlands", "merchant": "NS", "description": "NS Railway ticket"}, {"date": "2023-05-22", "type": "outgoing", "amount": -135, "country": "Netherlands", "merchant": "De Kas", "description": "Restaurant De Kas"}, {"date": "2023-05-30", "type": "outgoing", "amount": -20000, "country": "Brazil", "merchant": "SouthAm Growth Fund", "description": "International wire transfer"}, {"date": "2023-06-05", "type": "incoming", "amount": 5800, "country": "Netherlands", "merchant": "MultiTech Solutions BV", "description": "Salary deposit"}, {"date": "2023-06-12", "type": "outgoing", "amount": -112.8, "country": "Netherlands", "merchant": "Jumbo", "description": "Jumbo groceries"}, {"date": "2023-06-18", "type": "outgoing", "amount": -65, "country": "Netherlands", "merchant": "Vodafone", "description": "Vodafone bill"}, {"date": "2023-06-25", "type": "outgoing", "amount": -299.99, "country": "Netherlands", "merchant": "Media Markt", "description": "Media Markt electronics"}], "financialProfile": {"monthlyIncome": 5800, "savingsBalance": 68000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 120000}}, "suspiciousActivity": {"types": ["high-volume-suspicious-countries"], "timing": ["January 2023", "February 2023", "March 2023", "April 2023", "May 2023"], "amounts": [15000, 22000, 18000, 25000, 20000], "pattern": "high-volume-suspicious-countries", "frequencies": [5]}}	2
12	# Customer Overview\n\nThe customer involved is a **wholesale client headquartered in Istanbul, Turkey**, a jurisdiction known for its vibrant economy and unique geopolitical position. The customer operates within the **construction materials trading industry**, specializing in the import and distribution of building materials such as cement and steel.\n\n## Incoming Transactions\n\n- Several incoming transactions have been identified, consisting of payments from international suppliers located in countries known for their production of construction materials, such as China and Russia.\n- These transactions are significant in size and frequency, reflecting the customer's active procurement activities to meet demand in the local construction market.\n\n## Outgoing Transactions\n\n- On the outgoing side, multiple wire transfers have been initiated by the customer, primarily to construction companies and contractors.\n- The transaction descriptions indicate purchases of building materials for use in various construction projects across the region.\n\n## Response and Actions\n\n- In response to the flagged transactions, customer outreach has been conducted to seek clarification from the customer regarding the nature and purpose of the transactions.\n- The customer promptly provides detailed explanations, including purchase contracts and project agreements, to support the legitimacy of the transactions.\n- Additionally, the customer's compliance records indicate a history of cooperation with regulatory authorities and adherence to anti-money laundering (AML) regulations.\n	TM	1	6	{"KYC profile": {"Industry risk": true}, "Transaction analysis": {"Production risk": true}}	3
15	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "close", "difficultyLevel": "hard", "accountType": "retail", "suspiciousPattern": "high-volume-suspicious-countries")	TM	3	16	{"context": "Lotte van der Meer, a 42-year-old art dealer based in Amsterdam, has been flagged for suspicious activity due to high-volume transactions with entities in countries often associated with money laundering risks. Over a six-month period, Lotte has engaged in multiple large international wire transfers with art galleries and cultural institutions in the United Arab Emirates, Qatar, Bahrain, and Saudi Arabia. While these transactions align with her profession as an international art dealer, the frequency and volume of these transactions, coupled with cash withdrawals in some of these countries, have raised concerns. The pattern of incoming large sums followed by outgoing transfers to Hong Kong and Singapore adds another layer of complexity to the scenario. Given Lotte's background in the art world, a notoriously opaque market often scrutinized for potential money laundering, these transactions require careful examination. However, the consistent salary deposits and the fact that most transactions are with seemingly legitimate businesses in the art sector provide some mitigating factors to consider.", "persona": {"age": 42, "name": "Lotte van der Meer", "background": "Lotte is a successful art dealer based in Amsterdam. She frequently travels internationally for work, attending art fairs and auctions. She has a passion for contemporary art and has built a strong network of clients and artists worldwide. Recently, she's been expanding her business into emerging markets in Asia and the Middle East.", "occupation": "Art Dealer", "familyStatus": "Divorced", "previouslyFlagged": true}, "auxiliaryData": {"housing": 2500, "healthcare": 300, "dailyExpenses": 1200, "entertainment": 1000, "transportation": 800, "savingsInvestments": 2000, "internationalTransfers": 55000, "cashWithdrawalsDeposits": 2500}, "analystDecision": {"action": "close", "keyFactors": ["Transactions align with the client's declared profession as an international art dealer", "Most transfers are with established art galleries and cultural institutions", "Regular salary deposits indicate ongoing legitimate business activity", "Client has a history of international transactions due to the nature of her work", "While high-risk countries are involved, they are known for emerging art markets, which fits the client's business expansion plans"]}, "difficultyLevel": {"level": "hard", "score": 9}, "transactionData": [{"date": "2024-01-05", "type": "incoming", "amount": 8500, "country": "Netherlands", "merchant": "Van der Meer Fine Arts", "description": "Salary deposit"}, {"date": "2024-01-10", "type": "incoming", "amount": 45000, "country": "United Arab Emirates", "merchant": "Dubai Art Gallery LLC", "description": "International wire transfer"}, {"date": "2024-01-12", "type": "outgoing", "amount": -2000, "country": "Netherlands", "merchant": "ING ATM Museumplein", "description": "ATM withdrawal"}, {"date": "2024-01-15", "type": "outgoing", "amount": -38000, "country": "Hong Kong", "merchant": "AsiaArt Holdings Ltd", "description": "International wire transfer"}, {"date": "2024-01-20", "type": "outgoing", "amount": -3500, "country": "Netherlands", "merchant": "ING Bank", "description": "Credit card payment"}, {"date": "2024-02-03", "type": "incoming", "amount": 62000, "country": "Qatar", "merchant": "Doha Cultural Investments", "description": "International wire transfer"}, {"date": "2024-02-05", "type": "incoming", "amount": 8500, "country": "Netherlands", "merchant": "Van der Meer Fine Arts", "description": "Salary deposit"}, {"date": "2024-02-10", "type": "outgoing", "amount": -55000, "country": "Singapore", "merchant": "SingaporeArt Pte Ltd", "description": "International wire transfer"}, {"date": "2024-02-15", "type": "outgoing", "amount": -1500, "country": "United Arab Emirates", "merchant": "Emirates NBD ATM Dubai Mall", "description": "ATM withdrawal"}, {"date": "2024-02-20", "type": "incoming", "amount": 33000, "country": "Bahrain", "merchant": "Manama Art Consulting W.L.L.", "description": "International wire transfer"}, {"date": "2024-03-05", "type": "incoming", "amount": 8500, "country": "Netherlands", "merchant": "Van der Meer Fine Arts", "description": "Salary deposit"}, {"date": "2024-03-10", "type": "incoming", "amount": 70000, "country": "Saudi Arabia", "merchant": "Riyadh Fine Arts Co.", "description": "International wire transfer"}, {"date": "2024-03-15", "type": "outgoing", "amount": -68000, "country": "Hong Kong", "merchant": "AsiaArt Holdings Ltd", "description": "International wire transfer"}, {"date": "2024-03-20", "type": "outgoing", "amount": -3000, "country": "Netherlands", "merchant": "ABN AMRO ATM Schiphol Airport", "description": "ATM withdrawal"}, {"date": "2024-04-05", "type": "incoming", "amount": 8500, "country": "Netherlands", "merchant": "Van der Meer Fine Arts", "description": "Salary deposit"}, {"date": "2024-04-12", "type": "incoming", "amount": 52000, "country": "United Arab Emirates", "merchant": "Abu Dhabi Culture Foundation", "description": "International wire transfer"}, {"date": "2024-04-18", "type": "outgoing", "amount": -49000, "country": "Singapore", "merchant": "SingaporeArt Pte Ltd", "description": "International wire transfer"}, {"date": "2024-04-25", "type": "outgoing", "amount": -2500, "country": "Qatar", "merchant": "Qatar National Bank ATM", "description": "ATM withdrawal"}, {"date": "2024-05-05", "type": "incoming", "amount": 8500, "country": "Netherlands", "merchant": "Van der Meer Fine Arts", "description": "Salary deposit"}, {"date": "2024-05-15", "type": "incoming", "amount": 58000, "country": "Bahrain", "merchant": "Manama Art Consulting W.L.L.", "description": "International wire transfer"}, {"date": "2024-05-20", "type": "outgoing", "amount": -61000, "country": "Hong Kong", "merchant": "AsiaArt Holdings Ltd", "description": "International wire transfer"}, {"date": "2024-05-28", "type": "outgoing", "amount": -2000, "country": "Netherlands", "merchant": "Rabobank ATM Vondelpark", "description": "ATM withdrawal"}, {"date": "2024-06-05", "type": "incoming", "amount": 8500, "country": "Netherlands", "merchant": "Van der Meer Fine Arts", "description": "Salary deposit"}, {"date": "2024-06-12", "type": "incoming", "amount": 67000, "country": "Saudi Arabia", "merchant": "Riyadh Fine Arts Co.", "description": "International wire transfer"}, {"date": "2024-06-18", "type": "outgoing", "amount": -64000, "country": "Singapore", "merchant": "SingaporeArt Pte Ltd", "description": "International wire transfer"}, {"date": "2024-06-25", "type": "outgoing", "amount": -3500, "country": "United Arab Emirates", "merchant": "Dubai Islamic Bank ATM", "description": "ATM withdrawal"}], "financialProfile": {"monthlyIncome": 8500, "savingsBalance": 75000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 250000}}, "suspiciousActivity": {"types": ["high-volume-suspicious-countries"], "timing": ["Throughout January to June 2024"], "amounts": [45000, 62000, 33000, 70000, 52000, 58000, 67000], "pattern": "high-volume-suspicious-countries", "frequencies": [7]}}	2
16	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "close", "difficultyLevel": "easy", "accountType": "retail", "suspiciousPattern": "fast-in-fast-out")	TM	3	16	{"context": "Sander de Boer, a 28-year-old software developer, has shown a pattern of receiving large incoming transfers from cryptocurrency exchanges, followed by quick outgoing transfers to savings or investment accounts. This 'fast-in-fast-out' pattern occurred six times over a six-month period. While this behavior could be indicative of money laundering, it's also consistent with someone actively managing their cryptocurrency investments and promptly securing profits in more traditional financial instruments.", "persona": {"age": 28, "name": "Sander de Boer", "background": "Sander is a young professional working for a tech startup in Utrecht. He's tech-savvy and often uses online platforms for various financial transactions. Recently, he's been exploring cryptocurrency investments, which has led to some unusual transaction patterns in his account.", "occupation": "Software Developer", "familyStatus": "Single", "previouslyFlagged": false}, "auxiliaryData": {"housing": 1200, "healthcare": 150, "dailyExpenses": 1000, "entertainment": 400, "transportation": 200, "savingsInvestments": 1000, "internationalTransfers": 3300, "cashWithdrawalsDeposits": 200}, "analystDecision": {"action": "close", "keyFactors": ["Regular salary deposits indicate stable employment", "Transfers to savings and investment accounts suggest legitimate financial management", "Cryptocurrency transactions align with the client's tech-savvy profile", "No previous flags on the account", "Amounts involved are moderate and consistent with the client's income"]}, "difficultyLevel": {"level": "easy", "score": 3}, "transactionData": [{"date": "2024-01-05", "type": "incoming", "amount": 4200, "country": "Netherlands", "merchant": "TechNova B.V.", "description": "Salary deposit"}, {"date": "2024-01-15", "type": "incoming", "amount": 3000, "country": "United States", "merchant": "Coinbase", "description": "Online transfer from Coinbase"}, {"date": "2024-01-16", "type": "outgoing", "amount": -2800, "country": "Netherlands", "merchant": "ING Bank", "description": "Transfer to savings account"}, {"date": "2024-02-05", "type": "incoming", "amount": 4200, "country": "Netherlands", "merchant": "TechNova B.V.", "description": "Salary deposit"}, {"date": "2024-02-20", "type": "incoming", "amount": 2500, "country": "Malta", "merchant": "Binance", "description": "Online transfer from Binance"}, {"date": "2024-02-21", "type": "outgoing", "amount": -2300, "country": "Netherlands", "merchant": "DeGiro", "description": "Transfer to investment account"}, {"date": "2024-03-05", "type": "incoming", "amount": 4200, "country": "Netherlands", "merchant": "TechNova B.V.", "description": "Salary deposit"}, {"date": "2024-03-18", "type": "incoming", "amount": 3500, "country": "United States", "merchant": "Kraken", "description": "Online transfer from Kraken"}, {"date": "2024-03-19", "type": "outgoing", "amount": -3200, "country": "Netherlands", "merchant": "ING Bank", "description": "Transfer to savings account"}, {"date": "2024-04-05", "type": "incoming", "amount": 4200, "country": "Netherlands", "merchant": "TechNova B.V.", "description": "Salary deposit"}, {"date": "2024-04-22", "type": "incoming", "amount": 4000, "country": "United States", "merchant": "Coinbase", "description": "Online transfer from Coinbase"}, {"date": "2024-04-23", "type": "outgoing", "amount": -3800, "country": "Netherlands", "merchant": "DeGiro", "description": "Transfer to investment account"}, {"date": "2024-05-05", "type": "incoming", "amount": 4200, "country": "Netherlands", "merchant": "TechNova B.V.", "description": "Salary deposit"}, {"date": "2024-05-17", "type": "incoming", "amount": 3200, "country": "Malta", "merchant": "Binance", "description": "Online transfer from Binance"}, {"date": "2024-05-18", "type": "outgoing", "amount": -3000, "country": "Netherlands", "merchant": "ING Bank", "description": "Transfer to savings account"}, {"date": "2024-06-05", "type": "incoming", "amount": 4200, "country": "Netherlands", "merchant": "TechNova B.V.", "description": "Salary deposit"}, {"date": "2024-06-25", "type": "incoming", "amount": 3800, "country": "United States", "merchant": "Kraken", "description": "Online transfer from Kraken"}, {"date": "2024-06-26", "type": "outgoing", "amount": -3600, "country": "Netherlands", "merchant": "DeGiro", "description": "Transfer to investment account"}], "financialProfile": {"monthlyIncome": 4200, "savingsBalance": 15000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 5000}}, "suspiciousActivity": {"types": ["fast-in-fast-out"], "timing": ["Mid-January", "Late February", "Mid-March", "Late April", "Mid-May", "Late June"], "amounts": [3000, 2500, 3500, 4000, 3200, 3800], "pattern": "fast-in-fast-out", "frequencies": [6]}}	2
9	# Customer Overview\n\nThe customer involved is a **wholesale client headquartered in Lagos, Nigeria**. The customer operates within the **oil and gas exploration industry**, specializing in providing drilling equipment and services to companies involved in offshore and onshore exploration projects.\n\n## Incoming Transactions\n\n- Several incoming transactions have been identified, consisting of large payments from various international sources.\n- However, adverse media has surfaced regarding the customer, indicating potential involvement in fraudulent activities within the oil and gas sector. This adverse media suggests a history of regulatory violations, including allegations of bribery and corruption in securing contracts and licenses for exploration projects.\n\n## Outgoing Transactions\n\n- On the outgoing side, multiple wire transfers have been initiated by the customer, primarily to suppliers and subcontractors involved in the oil and gas exploration sector.\n- However, adverse media has also been identified on one of the counterparties, suggesting their connection to previous financial misconduct or criminal activities within the industry.\n\n## Response and Actions\n\n- In response to the flagged transactions, customer outreach has been conducted to seek clarification from the customer regarding the nature and purpose of the transactions.\n- However, the customer's responses are evasive and lack transparency, failing to provide satisfactory explanations for the unusual transaction patterns observed.\n	TM	1	6	{"KYC profile": {"Customer risk": true, "Industry risk": true, "Geographical risk": true}, "Adverse media": {"Counterparty risk": true}, "Customer outreach": {"Customer risk": true}, "Transaction analysis": {"Transaction risk": true}}	2
17	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "escalate", "difficultyLevel": "hard", "accountType": "retail", "suspiciousPattern": "fast-in-fast-out")	TM	3	16	{"context": "Eva Jansen, a 35-year-old marketing manager, has displayed a concerning pattern of large incoming transfers from various forex and cryptocurrency platforms, followed by immediate outgoing transfers to other financial entities. This 'fast-in-fast-out' pattern has occurred six times over a six-month period, with increasing amounts. While Eva's background in finance and her tech-savvy nature could explain some interest in diverse investments, the frequency, amounts, and the immediate transfer out raise red flags. The use of multiple platforms across different countries adds to the complexity. Eva's international travel, while potentially legitimate for her job, also complicates the scenario. Her previous flag history further intensifies the need for scrutiny.", "persona": {"age": 35, "name": "Eva Jansen", "background": "Eva works for a multinational company in Rotterdam. She's well-educated and has a background in finance. Recently, she's been showing increased interest in various investment opportunities, including forex trading and cryptocurrency. Eva is known to be tech-savvy and often travels for both work and leisure.", "occupation": "Marketing Manager", "familyStatus": "Married", "previouslyFlagged": true}, "auxiliaryData": {"housing": 2200, "healthcare": 250, "dailyExpenses": 1500, "entertainment": 800, "transportation": 400, "savingsInvestments": 2000, "internationalTransfers": 38800, "cashWithdrawalsDeposits": 1250}, "analystDecision": {"action": "escalate", "keyFactors": ["Repeated 'fast-in-fast-out' pattern with increasing amounts", "Use of multiple forex and crypto platforms across different jurisdictions", "Immediate transfers of large sums to other financial entities", "Previous flag on the account", "Discrepancy between transaction amounts and declared income", "International travel patterns coinciding with some large transactions"]}, "difficultyLevel": {"level": "hard", "score": 9}, "transactionData": [{"date": "2024-01-05", "type": "incoming", "amount": 6800, "country": "Netherlands", "merchant": "Global Innovations NV", "description": "Salary deposit"}, {"date": "2024-01-12", "type": "incoming", "amount": 25000, "country": "United Kingdom", "merchant": "FXCM Ltd", "description": "Online transfer from FXCM"}, {"date": "2024-01-13", "type": "outgoing", "amount": -24500, "country": "Malta", "merchant": "Binance", "description": "Transfer to Binance"}, {"date": "2024-01-20", "type": "outgoing", "amount": -1000, "country": "Netherlands", "merchant": "ING ATM Coolsingel", "description": "ATM withdrawal"}, {"date": "2024-02-05", "type": "incoming", "amount": 6800, "country": "Netherlands", "merchant": "Global Innovations NV", "description": "Salary deposit"}, {"date": "2024-02-15", "type": "incoming", "amount": 32000, "country": "United States", "merchant": "Kraken", "description": "Online transfer from Kraken"}, {"date": "2024-02-16", "type": "outgoing", "amount": -31500, "country": "United States", "merchant": "Interactive Brokers LLC", "description": "Transfer to Interactive Brokers"}, {"date": "2024-02-28", "type": "outgoing", "amount": -2500, "country": "Spain", "merchant": "Hotel Arts Barcelona", "description": "Hotel payment"}, {"date": "2024-03-05", "type": "incoming", "amount": 6800, "country": "Netherlands", "merchant": "Global Innovations NV", "description": "Salary deposit"}, {"date": "2024-03-18", "type": "incoming", "amount": 41000, "country": "Cyprus", "merchant": "eToro (Europe) Ltd", "description": "Online transfer from eToro"}, {"date": "2024-03-19", "type": "outgoing", "amount": -40500, "country": "United States", "merchant": "Coinbase", "description": "Transfer to Coinbase"}, {"date": "2024-03-25", "type": "outgoing", "amount": -3000, "country": "Netherlands", "merchant": "Bijenkorf", "description": "Online shopping"}, {"date": "2024-04-05", "type": "incoming", "amount": 6800, "country": "Netherlands", "merchant": "Global Innovations NV", "description": "Salary deposit"}, {"date": "2024-04-14", "type": "incoming", "amount": 38000, "country": "Cyprus", "merchant": "Plus500CY Ltd", "description": "Online transfer from Plus500"}, {"date": "2024-04-15", "type": "outgoing", "amount": -37500, "country": "Luxembourg", "merchant": "Bitstamp Europe SA", "description": "Transfer to Bitstamp"}, {"date": "2024-04-22", "type": "outgoing", "amount": -1800, "country": "Netherlands", "merchant": "KLM Royal Dutch Airlines", "description": "Flight tickets"}, {"date": "2024-05-05", "type": "incoming", "amount": 6800, "country": "Netherlands", "merchant": "Global Innovations NV", "description": "Salary deposit"}, {"date": "2024-05-16", "type": "incoming", "amount": 45000, "country": "Poland", "merchant": "X-Trade Brokers DM SA", "description": "Online transfer from XTB"}, {"date": "2024-05-17", "type": "outgoing", "amount": -44500, "country": "United States", "merchant": "Kraken", "description": "Transfer to Kraken"}, {"date": "2024-05-28", "type": "outgoing", "amount": -500, "country": "France", "merchant": "L'Arpège", "description": "Restaurant payment"}, {"date": "2024-06-05", "type": "incoming", "amount": 6800, "country": "Netherlands", "merchant": "Global Innovations NV", "description": "Salary deposit"}, {"date": "2024-06-20", "type": "incoming", "amount": 52000, "country": "United Kingdom", "merchant": "FXCM Ltd", "description": "Online transfer from FXCM"}, {"date": "2024-06-21", "type": "outgoing", "amount": -51500, "country": "United States", "merchant": "Interactive Brokers LLC", "description": "Transfer to Interactive Brokers"}, {"date": "2024-06-30", "type": "outgoing", "amount": -1500, "country": "Italy", "merchant": "UniCredit ATM Rome", "description": "ATM withdrawal"}], "financialProfile": {"monthlyIncome": 6800, "savingsBalance": 45000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 120000}}, "suspiciousActivity": {"types": ["fast-in-fast-out"], "timing": ["Mid-January", "Mid-February", "Mid-March", "Mid-April", "Mid-May", "Late June"], "amounts": [25000, 32000, 41000, 38000, 45000, 52000], "pattern": "fast-in-fast-out", "frequencies": [6]}}	2
1	## Compliance Due Diligence (CDD) Analysis Report\n\nAs a Compliance Due Diligence (CDD) analyst, your new task is to scrutinize the client profile of XYZ Global, a Corporate Banking client. XYZ Global is a multifaceted corporation with operations in diverse sectors across North America, Africa, and Southeast Asia.\n\n### Client Profile Examination:\nDuring your examination of XYZ Global's client profile, you encounter the following details:\n\nUltimate Beneficial Owner (UBO):\nThe Ultimate Beneficial Owner (UBO) of XYZ Global is Sarah Chen, a national of Country X, which is recognized as a medium-risk jurisdiction concerning financial crime and sanctions evasion. Sarah Chen has been linked to businesses that faced scrutiny for potential ethical lapses and minor compliance issues, but no significant legal actions have been taken against her.\n\nOwnership Structure:\nXYZ Global's ownership structure is complex, featuring several layers of subsidiaries and special purpose vehicles (SPVs) domiciled in jurisdictions that are frequently criticized for their lack of transparency and weak enforcement of anti-money laundering (AML) regulations.\n\n### Areas of Operation:\nThe company's areas of operation include technology development, green energy projects, and international trade.\n\nCompliance and Audits:\nDespite the complex ownership structure, XYZ Global has made efforts to maintain a clean compliance record. They have implemented comprehensive compliance policies, including enhanced due diligence (EDD) processes, and undergo regular audits by well-known audit firms.\n\nFinancial Transaction Analysis:\nThe analysis of XYZ Global's financial transactions shows consistent, transparent dealings with well-established and reputable business partners, indicating no immediate red flags related to their financial practices.\\\n	TM	1	6	{"KYC profile": {"Industry risk": true}, "Customer outreach": {"Production risk": true, "Geographical risk": true}, "Transaction analysis": {"Production risk": true}}	1
11	# Customer Overview\n\nThe customer involved is a **wholesale client headquartered in Miami, United States**, a jurisdiction known for its strong financial regulations and as a hub for trade with Latin America. The customer operates within the **import and distribution industry**, specializing in the distribution of agricultural products.\n\n## Incoming Transactions\n\n- Several incoming transactions have been identified, consisting of payments from international suppliers located in countries known for their agricultural production, such as Brazil and Argentina.\n- These transactions are significant in size and frequency, consistent with the customer's typical transaction history.\n\n## Outgoing Transactions\n\n- On the outgoing side, multiple wire transfers have been initiated by the customer, primarily to agricultural producers and distributors.\n- The transaction descriptions indicate routine purchases of agricultural goods such as grains and fruits.\n- Some of the payments are larger than what is usually seen in the customer’s transaction behavior.\n\n## Response and Actions\n\n- In response to the flagged transactions, customer outreach has been conducted to seek clarification from the customer regarding the nature and purpose of the transactions.\n- The customer promptly responds with detailed explanations, providing invoices and contracts supporting the legitimacy of the transactions.\n- Additionally, the customer's compliance records indicate a history of cooperation with regulatory authorities and adherence to anti-money laundering (AML) regulations.\n\n## Risk Assessment\n\nThis use-case demonstrates a relatively low-risk scenario associated with the customer's operations in the import and distribution industry in Miami. The presence of clear documentation, timely responses to inquiries, and a history of compliance contribute to a reduced risk profile. However, ongoing monitoring and due diligence are necessary to ensure continued compliance and mitigate potential financial crime risks.	TM	1	6	{"Transaction analysis": {"Industry risk": true, "Transaction risk": true, "Geographical risk": true}}	3
18	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "escalate", "difficultyLevel": "medium", "accountType": "retail", "suspiciousPattern": "high-volume-suspicious-countries")	TM	3	16	{"context": "Dirk van der Linden, a 45-year-old import/export consultant, has shown a pattern of high-volume transactions with entities in countries often associated with money laundering risks. Over a six-month period, Dirk has engaged in multiple large international wire transfers with companies in the United Arab Emirates, Saudi Arabia, Qatar, Malaysia, Indonesia, and Thailand. While these transactions align with his profession as an import/export consultant, the frequency and volume of these transactions have raised concerns. The pattern of incoming large sums quickly followed by outgoing transfers to other countries in the region adds another layer of complexity to the scenario. Given the nature of Dirk's work in facilitating trade between Dutch companies and businesses in emerging markets, these transactions require careful examination to distinguish between legitimate business activities and potential money laundering or other financial crimes.", "persona": {"age": 45, "name": "Dirk van der Linden", "background": "Dirk is a seasoned import/export consultant based in Rotterdam. He specializes in facilitating trade between Dutch companies and businesses in emerging markets. Recently, he's been expanding his client base in Southeast Asia and the Middle East. Dirk travels frequently for work and maintains a wide network of international contacts.", "occupation": "Import/Export Consultant", "familyStatus": "Divorced", "previouslyFlagged": false}, "auxiliaryData": {"housing": 1500, "healthcare": 180, "dailyExpenses": 1000, "entertainment": 400, "transportation": 250, "savingsInvestments": 1500, "internationalTransfers": 3500, "cashWithdrawalsDeposits": 1000}, "analystDecision": {"action": "escalate", "keyFactors": ["High volume and frequency of transactions with countries known for money laundering risks", "Rapid succession of incoming and outgoing international transfers", "Transactions often involve round figures, which is unusual for typical business operations", "Some transaction amounts exceed the client's monthly income", "Client's travel patterns coincide with some large transactions", "Despite alignment with the client's profession, the volume and frequency"]}, "difficultyLevel": {"level": "medium", "score": 6}, "transactionData": [{"date": "2024-01-05", "type": "incoming", "amount": 7500, "country": "Netherlands", "merchant": "Global Trade Solutions BV", "description": "Salary deposit"}, {"date": "2024-01-07", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-01-10", "type": "incoming", "amount": 25000, "country": "United Arab Emirates", "merchant": "Dubai Imports LLC", "description": "International wire transfer"}, {"date": "2024-01-12", "type": "outgoing", "amount": -120, "country": "Netherlands", "merchant": "Restaurant De Harmonie", "description": "Restaurant dinner"}, {"date": "2024-01-15", "type": "outgoing", "amount": -22000, "country": "Malaysia", "merchant": "KL Exports Sdn Bhd", "description": "International wire transfer"}, {"date": "2024-01-18", "type": "outgoing", "amount": -80, "country": "Netherlands", "merchant": "Shell Station Zuidplein", "description": "Fuel purchase"}, {"date": "2024-01-22", "type": "outgoing", "amount": -65, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-01-25", "type": "incoming", "amount": 18000, "country": "Thailand", "merchant": "Bangkok Goods Co., Ltd.", "description": "International wire transfer"}, {"date": "2024-01-28", "type": "outgoing", "amount": -50, "country": "Netherlands", "merchant": "BasicFit", "description": "Gym membership"}, {"date": "2024-01-31", "type": "outgoing", "amount": -200, "country": "Netherlands", "merchant": "Bol.com", "description": "Online shopping"}, {"date": "2024-02-05", "type": "incoming", "amount": 7500, "country": "Netherlands", "merchant": "Global Trade Solutions BV", "description": "Salary deposit"}, {"date": "2024-02-08", "type": "outgoing", "amount": -180, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-02-12", "type": "incoming", "amount": 30000, "country": "Saudi Arabia", "merchant": "Riyadh Trading Co.", "description": "International wire transfer"}, {"date": "2024-02-15", "type": "outgoing", "amount": -350, "country": "Netherlands", "merchant": "AutoService Rotterdam", "description": "Car maintenance"}, {"date": "2024-02-18", "type": "outgoing", "amount": -28000, "country": "Indonesia", "merchant": "Jakarta Exports PT", "description": "International wire transfer"}, {"date": "2024-02-22", "type": "outgoing", "amount": -95, "country": "Netherlands", "merchant": "Bazar Rotterdam", "description": "Restaurant dinner"}, {"date": "2024-02-25", "type": "outgoing", "amount": -250, "country": "Netherlands", "merchant": "De Bijenkorf", "description": "Clothing purchase"}, {"date": "2024-02-28", "type": "incoming", "amount": 22000, "country": "Qatar", "merchant": "Doha Imports W.L.L.", "description": "International wire transfer"}, {"date": "2024-03-05", "type": "incoming", "amount": 7500, "country": "Netherlands", "merchant": "Global Trade Solutions BV", "description": "Salary deposit"}, {"date": "2024-03-08", "type": "outgoing", "amount": -160, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-03-12", "type": "incoming", "amount": 28000, "country": "United Arab Emirates", "merchant": "Abu Dhabi Traders LLC", "description": "International wire transfer"}, {"date": "2024-03-15", "type": "outgoing", "amount": -850, "country": "Netherlands", "merchant": "KLM Royal Dutch Airlines", "description": "Flight tickets"}, {"date": "2024-03-18", "type": "outgoing", "amount": -25000, "country": "Malaysia", "merchant": "Penang Exports Sdn Bhd", "description": "International wire transfer"}, {"date": "2024-03-22", "type": "outgoing", "amount": -1200, "country": "United Arab Emirates", "merchant": "Burj Al Arab Jumeirah", "description": "Hotel payment"}, {"date": "2024-03-25", "type": "outgoing", "amount": -180, "country": "United Arab Emirates", "merchant": "Nobu Dubai", "description": "Restaurant dinner"}, {"date": "2024-03-28", "type": "incoming", "amount": 20000, "country": "Thailand", "merchant": "Chiang Mai Goods Co., Ltd.", "description": "International wire transfer"}, {"date": "2024-04-05", "type": "incoming", "amount": 7500, "country": "Netherlands", "merchant": "Global Trade Solutions BV", "description": "Salary deposit"}, {"date": "2024-04-08", "type": "outgoing", "amount": -170, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-04-12", "type": "incoming", "amount": 32000, "country": "Saudi Arabia", "merchant": "Jeddah Imports Est.", "description": "International wire transfer"}, {"date": "2024-04-15", "type": "outgoing", "amount": -800, "country": "Netherlands", "merchant": "MediaMarkt", "description": "Electronics purchase"}, {"date": "2024-04-18", "type": "outgoing", "amount": -29000, "country": "Indonesia", "merchant": "Surabaya Traders PT", "description": "International wire transfer"}, {"date": "2024-04-22", "type": "outgoing", "amount": -68, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-04-25", "type": "outgoing", "amount": -110, "country": "Netherlands", "merchant": "Restaurant Parkheuvel", "description": "Restaurant dinner"}, {"date": "2024-04-28", "type": "incoming", "amount": 24000, "country": "Qatar", "merchant": "Doha Exports W.L.L.", "description": "International wire transfer"}, {"date": "2024-05-05", "type": "incoming", "amount": 7500, "country": "Netherlands", "merchant": "Global Trade Solutions BV", "description": "Salary deposit"}, {"date": "2024-05-08", "type": "outgoing", "amount": -190, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-05-12", "type": "incoming", "amount": 35000, "country": "United Arab Emirates", "merchant": "Sharjah Trading LLC", "description": "International wire transfer"}, {"date": "2024-05-15", "type": "outgoing", "amount": -450, "country": "Netherlands", "merchant": "Centraal Beheer", "description": "Car insurance"}, {"date": "2024-05-18", "type": "outgoing", "amount": -32000, "country": "Malaysia", "merchant": "Johor Bahru Exports Sdn Bhd", "description": "International wire transfer"}, {"date": "2024-05-22", "type": "outgoing", "amount": -300, "country": "Netherlands", "merchant": "Zalando", "description": "Clothing purchase"}, {"date": "2024-05-25", "type": "outgoing", "amount": -50, "country": "Netherlands", "merchant": "BasicFit", "description": "Gym membership"}, {"date": "2024-05-28", "type": "incoming", "amount": 26000, "country": "Thailand", "merchant": "Phuket Goods Co., Ltd.", "description": "International wire transfer"}, {"date": "2024-06-05", "type": "incoming", "amount": 7500, "country": "Netherlands", "merchant": "Global Trade Solutions BV", "description": "Salary deposit"}, {"date": "2024-06-08", "type": "outgoing", "amount": -200, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-06-12", "type": "incoming", "amount": 38000, "country": "Saudi Arabia", "merchant": "Dammam Trading Co.", "description": "International wire transfer"}, {"date": "2024-06-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "Klusjesman Rotterdam", "description": "Home repairs"}, {"date": "2024-06-18", "type": "outgoing", "amount": -35000, "country": "Indonesia", "merchant": "Bali Exports PT", "description": "International wire transfer"}, {"date": "2024-06-22", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "FG Restaurant", "description": "Restaurant dinner"}, {"date": "2024-06-25", "type": "outgoing", "amount": -1100, "country": "Netherlands", "merchant": "Emirates", "description": "Flight tickets"}, {"date": "2024-06-28", "type": "incoming", "amount": 30000, "country": "Qatar", "merchant": "Doha Global Traders W.L.L.", "description": "International wire transfer"}], "financialProfile": {"monthlyIncome": 7500, "savingsBalance": 65000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 180000}}, "suspiciousActivity": {"types": ["high-volume-suspicious-countries"], "timing": ["Throughout January to June 2024"], "amounts": [25000, 30000, 28000, 32000, 35000, 38000], "pattern": "high-volume-suspicious-countries", "frequencies": [12]}}	2
99	YOU MADE IT TO LESSON2. YOU ARE A FUCKING GENIUS MY FRIEND A GENIUS I SAY!!!	TM	2	6	{"KYC profile": {"Customer risk": true, "Industry risk": true, "Geographical risk": true}, "Adverse media": {"Counterparty risk": true}, "Customer outreach": {"Customer risk": true}, "Transaction analysis": {"Transaction risk": true}}	2
19	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "escalate", "difficultyLevel": "medium", "accountType": "retail", "suspiciousPattern": "large-atm-withdrawals")	TM	3	16	{"context": "Marieke de Vries, a 38-year-old real estate agent in Amsterdam, has shown a pattern of unusually large and frequent ATM withdrawals over a six-month period. These withdrawals, often close to or exceeding €9,000, occur approximately twice a month and are significantly larger than what would be expected for normal cash needs. While Marieke's high income and luxurious lifestyle could explain some cash usage, the frequency and amounts of these withdrawals raise concerns about potential money laundering or other illicit activities. The pattern is particularly suspicious given that the Netherlands is increasingly moving towards digital payments, making such large cash withdrawals unusual. Additionally, Marieke's high-value purchases in art and jewelry, combined with international travel and dining at exclusive restaurants, create a complex financial picture that requires further scrutiny. The cash withdrawals could potentially be linked to undeclared income from real estate transactions or used for high-value purchases to evade taxation or reporting requirements.", "persona": {"age": 38, "name": "Marieke de Vries", "background": "Marieke is a successful real estate agent working in Amsterdam. She's known for her ability to close high-value property deals and has a wide network of wealthy clients. Marieke leads a luxurious lifestyle and frequently attends exclusive events. Recently, she's been showing interest in art collecting and has made several high-value purchases.", "occupation": "Real Estate Agent", "familyStatus": "Single", "previouslyFlagged": false}, "auxiliaryData": {"housing": 3500, "healthcare": 300, "dailyExpenses": 350, "entertainment": 2000, "transportation": 800, "savingsInvestments": 2500, "internationalTransfers": 0, "cashWithdrawalsDeposits": 18000}, "analystDecision": {"action": "escalate", "keyFactors": ["Frequent large ATM withdrawals, often near €9,000, occurring roughly twice a month", "Total cash withdrawals significantly exceed expected cash needs for daily expenses", "Pattern of withdrawals is inconsistent with the trend towards digital payments in the Netherlands", "High-value purchases in cash-intensive sectors like art and jewelry", "Lifestyle expenses and purchasing patterns suggest potential undeclared income", "Previous ATM withdrawal activity (if any) shows a significant increase in frequency and amount"]}, "difficultyLevel": {"level": "medium", "score": 6}, "transactionData": [{"date": "2024-01-05", "type": "incoming", "amount": 9500, "country": "Netherlands", "merchant": "Amsterdam Luxury Real Estate BV", "description": "Salary deposit"}, {"date": "2024-01-07", "type": "outgoing", "amount": -250, "country": "Netherlands", "merchant": "Albert Heijn XL", "description": "Grocery shopping"}, {"date": "2024-01-10", "type": "outgoing", "amount": -9000, "country": "Netherlands", "merchant": "ING ATM Leidseplein", "description": "ATM withdrawal"}, {"date": "2024-01-12", "type": "outgoing", "amount": -380, "country": "Netherlands", "merchant": "Restaurant De Kas", "description": "Restaurant dinner"}, {"date": "2024-01-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "P.C. Hooftstraat Boutique", "description": "Clothing purchase"}, {"date": "2024-01-18", "type": "outgoing", "amount": -120, "country": "Netherlands", "merchant": "Shell Station Amstelveen", "description": "Fuel purchase"}, {"date": "2024-01-22", "type": "outgoing", "amount": -85, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-01-25", "type": "outgoing", "amount": -8500, "country": "Netherlands", "merchant": "ABN AMRO ATM Zuidas", "description": "ATM withdrawal"}, {"date": "2024-01-28", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "Luxury Fitness Club", "description": "Gym membership"}, {"date": "2024-01-31", "type": "outgoing", "amount": -500, "country": "Netherlands", "merchant": "Net-a-Porter", "description": "Online shopping"}, {"date": "2024-02-05", "type": "incoming", "amount": 9500, "country": "Netherlands", "merchant": "Amsterdam Luxury Real Estate BV", "description": "Salary deposit"}, {"date": "2024-02-08", "type": "outgoing", "amount": -280, "country": "Netherlands", "merchant": "Marqt", "description": "Grocery shopping"}, {"date": "2024-02-12", "type": "outgoing", "amount": -9500, "country": "Netherlands", "merchant": "Rabobank ATM Museumplein", "description": "ATM withdrawal"}, {"date": "2024-02-15", "type": "outgoing", "amount": -750, "country": "Netherlands", "merchant": "Luxury Car Service Amsterdam", "description": "Car maintenance"}, {"date": "2024-02-18", "type": "outgoing", "amount": -420, "country": "Netherlands", "merchant": "Ciel Bleu Restaurant", "description": "Restaurant dinner"}, {"date": "2024-02-22", "type": "outgoing", "amount": -300, "country": "Netherlands", "merchant": "Conservatorium Spa", "description": "Spa treatment"}, {"date": "2024-02-25", "type": "outgoing", "amount": -8000, "country": "Netherlands", "merchant": "ING ATM Rembrandtplein", "description": "ATM withdrawal"}, {"date": "2024-02-28", "type": "outgoing", "amount": -15000, "country": "Netherlands", "merchant": "Amsterdam Art Gallery", "description": "Art purchase"}, {"date": "2024-03-05", "type": "incoming", "amount": 9500, "country": "Netherlands", "merchant": "Amsterdam Luxury Real Estate BV", "description": "Salary deposit"}, {"date": "2024-03-08", "type": "outgoing", "amount": -260, "country": "Netherlands", "merchant": "Albert Heijn XL", "description": "Grocery shopping"}, {"date": "2024-03-12", "type": "outgoing", "amount": -9800, "country": "Netherlands", "merchant": "ABN AMRO ATM Dam Square", "description": "ATM withdrawal"}, {"date": "2024-03-15", "type": "outgoing", "amount": -3500, "country": "Netherlands", "merchant": "KLM Royal Dutch Airlines", "description": "Flight tickets"}, {"date": "2024-03-18", "type": "outgoing", "amount": -2800, "country": "France", "merchant": "Ritz Paris", "description": "Hotel payment"}, {"date": "2024-03-22", "type": "outgoing", "amount": -650, "country": "France", "merchant": "L'Arpège", "description": "Restaurant dinner"}, {"date": "2024-03-25", "type": "outgoing", "amount": -8500, "country": "France", "merchant": "BNP Paribas ATM Champs-Élysées", "description": "ATM withdrawal"}, {"date": "2024-03-28", "type": "outgoing", "amount": -4500, "country": "France", "merchant": "Chanel Rue Cambon", "description": "Clothing purchase"}, {"date": "2024-04-05", "type": "incoming", "amount": 9500, "country": "Netherlands", "merchant": "Amsterdam Luxury Real Estate BV", "description": "Salary deposit"}, {"date": "2024-04-08", "type": "outgoing", "amount": -270, "country": "Netherlands", "merchant": "Marqt", "description": "Grocery shopping"}, {"date": "2024-04-12", "type": "outgoing", "amount": -9200, "country": "Netherlands", "merchant": "Rabobank ATM Vondelpark", "description": "ATM withdrawal"}, {"date": "2024-04-15", "type": "outgoing", "amount": -2800, "country": "Netherlands", "merchant": "De Bijenkorf", "description": "Electronics purchase"}, {"date": "2024-04-18", "type": "outgoing", "amount": -380, "country": "Netherlands", "merchant": "Librije's Zusje Amsterdam", "description": "Restaurant dinner"}, {"date": "2024-04-22", "type": "outgoing", "amount": -88, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-04-25", "type": "outgoing", "amount": -8800, "country": "Netherlands", "merchant": "ING ATM Centraal Station", "description": "ATM withdrawal"}, {"date": "2024-04-28", "type": "outgoing", "amount": -1800, "country": "Netherlands", "merchant": "Spa Zuiver Amsterdam", "description": "Spa weekend"}, {"date": "2024-05-05", "type": "incoming", "amount": 9500, "country": "Netherlands", "merchant": "Amsterdam Luxury Real Estate BV", "description": "Salary deposit"}, {"date": "2024-05-08", "type": "outgoing", "amount": -290, "country": "Netherlands", "merchant": "Albert Heijn XL", "description": "Grocery shopping"}, {"date": "2024-05-12", "type": "outgoing", "amount": -9600, "country": "Netherlands", "merchant": "ABN AMRO ATM Museum Quarter", "description": "ATM withdrawal"}, {"date": "2024-05-15", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "Centraal Beheer", "description": "Car insurance"}, {"date": "2024-05-18", "type": "outgoing", "amount": -450, "country": "Netherlands", "merchant": "Vinkeles", "description": "Restaurant dinner"}, {"date": "2024-05-22", "type": "outgoing", "amount": -3500, "country": "Netherlands", "merchant": "P.C. Hooftstraat Boutique", "description": "Clothing purchase"}, {"date": "2024-05-25", "type": "outgoing", "amount": -9000, "country": "Netherlands", "merchant": "Rabobank ATM Jordaan", "description": "ATM withdrawal"}, {"date": "2024-05-28", "type": "outgoing", "amount": -22000, "country": "Netherlands", "merchant": "Sotheby's Amsterdam", "description": "Art auction"}, {"date": "2024-06-05", "type": "incoming", "amount": 9500, "country": "Netherlands", "merchant": "Amsterdam Luxury Real Estate BV", "description": "Salary deposit"}, {"date": "2024-06-08", "type": "outgoing", "amount": -300, "country": "Netherlands", "merchant": "Marqt", "description": "Grocery shopping"}, {"date": "2024-06-12", "type": "outgoing", "amount": -9700, "country": "Netherlands", "merchant": "ING ATM Zuidas", "description": "ATM withdrawal"}, {"date": "2024-06-15", "type": "outgoing", "amount": -5500, "country": "Netherlands", "merchant": "The Frozen Fountain", "description": "Home decor"}, {"date": "2024-06-18", "type": "outgoing", "amount": -520, "country": "Netherlands", "merchant": "Rijks®", "description": "Restaurant dinner"}, {"date": "2024-06-22", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "Luxury Fitness Club", "description": "Gym membership"}, {"date": "2024-06-25", "type": "outgoing", "amount": -9300, "country": "Netherlands", "merchant": "ABN AMRO ATM Kalverstraat", "description": "ATM withdrawal"}, {"date": "2024-06-28", "type": "outgoing", "amount": -18000, "country": "Netherlands", "merchant": "Gassan Diamonds", "description": "Jewelry purchase"}], "financialProfile": {"monthlyIncome": 9500, "savingsBalance": 85000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 220000}}, "suspiciousActivity": {"types": ["large-atm-withdrawals"], "timing": ["Throughout January to June 2024"], "amounts": [9000, 8500, 9500, 8000, 9800, 8500, 9200, 8800, 9600, 9000, 9700, 9300], "pattern": "large-atm-withdrawals", "frequencies": [12]}}	2
20	GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "close", "difficultyLevel": "hard", "accountType": "retail", "suspiciousPattern": "large-atm-withdrawals")	TM	3	16	{"context": "Pieter van den Berg, a 52-year-old antique dealer based in Utrecht, has exhibited a pattern of large ATM withdrawals over a six-month period. These withdrawals, consistently around €9,000, occur approximately twice a month and raise initial concerns due to their size and frequency. However, several factors complicate this scenario:\\n\\n1. Nature of Business: The antique trade often involves cash transactions, especially when dealing with private collectors or at antique fairs.\\n2. Travel Pattern: Pieter's frequent trips to other European countries align with his business needs and could explain some of the cash withdrawals for on-site purchases.\\n3. Business Income: The regular large deposits into his account from his antique business provide a legitimate source for the withdrawn funds.\\n4. Transaction History: While the ATM withdrawals are large, they are consistent with his overall financial picture, including his income and business expenses.\\n5. Previous Flag: Pieter's account has been flagged before, which requires extra scrutiny. However, this could also indicate that his business model has been previously examined and understood by the bank.\\n6. Lifestyle and Expenses: His other transactions, including high-end hotel stays and restaurants, are consistent with his business profile and income level.\\n\\nThe complexity of this case lies in distinguishing between legitimate cash needs for a high-value, cash-intensive business and potential money laundering activities. The consistency of the withdrawal amounts and timing suggests a pattern, but it also aligns with a structured business operation. The international nature of his business further complicates the assessment of his financial activities.", "persona": {"age": 52, "name": "Pieter van den Berg", "background": "Pieter is a well-established antique dealer based in Utrecht. He owns a high-end antique shop in the city center and frequently travels across Europe for auctions and to meet private collectors. Pieter has been in the business for over 25 years and has built a reputation for dealing with rare and valuable items. He's known for his expertise in 17th-century Dutch art and furniture. Recently, he's been expanding his business to include online sales and international shipping.", "occupation": "Antique Dealer", "familyStatus": "Married", "previouslyFlagged": true}, "auxiliaryData": {"housing": 3500, "healthcare": 600, "dailyExpenses": 450, "entertainment": 1800, "transportation": 1200, "savingsInvestments": 3000, "internationalTransfers": 5000, "cashWithdrawalsDeposits": 18500}, "analystDecision": {"action": "close", "keyFactors": ["Consistent pattern of large ATM withdrawals aligns with the cash-intensive nature of the antique business", "Regular business income deposits provide a legitimate source for the withdrawn funds", "Travel patterns and expenses correspond with the client's business model of attending international antique fairs and auctions", "Overall financial activity, including high-value purchases and business expenses, is consistent with the client's declared occupation and income", "Despite previous flagging, the client's business model appears to have been established and understood by the bank", "No evidence of structuring or attempting to avoid reporting thresholds, as withdrawals consistently approach but do not exceed €10,000", "Client's long-standing reputation in the antique business (over 25 years) adds credibility to his financial patterns"]}, "difficultyLevel": {"level": "hard", "score": 9}, "transactionData": [{"date": "2024-01-02", "type": "incoming", "amount": 28500, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-01-05", "type": "outgoing", "amount": -320, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-01-08", "type": "outgoing", "amount": -9500, "country": "Netherlands", "merchant": "ING ATM Vredenburg", "description": "ATM withdrawal"}, {"date": "2024-01-10", "type": "outgoing", "amount": -850, "country": "Netherlands", "merchant": "KLM", "description": "Flight tickets"}, {"date": "2024-01-15", "type": "outgoing", "amount": -1200, "country": "Belgium", "merchant": "Hotel Amigo Brussels", "description": "Hotel payment"}, {"date": "2024-01-18", "type": "outgoing", "amount": -15000, "country": "Belgium", "merchant": "Brussels Antique Market", "description": "Antique purchase"}, {"date": "2024-01-20", "type": "outgoing", "amount": -280, "country": "Netherlands", "merchant": "Restaurant Vroeg", "description": "Restaurant dinner"}, {"date": "2024-01-23", "type": "outgoing", "amount": -9000, "country": "Netherlands", "merchant": "Rabobank ATM Domplein", "description": "ATM withdrawal"}, {"date": "2024-01-28", "type": "incoming", "amount": 22000, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-02-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "ABN AMRO Bank", "description": "Mortgage payment"}, {"date": "2024-02-05", "type": "outgoing", "amount": -290, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-02-08", "type": "outgoing", "amount": -9200, "country": "Netherlands", "merchant": "ING ATM Central Station", "description": "ATM withdrawal"}, {"date": "2024-02-12", "type": "outgoing", "amount": -3500, "country": "Netherlands", "merchant": "Antique Restoration Services", "description": "Business expense"}, {"date": "2024-02-15", "type": "outgoing", "amount": -4800, "country": "United Kingdom", "merchant": "Christie's Auctions", "description": "Online payment"}, {"date": "2024-02-18", "type": "outgoing", "amount": -350, "country": "Netherlands", "merchant": "Restaurant Podium", "description": "Restaurant dinner"}, {"date": "2024-02-22", "type": "outgoing", "amount": -8800, "country": "Netherlands", "merchant": "ABN AMRO ATM Nobelstraat", "description": "ATM withdrawal"}, {"date": "2024-02-25", "type": "incoming", "amount": 31000, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-03-01", "type": "outgoing", "amount": -380, "country": "Netherlands", "merchant": "Eneco", "description": "Utility bills"}, {"date": "2024-03-05", "type": "outgoing", "amount": -310, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-03-08", "type": "outgoing", "amount": -9400, "country": "Netherlands", "merchant": "Rabobank ATM Oudegracht", "description": "ATM withdrawal"}, {"date": "2024-03-12", "type": "outgoing", "amount": -1100, "country": "Netherlands", "merchant": "Lufthansa", "description": "Flight tickets"}, {"date": "2024-03-15", "type": "outgoing", "amount": -1800, "country": "Germany", "merchant": "Hotel Adlon Kempinski Berlin", "description": "Hotel payment"}, {"date": "2024-03-18", "type": "outgoing", "amount": -28000, "country": "Germany", "merchant": "Berlin Antique Fair", "description": "Antique purchase"}, {"date": "2024-03-22", "type": "outgoing", "amount": -9100, "country": "Germany", "merchant": "Deutsche Bank ATM Mitte", "description": "ATM withdrawal"}, {"date": "2024-03-25", "type": "incoming", "amount": 35000, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-03-28", "type": "outgoing", "amount": -750, "country": "Netherlands", "merchant": "Auto Service Utrecht", "description": "Car maintenance"}, {"date": "2024-04-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "ABN AMRO Bank", "description": "Mortgage payment"}, {"date": "2024-04-05", "type": "outgoing", "amount": -340, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-04-08", "type": "outgoing", "amount": -9300, "country": "Netherlands", "merchant": "ING ATM Janskerkhof", "description": "ATM withdrawal"}, {"date": "2024-04-12", "type": "outgoing", "amount": -5200, "country": "Netherlands", "merchant": "Antique Packaging Supplies", "description": "Business expense"}, {"date": "2024-04-15", "type": "outgoing", "amount": -8500, "country": "France", "merchant": "Drouot Digital", "description": "Online payment"}, {"date": "2024-04-18", "type": "outgoing", "amount": -420, "country": "Netherlands", "merchant": "Restaurant Ivy", "description": "Restaurant dinner"}, {"date": "2024-04-22", "type": "outgoing", "amount": -8900, "country": "Netherlands", "merchant": "ABN AMRO ATM Lange Viestraat", "description": "ATM withdrawal"}, {"date": "2024-04-25", "type": "incoming", "amount": 29000, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-04-28", "type": "outgoing", "amount": -410, "country": "Netherlands", "merchant": "CZ Zorgverzekering", "description": "Health insurance"}, {"date": "2024-05-01", "type": "outgoing", "amount": -360, "country": "Netherlands", "merchant": "Vattenfall", "description": "Utility bills"}, {"date": "2024-05-05", "type": "outgoing", "amount": -330, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-05-08", "type": "outgoing", "amount": -9600, "country": "Netherlands", "merchant": "Rabobank ATM Neude", "description": "ATM withdrawal"}, {"date": "2024-05-12", "type": "outgoing", "amount": -980, "country": "Netherlands", "merchant": "Air France", "description": "Flight tickets"}, {"date": "2024-05-15", "type": "outgoing", "amount": -2200, "country": "France", "merchant": "Ritz Paris", "description": "Hotel payment"}, {"date": "2024-05-18", "type": "outgoing", "amount": -42000, "country": "France", "merchant": "Marché aux Puces de Saint-Ouen", "description": "Antique purchase"}, {"date": "2024-05-22", "type": "outgoing", "amount": -9200, "country": "France", "merchant": "BNP Paribas ATM Champs-Élysées", "description": "ATM withdrawal"}, {"date": "2024-05-25", "type": "incoming", "amount": 38000, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-05-28", "type": "outgoing", "amount": -890, "country": "Netherlands", "merchant": "Centraal Beheer", "description": "Car insurance"}, {"date": "2024-06-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "ABN AMRO Bank", "description": "Mortgage payment"}, {"date": "2024-06-05", "type": "outgoing", "amount": -350, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-06-08", "type": "outgoing", "amount": -9400, "country": "Netherlands", "merchant": "ING ATM Stadhuisbrug", "description": "ATM withdrawal"}, {"date": "2024-06-12", "type": "outgoing", "amount": -6800, "country": "Netherlands", "merchant": "Antique Restoration Experts", "description": "Business expense"}, {"date": "2024-06-15", "type": "outgoing", "amount": -12000, "country": "United Kingdom", "merchant": "Sotheby's", "description": "Online payment"}, {"date": "2024-06-18", "type": "outgoing", "amount": -380, "country": "Netherlands", "merchant": "Restaurant Voltaire", "description": "Restaurant dinner"}, {"date": "2024-06-22", "type": "outgoing", "amount": -9100, "country": "Netherlands", "merchant": "ABN AMRO ATM Voorstraat", "description": "ATM withdrawal"}, {"date": "2024-06-25", "type": "incoming", "amount": 33000, "country": "Netherlands", "merchant": "Van den Berg Antiques", "description": "Business income"}, {"date": "2024-06-28", "type": "outgoing", "amount": -1200, "country": "Netherlands", "merchant": "Gemeente Utrecht", "description": "Property tax"}], "financialProfile": {"monthlyIncome": 12000, "savingsBalance": 180000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 450000}}, "suspiciousActivity": {"types": ["large-atm-withdrawals"], "timing": ["Throughout January to June 2024"], "amounts": [9500, 9000, 9200, 8800, 9400, 9100, 9300, 8900, 9600, 9200, 9400, 9100], "pattern": "large-atm-withdrawals", "frequencies": [12]}}	2
21	 GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "close", "difficultyLevel": "hard", "accountType": "retail", "suspiciousPattern": "fast-in-fast-out")	TM	3	16	{"context": "Femke Visser, a 41-year-old freelance event planner, exhibits a pattern of large incoming transfers quickly followed by outgoing transfers, often to cryptocurrency exchanges. This 'fast-in-fast-out' pattern occurs roughly twice a month and involves substantial sums, typically ranging from €45,000 to €80,000. While this pattern initially raises red flags for potential money laundering, several factors complicate the assessment:\\n\\n1. Nature of Business: As a high-end event planner, Femke deals with large sums for corporate events and luxury weddings, which could explain the high-value transactions.\\n2. International Clientele: Her diverse international client base justifies transfers from various countries.\\n3. Use of Cryptocurrency: Femke's personal interest in and use of cryptocurrency for international payments adds a layer of complexity but also aligns with her global business model.\\n4. Consistent Business Pattern: The regularity of these transactions suggests an established business pattern rather than sporadic, potentially illicit activities.\\n5. Previous Flag History: While her account has been flagged before, this could be due to the unusual nature of her business rather than actual suspicious activity.\\n6. Lifestyle Consistency: Her personal expenses, while high-end, are consistent with her income level and profession.\\n7. Vendor Payments: Large outgoing transfers often correspond to payments to event-related vendors in various countries, aligning with her business operations.\\n\\nThe complexity of this case lies in distinguishing between legitimate business operations in a fast-paced, high-value industry and potential money laundering activities. The use of cryptocurrency adds an additional layer of scrutiny required. However, the overall pattern of transactions appears consistent with a successful international event planning business.", "persona": {"age": 41, "name": "Femke Visser", "background": "Femke is a highly sought-after event planner based in Amsterdam, specializing in high-end corporate events and luxury weddings. She has a diverse international client base and often travels for work. Femke is known for her ability to organize extravagant events on short notice, sometimes requiring quick financial transactions. She has a personal interest in cryptocurrency and often uses it for international payments due to its speed and lower fees.", "occupation": "Freelance Event Planner", "familyStatus": "Single", "previouslyFlagged": true}, "auxiliaryData": {"housing": 2500, "healthcare": 200, "dailyExpenses": 300, "entertainment": 1200, "transportation": 800, "savingsInvestments": 5000, "internationalTransfers": 55000, "cashWithdrawalsDeposits": 2000}, "analystDecision": {"action": "close", "keyFactors": ["Transaction patterns, while unusual, are consistent with the nature of high-end international event planning", "Incoming transfers correspond to specific events or clients, and outgoing transfers often match vendor payments", "Use of cryptocurrency, while adding complexity, aligns with the need for quick international transfers in the event industry", "Regular personal expenses and rent payments suggest a stable lifestyle consistent with declared income", "Despite large sums, there's no attempt to structure transactions to avoid reporting thresholds", "Previous flag history has likely led to enhanced due diligence, potentially explaining and verifying the business model", "The consistent pattern over six months indicates an established business practice rather than sporadic suspicious activity"]}, "difficultyLevel": {"level": "hard", "score": 9}, "transactionData": [{"date": "2024-01-03", "type": "incoming", "amount": 45000, "country": "Netherlands", "merchant": "Global Tech Conference", "description": "Event planning fee"}, {"date": "2024-01-04", "type": "outgoing", "amount": -40000, "country": "Malta", "merchant": "Binance", "description": "Transfer to Binance"}, {"date": "2024-01-05", "type": "outgoing", "amount": -250, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-01-08", "type": "outgoing", "amount": -8500, "country": "Netherlands", "merchant": "Event Essentials BV", "description": "Event supplies"}, {"date": "2024-01-10", "type": "outgoing", "amount": -180, "country": "Netherlands", "merchant": "Restaurant De Kas", "description": "Restaurant dinner"}, {"date": "2024-01-15", "type": "incoming", "amount": 38000, "country": "United States", "merchant": "Kraken", "description": "Transfer from Kraken"}, {"date": "2024-01-16", "type": "outgoing", "amount": -35000, "country": "Germany", "merchant": "Berlin Catering GmbH", "description": "Vendor payment"}, {"date": "2024-01-20", "type": "outgoing", "amount": -80, "country": "Netherlands", "merchant": "Fit For Free", "description": "Gym membership"}, {"date": "2024-01-25", "type": "incoming", "amount": 55000, "country": "United Kingdom", "merchant": "London Fashion Week", "description": "Event planning fee"}, {"date": "2024-01-26", "type": "outgoing", "amount": -50000, "country": "United States", "merchant": "Coinbase", "description": "Transfer to Coinbase"}, {"date": "2024-01-28", "type": "outgoing", "amount": -75, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-02-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "Amsterdam Real Estate", "description": "Rent payment"}, {"date": "2024-02-05", "type": "outgoing", "amount": -220, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-02-10", "type": "incoming", "amount": 42000, "country": "Malta", "merchant": "Binance", "description": "Transfer from Binance"}, {"date": "2024-02-11", "type": "outgoing", "amount": -38000, "country": "France", "merchant": "Paris Floral Designs", "description": "Vendor payment"}, {"date": "2024-02-15", "type": "outgoing", "amount": -7500, "country": "Netherlands", "merchant": "Dutch Decor Rentals", "description": "Event supplies"}, {"date": "2024-02-18", "type": "outgoing", "amount": -210, "country": "Netherlands", "merchant": "Restaurant Vermeer", "description": "Restaurant dinner"}, {"date": "2024-02-22", "type": "incoming", "amount": 60000, "country": "Switzerland", "merchant": "Geneva Luxury Weddings", "description": "Event planning fee"}, {"date": "2024-02-23", "type": "outgoing", "amount": -55000, "country": "United States", "merchant": "Kraken", "description": "Transfer to Kraken"}, {"date": "2024-02-28", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "CZ Zorgverzekering", "description": "Health insurance"}, {"date": "2024-03-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "Amsterdam Real Estate", "description": "Rent payment"}, {"date": "2024-03-05", "type": "outgoing", "amount": -280, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-03-10", "type": "incoming", "amount": 48000, "country": "United States", "merchant": "Coinbase", "description": "Transfer from Coinbase"}, {"date": "2024-03-11", "type": "outgoing", "amount": -45000, "country": "Italy", "merchant": "Milan Audio Visual Services", "description": "Vendor payment"}, {"date": "2024-03-15", "type": "outgoing", "amount": -9000, "country": "Netherlands", "merchant": "Amsterdam Event Tech", "description": "Event supplies"}, {"date": "2024-03-18", "type": "outgoing", "amount": -190, "country": "Netherlands", "merchant": "Cafe de Pijp", "description": "Restaurant dinner"}, {"date": "2024-03-22", "type": "incoming", "amount": 70000, "country": "United Arab Emirates", "merchant": "Dubai Corporate Events", "description": "Event planning fee"}, {"date": "2024-03-23", "type": "outgoing", "amount": -65000, "country": "Malta", "merchant": "Binance", "description": "Transfer to Binance"}, {"date": "2024-03-28", "type": "outgoing", "amount": -80, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-04-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "Amsterdam Real Estate", "description": "Rent payment"}, {"date": "2024-04-05", "type": "outgoing", "amount": -240, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-04-10", "type": "incoming", "amount": 52000, "country": "United States", "merchant": "Kraken", "description": "Transfer from Kraken"}, {"date": "2024-04-11", "type": "outgoing", "amount": -48000, "country": "Spain", "merchant": "Barcelona Event Staffing", "description": "Vendor payment"}, {"date": "2024-04-15", "type": "outgoing", "amount": -8200, "country": "Netherlands", "merchant": "Dutch Decor Rentals", "description": "Event supplies"}, {"date": "2024-04-18", "type": "outgoing", "amount": -220, "country": "Netherlands", "merchant": "Restaurant Jansz", "description": "Restaurant dinner"}, {"date": "2024-04-22", "type": "incoming", "amount": 65000, "country": "France", "merchant": "Cannes Film Festival", "description": "Event planning fee"}, {"date": "2024-04-23", "type": "outgoing", "amount": -60000, "country": "United States", "merchant": "Coinbase", "description": "Transfer to Coinbase"}, {"date": "2024-04-28", "type": "outgoing", "amount": -80, "country": "Netherlands", "merchant": "Fit For Free", "description": "Gym membership"}, {"date": "2024-05-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "Amsterdam Real Estate", "description": "Rent payment"}, {"date": "2024-05-05", "type": "outgoing", "amount": -260, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-05-10", "type": "incoming", "amount": 58000, "country": "Malta", "merchant": "Binance", "description": "Transfer from Binance"}, {"date": "2024-05-11", "type": "outgoing", "amount": -54000, "country": "United Kingdom", "merchant": "London Luxury Venues", "description": "Vendor payment"}, {"date": "2024-05-15", "type": "outgoing", "amount": -9500, "country": "Netherlands", "merchant": "Amsterdam Event Tech", "description": "Event supplies"}, {"date": "2024-05-18", "type": "outgoing", "amount": -230, "country": "Netherlands", "merchant": "Restaurant Bougainville", "description": "Restaurant dinner"}, {"date": "2024-05-22", "type": "incoming", "amount": 75000, "country": "Germany", "merchant": "Munich Tech Summit", "description": "Event planning fee"}, {"date": "2024-05-23", "type": "outgoing", "amount": -70000, "country": "United States", "merchant": "Kraken", "description": "Transfer to Kraken"}, {"date": "2024-05-28", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "CZ Zorgverzekering", "description": "Health insurance"}, {"date": "2024-06-01", "type": "outgoing", "amount": -2500, "country": "Netherlands", "merchant": "Amsterdam Real Estate", "description": "Rent payment"}, {"date": "2024-06-05", "type": "outgoing", "amount": -270, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-06-10", "type": "incoming", "amount": 62000, "country": "United States", "merchant": "Coinbase", "description": "Transfer from Coinbase"}, {"date": "2024-06-11", "type": "outgoing", "amount": -58000, "country": "Italy", "merchant": "Rome Luxury Catering", "description": "Vendor payment"}, {"date": "2024-06-15", "type": "outgoing", "amount": -8800, "country": "Netherlands", "merchant": "Event Essentials BV", "description": "Event supplies"}, {"date": "2024-06-18", "type": "outgoing", "amount": -240, "country": "Netherlands", "merchant": "Restaurant Ciel Bleu", "description": "Restaurant dinner"}, {"date": "2024-06-22", "type": "incoming", "amount": 80000, "country": "Sweden", "merchant": "Stockholm Fashion Week", "description": "Event planning fee"}, {"date": "2024-06-23", "type": "outgoing", "amount": -75000, "country": "Malta", "merchant": "Binance", "description": "Transfer to Binance"}, {"date": "2024-06-28", "type": "outgoing", "amount": -85, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-06-30", "type": "incoming", "amount": 70000, "country": "Japan", "merchant": "Tokyo Business Expo", "description": "Event planning fee"}], "financialProfile": {"monthlyIncome": 15000, "savingsBalance": 120000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 350000}}, "suspiciousActivity": {"types": ["fast-in-fast-out"], "timing": ["Throughout January to June 2024"], "amounts": [45000, 55000, 60000, 70000, 65000, 75000, 80000], "pattern": "fast-in-fast-out", "frequencies": [12]}}	2
22	 GenerateKYCTestScenario( "showAuxiliaryData": "true", "decisionOutcome": "escalate", "difficultyLevel": "easy", "accountType": "retail", "suspiciousPattern": "fast-in-fast-out") 	TM	3	16	{"context": "Jeroen de Vries, a 32-year-old software developer, has shown a clear pattern of 'fast-in-fast-out' transactions over a three-month period. Large amounts are transferred into his account from cryptocurrency exchanges, followed almost immediately by transfers of similar amounts to online gambling sites. This pattern occurs approximately twice a month and involves sums that are significantly larger than his regular salary. The rapid movement of funds between crypto exchanges and gambling sites, combined with the amounts involved, raises concerns about potential money laundering or other illicit activities.", "persona": {"age": 32, "name": "Jeroen de Vries", "background": "Jeroen is a software developer working for a small tech startup in Amsterdam. He has recently shown an increased interest in cryptocurrency trading and online gambling. Jeroen has no prior history of suspicious activities and has been a customer of the bank for 5 years.", "occupation": "Software Developer", "familyStatus": "Single", "previouslyFlagged": false}, "auxiliaryData": {"housing": 1200, "healthcare": 100, "dailyExpenses": 50, "entertainment": 300, "transportation": 150, "savingsInvestments": 500, "internationalTransfers": 7500, "cashWithdrawalsDeposits": 200}, "analystDecision": {"action": "escalate", "keyFactors": ["Repeated pattern of large incoming transfers from cryptocurrency exchanges", "Quick outgoing transfers to online gambling sites following crypto deposits", "Transaction amounts significantly exceed the client's regular income", "Frequency of these transactions (about twice a month) suggests a consistent pattern", "Use of multiple cryptocurrency exchanges and gambling sites may indicate attempts to obscure the money trail"]}, "difficultyLevel": {"level": "easy", "score": 3}, "transactionData": [{"date": "2024-01-05", "type": "incoming", "amount": 4500, "country": "Netherlands", "merchant": "TechSpark B.V.", "description": "Salary deposit"}, {"date": "2024-01-07", "type": "outgoing", "amount": -120, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-01-10", "type": "incoming", "amount": 8000, "country": "Malta", "merchant": "Binance", "description": "Online transfer from Binance"}, {"date": "2024-01-11", "type": "outgoing", "amount": -7500, "country": "Malta", "merchant": "LuckyPlay Casino", "description": "Transfer to online gambling site"}, {"date": "2024-01-15", "type": "outgoing", "amount": -85, "country": "Netherlands", "merchant": "Pizzeria Italia", "description": "Restaurant dinner"}, {"date": "2024-01-20", "type": "outgoing", "amount": -50, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-01-25", "type": "incoming", "amount": 6500, "country": "United States", "merchant": "Kraken", "description": "Online transfer from Kraken"}, {"date": "2024-01-26", "type": "outgoing", "amount": -6000, "country": "Gibraltar", "merchant": "BetSmart", "description": "Transfer to online gambling site"}, {"date": "2024-01-30", "type": "outgoing", "amount": -40, "country": "Netherlands", "merchant": "BasicFit", "description": "Gym membership"}, {"date": "2024-02-05", "type": "incoming", "amount": 4500, "country": "Netherlands", "merchant": "TechSpark B.V.", "description": "Salary deposit"}, {"date": "2024-02-08", "type": "outgoing", "amount": -140, "country": "Netherlands", "merchant": "Jumbo", "description": "Grocery shopping"}, {"date": "2024-02-12", "type": "incoming", "amount": 9000, "country": "United States", "merchant": "Coinbase", "description": "Online transfer from Coinbase"}, {"date": "2024-02-13", "type": "outgoing", "amount": -8500, "country": "Malta", "merchant": "LuckyPlay Casino", "description": "Transfer to online gambling site"}, {"date": "2024-02-18", "type": "outgoing", "amount": -70, "country": "Netherlands", "merchant": "Burger King", "description": "Restaurant dinner"}, {"date": "2024-02-22", "type": "outgoing", "amount": -150, "country": "Netherlands", "merchant": "Bol.com", "description": "Online shopping"}, {"date": "2024-02-26", "type": "incoming", "amount": 7500, "country": "Malta", "merchant": "Binance", "description": "Online transfer from Binance"}, {"date": "2024-02-27", "type": "outgoing", "amount": -7000, "country": "Gibraltar", "merchant": "BetSmart", "description": "Transfer to online gambling site"}, {"date": "2024-03-05", "type": "incoming", "amount": 4500, "country": "Netherlands", "merchant": "TechSpark B.V.", "description": "Salary deposit"}, {"date": "2024-03-08", "type": "outgoing", "amount": -130, "country": "Netherlands", "merchant": "Albert Heijn", "description": "Grocery shopping"}, {"date": "2024-03-12", "type": "incoming", "amount": 8500, "country": "United States", "merchant": "Kraken", "description": "Online transfer from Kraken"}, {"date": "2024-03-13", "type": "outgoing", "amount": -8000, "country": "Malta", "merchant": "LuckyPlay Casino", "description": "Transfer to online gambling site"}, {"date": "2024-03-18", "type": "outgoing", "amount": -90, "country": "Netherlands", "merchant": "Sushi Time", "description": "Restaurant dinner"}, {"date": "2024-03-22", "type": "outgoing", "amount": -50, "country": "Netherlands", "merchant": "KPN", "description": "Mobile phone bill"}, {"date": "2024-03-26", "type": "incoming", "amount": 7000, "country": "United States", "merchant": "Coinbase", "description": "Online transfer from Coinbase"}, {"date": "2024-03-27", "type": "outgoing", "amount": -6500, "country": "Gibraltar", "merchant": "BetSmart", "description": "Transfer to online gambling site"}, {"date": "2024-03-30", "type": "outgoing", "amount": -40, "country": "Netherlands", "merchant": "BasicFit", "description": "Gym membership"}], "financialProfile": {"monthlyIncome": 4500, "savingsBalance": 15000, "investmentPortfolio": {"hasInvestments": true, "investmentAmount": 10000}}, "suspiciousActivity": {"types": ["fast-in-fast-out"], "timing": ["Throughout January to March 2024"], "amounts": [8000, 6500, 9000, 7500, 8500, 7000], "pattern": "fast-in-fast-out", "frequencies": [6]}}	2
\.


--
-- Data for Name: user_answers; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.user_answers (id, user_id, use_case_id, question_id, option_id, is_correct, created_at, lesson_id) FROM stdin;
463	16	1	1	3	t	2024-06-30 20:27:54.739398	1
464	16	1	1	1	f	2024-07-05 10:09:21.380962	1
465	16	2	2	6	f	2024-07-05 10:09:23.955489	1
466	16	3	3	28	f	2024-07-05 10:09:25.640822	1
467	16	10	6	17	t	2024-07-05 10:09:27.241041	1
468	16	1	1	1	f	2024-07-05 10:09:34.996215	1
469	16	2	2	5	f	2024-07-05 10:09:36.765782	1
393	6	1	1	1	f	2024-06-18 20:06:45.23962	1
394	6	1	1	4	f	2024-06-18 20:14:50.502341	1
395	6	2	2	5	f	2024-06-18 20:15:56.113692	1
396	6	1	1	1	f	2024-06-18 20:30:02.462822	1
397	6	2	2	8	f	2024-06-18 20:30:13.27089	1
17	3	2	2	5	f	2024-03-09 14:02:31.903551	1
18	3	1	1	3	t	2024-03-09 14:02:31.903551	1
19	3	1	1	1	f	2024-03-09 14:02:31.903551	1
20	3	1	1	4	f	2024-03-09 14:02:31.903551	1
21	3	1	1	4	f	2024-03-09 14:02:31.903551	1
22	3	1	1	3	t	2024-03-09 14:02:31.903551	1
23	3	1	1	3	t	2024-03-09 14:02:31.903551	1
24	3	1	1	1	f	2024-03-09 14:02:31.903551	1
25	3	1	1	4	f	2024-03-09 14:02:31.903551	1
26	3	1	1	4	f	2024-03-09 14:02:31.903551	1
27	3	1	1	3	t	2024-03-09 14:02:31.903551	1
28	3	1	1	3	t	2024-03-09 14:02:31.903551	1
29	3	1	1	4	f	2024-03-09 14:02:31.903551	1
30	3	1	1	3	t	2024-03-09 14:02:31.903551	1
31	3	1	1	4	f	2024-03-09 14:02:31.903551	1
32	3	1	1	4	f	2024-03-09 14:02:31.903551	1
33	3	1	1	1	f	2024-03-09 14:02:31.903551	1
34	3	1	1	4	f	2024-03-09 14:02:31.903551	1
35	3	1	1	2	f	2024-03-09 14:02:31.903551	1
36	3	1	1	4	f	2024-03-09 14:02:31.903551	1
37	3	1	1	1	f	2024-03-09 14:02:31.903551	1
38	3	1	1	1	f	2024-03-09 14:02:31.903551	1
39	3	1	1	3	t	2024-03-09 14:02:31.903551	1
40	3	1	1	3	t	2024-03-09 14:02:31.903551	1
41	3	1	1	1	f	2024-03-09 14:02:31.903551	1
42	3	1	1	2	f	2024-03-09 14:02:31.903551	1
43	3	1	1	1	f	2024-03-09 14:02:31.903551	1
44	3	1	1	3	t	2024-03-09 14:02:31.903551	1
46	3	1	1	2	f	2024-03-09 14:02:31.903551	1
47	3	1	1	3	t	2024-03-09 14:02:31.903551	1
48	3	1	1	4	f	2024-03-09 14:02:31.903551	1
49	3	1	1	1	f	2024-03-09 14:02:31.903551	1
50	3	1	1	1	f	2024-03-09 14:02:31.903551	1
51	3	1	1	4	f	2024-03-09 14:02:31.903551	1
52	3	1	1	3	t	2024-03-09 14:02:31.903551	1
53	3	1	1	4	f	2024-03-09 14:02:31.903551	1
54	3	1	1	4	f	2024-03-09 14:02:31.903551	1
55	3	1	1	4	f	2024-03-09 14:02:31.903551	1
56	3	1	1	4	f	2024-03-09 14:02:31.903551	1
59	3	1	1	1	f	2024-03-09 14:02:31.903551	1
60	3	1	1	4	f	2024-03-09 14:02:31.903551	1
61	3	1	1	4	f	2024-03-09 14:02:31.903551	1
63	3	1	1	3	t	2024-03-09 14:02:31.903551	1
64	3	1	1	2	f	2024-03-09 14:02:31.903551	1
65	3	1	1	2	f	2024-03-09 14:02:31.903551	1
66	3	2	2	7	t	2024-03-09 14:02:31.903551	1
67	3	1	1	1	f	2024-03-09 14:02:31.903551	1
68	3	2	2	5	f	2024-03-09 14:02:31.903551	1
69	3	3	3	18	f	2024-03-09 14:02:31.903551	1
70	3	9	5	10	f	2024-03-09 14:02:31.903551	1
71	3	10	6	15	f	2024-03-09 14:02:31.903551	1
72	3	1	1	3	t	2024-03-09 14:02:31.903551	1
73	3	2	2	7	t	2024-03-09 14:02:31.903551	1
74	3	3	3	19	t	2024-03-09 14:02:31.903551	1
75	3	9	5	12	f	2024-03-09 14:02:31.903551	1
76	3	10	6	16	f	2024-03-09 14:02:31.903551	1
77	3	1	1	2	f	2024-03-09 14:02:31.903551	1
78	3	1	1	1	f	2024-03-09 14:02:31.903551	1
79	3	2	2	8	f	2024-03-09 14:02:31.903551	1
80	3	3	3	19	t	2024-03-09 14:02:31.903551	1
81	3	1	1	2	f	2024-03-09 14:02:31.903551	1
82	3	1	1	3	t	2024-03-09 14:02:31.903551	1
83	3	2	2	8	f	2024-03-09 14:02:31.903551	1
84	3	3	3	19	t	2024-03-09 14:02:31.903551	1
85	3	1	1	4	f	2024-03-09 14:02:31.903551	1
86	3	1	1	1	f	2024-03-09 14:02:31.903551	1
87	3	2	2	7	t	2024-03-09 14:02:31.903551	1
88	3	1	1	3	t	2024-03-09 14:02:31.903551	1
89	3	1	1	4	f	2024-03-09 14:02:31.903551	1
90	3	1	1	4	f	2024-03-09 14:02:31.903551	1
91	3	1	1	4	f	2024-03-13 14:04:48.395522	1
92	3	2	2	7	t	2024-03-13 14:04:54.645099	1
93	3	3	3	19	t	2024-03-13 14:04:58.707446	1
94	3	9	5	11	f	2024-03-13 14:05:00.705763	1
95	3	10	6	16	f	2024-03-13 14:05:02.409618	1
96	3	1	1	4	f	2024-03-13 14:09:15.060977	1
97	3	2	2	6	f	2024-03-13 14:09:18.741901	1
98	3	1	1	4	f	2024-03-13 14:11:30.58763	1
99	3	1	1	1	f	2024-03-13 14:12:29.399558	1
100	3	2	2	8	f	2024-03-13 14:12:52.42004	1
101	3	1	1	3	t	2024-03-13 14:21:20.839896	1
102	3	2	2	7	t	2024-03-13 14:21:22.573421	1
103	3	3	3	19	t	2024-03-13 14:21:24.599543	1
104	3	9	5	10	f	2024-03-13 14:21:26.158175	1
105	3	10	6	17	t	2024-03-13 14:21:28.47597	1
106	3	11	7	20	f	2024-03-13 14:21:30.171	1
107	3	12	8	27	f	2024-03-13 14:21:31.618186	1
398	6	1	1	1	f	2024-06-19 19:06:43.699129	1
399	6	1	1	1	f	2024-06-19 19:08:03.981434	1
400	6	1	1	3	t	2024-06-19 19:08:15.082013	1
401	6	2	2	7	t	2024-06-19 19:08:34.379625	1
45	1	1	1	3	t	2024-03-09 14:02:31.903551	1
451	16	1	1	1	f	2024-06-30 14:25:15.692806	1
452	16	2	2	6	f	2024-06-30 14:25:20.278691	1
453	16	3	3	29	f	2024-06-30 14:25:23.041247	1
454	16	9	5	13	t	2024-06-30 14:25:25.523966	1
455	16	10	6	16	f	2024-06-30 14:25:28.075631	1
456	16	11	7	21	t	2024-06-30 14:25:29.960804	1
457	16	12	8	26	f	2024-06-30 14:25:31.953715	1
458	16	1	1	2	f	2024-06-30 14:25:34.117399	1
459	16	2	2	8	f	2024-06-30 14:25:35.955296	1
460	16	3	3	28	f	2024-06-30 14:25:38.133844	1
461	16	10	6	15	f	2024-06-30 14:25:40.183702	1
462	16	12	8	24	t	2024-06-30 14:25:42.015408	1
\.


--
-- Data for Name: user_lesson_interactions; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.user_lesson_interactions (id, user_id, lesson_id, completed, completion_date, score, last_accessed) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.users (id, email, hashed_password, use_case_difficulty, score, is_admin, lesson_id, first_name, last_name, created_at, updated_at) FROM stdin;
10	john.dodasdade@example.com	scrypt:32768:8:1$yLLKGDWjxlsJAMPd$be979143eb749a47076c2455d27f5dc9af54a43781424c3c5a02a9e5f26ac991f5b108cf90c34c6fdce0a9efcf850b89c6771e71b0019bba1d10dbb270bb6792	\N	\N	t	\N	john	rika	2024-06-23 22:12:49.95752	2024-06-23 22:12:49.957527
11	erik@gmail.com	scrypt:32768:8:1$fjJZTyJq8jjMqBrr$fd1c9827ceaa65fc762271d388ecff0ccfff74cbfd56ed117a05730c8a0c0e22e83903ee4e2d3704870f0018362a82bffb2a9c09ab05efd924318fad6e2bb941	\N	\N	f	\N	ckemi	lale	2024-06-23 22:15:06.702473	2024-06-23 22:15:06.702479
12	un@gmail.com	scrypt:32768:8:1$kX9SqNUmv4MbO53F$ce36da45648753ea1a492204cf9a8709865ced99dce5b3095ea382f355a443599e2c20e4040cd91aac8993b9b627ed5b45624711752f91d305f399e7d22e5058	\N	\N	f	\N	ome	lali	2024-06-23 22:16:42.390669	2024-06-23 22:16:42.390674
13	admasd@gmail.comad	scrypt:32768:8:1$kizOSk2i7f7xUQGA$1d27a08b25cda270512a9d62b61f85bdc3d11e674082db753bc24da6849d01b4cc7e93d20fbb044ad9c3b2c20318456c175d153b9ab3bbdfba7c79d27442da26	\N	\N	f	\N	adkoasjdoad	kpasdkpsa	2024-06-23 22:17:10.266917	2024-06-23 22:17:10.266921
14	adadqwd@gmail.comad	scrypt:32768:8:1$IFQMcGgEYOdk8xwE$1de80315facdef1a439927da04c07299ae92747541e7981504d8eab8113e4b29cac063c456a6e5cd1463d1c7c80c90e362ade96d78f7ca2b215a75b1a6cd49f7	\N	\N	f	\N	lalu	kpqwwwwasdkpsa	2024-06-23 22:18:42.999216	2024-06-23 22:18:42.999225
15	rika@gmail.comad	scrypt:32768:8:1$snRNxUYD2DPRTJ5u$2ba99e4d8f91e361624c9c22f57cca8a4343d48b468d9fb5826f530828fba7b8abac87f408abd37acfaf436103b3c9b7296c690aa6c4955f298aaf7a2838e42b	\N	\N	f	\N	Une	jam	2024-06-24 00:25:18.809023	2024-06-24 00:25:18.809028
16	omelale@gmail.com	scrypt:32768:8:1$h9rer1yKTqVq3wmi$d4de76056811431e64bed0f233057c8d2633c7006285d65cd2b2b587ee9cccd25bf576078cfa28890cc5200b8c45261d5d434e2d2173fdac44ba78e9cbff6561	\N	\N	t	\N	Amarda	Amarda	2024-06-25 23:05:51.863156	2024-06-25 23:05:51.863161
1	lucavehbiu96@gmail.com	scrypt:32768:8:1$ELcHhcrtvUvxrZ69$2736ccc3a4222a6ed38cc2ce10b4e60dabf29b03a1b53b4c393657c95e63f6e831a32b3ce8c2bad0ee8753559302973b6c0cb79ce1755720ffd4e587ef7b1a77	\N	\N	f	\N	Luca	Vehbiu	2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
2	bgjoleka@gmail.com	scrypt:32768:8:1$ysYoOKSsrxIt4jn8$7d22dce86fa34252db91f1070239b21f171c49c1374877dede3a9b7db54970990968f586f22b8de54bfcbea394d2e35572903719fbcd3aba06f01e03d834344f	\N	\N	f	\N	Bojken	Gjoleka	2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
3	lucavehbiu96+test1@gmail.com	scrypt:32768:8:1$S4AWfoCEW1pKVh99$cadae8c040bf8fa886066d7ef32cea72920558f57c043865e472226bc43dfd3825521ae57ac8769c707daef45b5c5583f12b5d7758fd7411393ee3c9e5441e7e	\N	\N	f	\N	Mandi	Nishtulles	2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
4	Rikes@gmail.com	scrypt:32768:8:1$u5XFrZbiWBiTLqbG$716f00c84b55d74f82469d4d2c284c91246bb53fc4c73cc4f2907d58fcc1ec67187d447f76a457fbbb1ac246eff57a31e6bf38dc73c614d7aea9a5c66290ab38	\N	\N	f	\N	Llahu		2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
5	lucavehbiu96+test2@gmail.com	scrypt:32768:8:1$97fe7W6jWVvmT31V$2ed4774fc11a8e6169679271e60356243914a635823ed98eb64bc4bf42a93ef857ea9e907c1676f9db9eea6efdbf9f1296d8d182096b488965e9d88030217ded	\N	\N	f	\N	Tafil	Hafizi	2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
6	lucavehbiu96+test3@gmail.com	scrypt:32768:8:1$S4AWfoCEW1pKVh99$cadae8c040bf8fa886066d7ef32cea72920558f57c043865e472226bc43dfd3825521ae57ac8769c707daef45b5c5583f12b5d7758fd7411393ee3c9e5441e7e	\N	\N	t	1	Noed	Dutch	2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
7	john.doe@example.com	scrypt:32768:8:1$np6AmRdP7L1zshv7$62a3215e81061338e4b1f1a2be2541ac08882855fb2d0bf546fdf681daba87e7136198735cc8876997ee40d4b23500885adb0cf7029bc655004d2b1a84f67e81	\N	\N	t	\N	john_doe		2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
8		scrypt:32768:8:1$nFRg2l9bmWwT4SGi$3cefa83642510aa818e37438be9f4598af919230fd3eab5d08975ca76dc053f589b1496bff4213d69dfa8fd22b1a3d706dc49c347c60933756155b704b7f717b	\N	\N	f	\N	\N	\N	2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
9	dasdad.doe@example.com	scrypt:32768:8:1$kw9JadO750MxY3pr$aaac5ba291e810f85d9ccdc14de81d63a1a439e5e039ffa327c70f7b002feaaa2add4f250e1feca26d1be23935ffc4c02342b42668a41b64f23bf71bd840f147	\N	\N	t	\N	dasd		2024-06-24 00:12:31.288034	2024-06-24 00:12:34.902488
\.


--
-- Name: difficulty_level_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.difficulty_level_id_seq', 4, true);


--
-- Name: learning_paths_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.learning_paths_id_seq', 1, false);


--
-- Name: lessons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.lessons_id_seq', 1, false);


--
-- Name: news_articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.news_articles_id_seq', 8, true);


--
-- Name: options_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.options_id_seq', 17, true);


--
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.questions_id_seq', 6, true);


--
-- Name: risk_factor_matrix_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.risk_factor_matrix_id_seq', 1, false);


--
-- Name: use_cases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.use_cases_id_seq', 22, true);


--
-- Name: user_answers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.user_answers_id_seq', 469, true);


--
-- Name: user_lesson_interactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.user_lesson_interactions_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.users_id_seq', 16, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: difficulty_level difficulty_level_level_key; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.difficulty_level
    ADD CONSTRAINT difficulty_level_level_key UNIQUE (level);


--
-- Name: difficulty_level difficulty_level_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.difficulty_level
    ADD CONSTRAINT difficulty_level_pkey PRIMARY KEY (id);


--
-- Name: learning_paths learning_paths_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.learning_paths
    ADD CONSTRAINT learning_paths_pkey PRIMARY KEY (id);


--
-- Name: lessons lessons_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT lessons_pkey PRIMARY KEY (id);


--
-- Name: news_articles news_articles_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.news_articles
    ADD CONSTRAINT news_articles_pkey PRIMARY KEY (id);


--
-- Name: options options_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.options
    ADD CONSTRAINT options_pkey PRIMARY KEY (id);


--
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- Name: risk_factor_matrix risk_factor_matrix_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.risk_factor_matrix
    ADD CONSTRAINT risk_factor_matrix_pkey PRIMARY KEY (id);


--
-- Name: use_cases use_cases_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.use_cases
    ADD CONSTRAINT use_cases_pkey PRIMARY KEY (id);


--
-- Name: user_answers user_answers_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_pkey PRIMARY KEY (id);


--
-- Name: user_lesson_interactions user_lesson_interactions_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_lesson_interactions
    ADD CONSTRAINT user_lesson_interactions_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: use_cases fk_created_by_user; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.use_cases
    ADD CONSTRAINT fk_created_by_user FOREIGN KEY (created_by_user) REFERENCES public.users(id);


--
-- Name: use_cases fk_difficulty; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.use_cases
    ADD CONSTRAINT fk_difficulty FOREIGN KEY (difficulty_id) REFERENCES public.difficulty_level(id);


--
-- Name: user_answers fk_lesson; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT fk_lesson FOREIGN KEY (lesson_id) REFERENCES public.difficulty_level(id);


--
-- Name: news_articles fk_use_case; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.news_articles
    ADD CONSTRAINT fk_use_case FOREIGN KEY (use_case_id) REFERENCES public.use_cases(id) ON DELETE CASCADE;


--
-- Name: options options_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.options
    ADD CONSTRAINT options_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(id) ON DELETE CASCADE;


--
-- Name: questions questions_use_case_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_use_case_id_fkey FOREIGN KEY (use_case_id) REFERENCES public.use_cases(id) ON DELETE CASCADE;


--
-- Name: risk_factor_matrix risk_factor_matrix_use_case_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.risk_factor_matrix
    ADD CONSTRAINT risk_factor_matrix_use_case_id_fkey FOREIGN KEY (use_case_id) REFERENCES public.use_cases(id) ON DELETE CASCADE;


--
-- Name: user_answers user_answers_option_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_option_id_fkey FOREIGN KEY (option_id) REFERENCES public.options(id) ON DELETE CASCADE;


--
-- Name: user_answers user_answers_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.questions(id) ON DELETE CASCADE;


--
-- Name: user_answers user_answers_use_case_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_use_case_id_fkey FOREIGN KEY (use_case_id) REFERENCES public.use_cases(id) ON DELETE CASCADE;


--
-- Name: user_answers user_answers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_answers
    ADD CONSTRAINT user_answers_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: user_lesson_interactions user_lesson_interactions_lesson_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_lesson_interactions
    ADD CONSTRAINT user_lesson_interactions_lesson_id_fkey FOREIGN KEY (lesson_id) REFERENCES public.lessons(id);


--
-- Name: user_lesson_interactions user_lesson_interactions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.user_lesson_interactions
    ADD CONSTRAINT user_lesson_interactions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: data_admin
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

