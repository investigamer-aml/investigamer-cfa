--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5 (Homebrew)
-- Dumped by pg_dump version 15.5 (Homebrew)

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
-- Name: lesson; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.lesson (
    id integer NOT NULL,
    title character varying NOT NULL
);


ALTER TABLE public.lesson OWNER TO data_admin;

--
-- Name: lesson_id_seq; Type: SEQUENCE; Schema: public; Owner: data_admin
--

CREATE SEQUENCE public.lesson_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lesson_id_seq OWNER TO data_admin;

--
-- Name: lesson_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: data_admin
--

ALTER SEQUENCE public.lesson_id_seq OWNED BY public.lesson.id;


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
    difficulty text,
    multiple_risks boolean,
    correct_answer text,
    final_decision text,
    risk_factor_matrix_id integer,
    lesson_id integer,
    created_by_user integer
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
    is_correct boolean
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
-- Name: users; Type: TABLE; Schema: public; Owner: data_admin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255),
    email character varying(255),
    hashed_password character varying(255),
    use_case_difficulty character varying,
    score double precision,
    is_admin boolean DEFAULT false NOT NULL
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
-- Name: lesson id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.lesson ALTER COLUMN id SET DEFAULT nextval('public.lesson_id_seq'::regclass);


--
-- Name: lessons id; Type: DEFAULT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.lessons ALTER COLUMN id SET DEFAULT nextval('public.lessons_id_seq'::regclass);


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
-- Data for Name: lesson; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.lesson (id, title) FROM stdin;
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
10	5	dickhead	f
11	5	dick	f
12	5	head	f
13	5	pussy	t
14	6	fuck	f
15	6	no	f
16	6	maybe	f
17	6	let's go	t
\.


--
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.questions (id, use_case_id, text) FROM stdin;
1	1	What is the biggest KYC risk?
2	2	What is the geography Risk in this use case?
5	9	Who are you?
6	10	What do you mean?
\.


--
-- Data for Name: risk_factor_matrix; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.risk_factor_matrix (id, factor, score, use_case_id) FROM stdin;
\.


--
-- Data for Name: use_cases; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.use_cases (id, description, type, difficulty, multiple_risks, correct_answer, final_decision, risk_factor_matrix_id, lesson_id, created_by_user) FROM stdin;
2	    <h2>Compliance Due Diligence (CDD) Analysis Report</h2>\n    <p>\n        As a Compliance Due Diligence (CDD) analyst, you are tasked with reviewing the client profile of LMN International, a Wholesale Banking client. LMN International is a conglomerate with diverse business interests in multiple industries. They operate in various jurisdictions across Europe, the Middle East, and Asia.\n    </p>\n\n    <h3>Ultimate Beneficial Owner (UBO) Information:</h3>\n    <p>\n        The UBO of LMN International is Mark Lee, a citizen of Country Z, which has been flagged as a high-risk jurisdiction for financial crime and corruption. Mark Lee has previously been associated with companies involved in regulatory violations and financial irregularities.\n    </p>\n\n    <h3>Ownership Structure:</h3>\n    <p>\n        LMN International's ownership structure involves multiple layers of holding companies and offshore entities located in jurisdictions known for lax regulatory oversight and secrecy.\n    </p>\n\n    <h3>Business Operations:</h3>\n    <p>\n        LMN International operates in sectors such as real estate development, hospitality, and luxury retail.\n    </p>\n\n    <h3>Compliance and Transparency:</h3>\n    <p>\n        LMN International has demonstrated a commitment to regulatory compliance, with robust internal controls and regular audits conducted by reputable firms. Analysis of transactional data reveals transparent and well-documented transactions with reputable counterparties.\n    </p>\n	KYC	Easy	t	They operate in various jurisdictions across Europe, the Middle East, and Asia.	Ignore	2	1	\N
1	    <h2>Compliance Due Diligence (CDD) Analysis Report</h2>\n    <p>\n        As a Compliance Due Diligence (CDD) analyst, your new task is to scrutinize the client profile of XYZ Global, a Corporate Banking client. XYZ Global is a multifaceted corporation with operations in diverse sectors across North America, Africa, and Southeast Asia.\n    </p>\n\n    <h3>Client Profile Examination:</h3>\n    <p>\n        During your examination of XYZ Global's client profile, you encounter the following details:\n    </p>\n\n    <h4>Ultimate Beneficial Owner (UBO):</h4>\n    <p>\n        The Ultimate Beneficial Owner (UBO) of XYZ Global is Sarah Chen, a national of Country X, which is recognized as a medium-risk jurisdiction concerning financial crime and sanctions evasion. Sarah Chen has been linked to businesses that faced scrutiny for potential ethical lapses and minor compliance issues, but no significant legal actions have been taken against her.\n    </p>\n\n    <h4>Ownership Structure:</h4>\n    <p>\n        XYZ Global's ownership structure is complex, featuring several layers of subsidiaries and special purpose vehicles (SPVs) domiciled in jurisdictions that are frequently criticized for their lack of transparency and weak enforcement of anti-money laundering (AML) regulations.\n    </p>\n\n    <h4>Areas of Operation:</h4>\n    <p>\n        The company's areas of operation include technology development, green energy projects, and international trade.\n    </p>\n\n    <h4>Compliance and Audits:</h4>\n    <p>\n        Despite the complex ownership structure, XYZ Global has made efforts to maintain a clean compliance record. They have implemented comprehensive compliance policies, including enhanced due diligence (EDD) processes, and undergo regular audits by well-known audit firms.\n    </p>\n\n    <h4>Financial Transaction Analysis:</h4>\n    <p>\n        The analysis of XYZ Global's financial transactions shows consistent, transparent dealings with well-established and reputable business partners, indicating no immediate red flags related to their financial practices.\n    </p>	KYC	Easy	t	Real estate development, hospitality, and luxury retail.	Escalate	1	1	\N
3	case 3 baby help meeeeee <br><br> wow what a case	KYC	Easy	t	Fuck me I have no idea, please don't fire me	In doubt	3	1	6
9	amazing use case baby	KYC	\N	\N	\N	\N	\N	\N	6
10	take me back to ROma 99	AML	\N	\N	\N	\N	\N	\N	6
\.


--
-- Data for Name: user_answers; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.user_answers (id, user_id, use_case_id, question_id, option_id, is_correct) FROM stdin;
1	1	2	2	5	f
2	1	2	2	6	f
3	1	2	2	7	t
4	1	2	2	7	t
5	1	2	2	6	f
6	1	2	2	7	t
7	1	2	2	6	f
8	1	2	2	7	t
9	1	2	2	6	f
10	1	2	2	7	t
11	1	2	2	7	t
12	1	2	2	8	f
13	1	2	2	6	f
14	1	2	2	7	t
15	1	2	2	7	t
16	1	2	2	6	f
17	3	2	2	5	f
18	3	1	1	3	t
19	3	1	1	1	f
20	3	1	1	4	f
21	3	1	1	4	f
22	3	1	1	3	t
23	3	1	1	3	t
24	3	1	1	1	f
25	3	1	1	4	f
26	3	1	1	4	f
27	3	1	1	3	t
28	3	1	1	3	t
29	3	1	1	4	f
30	3	1	1	3	t
31	3	1	1	4	f
32	3	1	1	4	f
33	3	1	1	1	f
34	3	1	1	4	f
35	3	1	1	2	f
36	3	1	1	4	f
37	3	1	1	1	f
38	3	1	1	1	f
39	3	1	1	3	t
40	3	1	1	3	t
41	3	1	1	1	f
42	3	1	1	2	f
43	3	1	1	1	f
44	3	1	1	3	t
45	3	1	1	3	t
46	3	1	1	2	f
47	3	1	1	3	t
48	3	1	1	4	f
49	3	1	1	1	f
50	3	1	1	1	f
51	3	1	1	4	f
52	3	1	1	3	t
53	3	1	1	4	f
54	3	1	1	4	f
55	3	1	1	4	f
56	3	1	1	4	f
57	1	1	1	4	f
58	1	1	1	4	f
59	3	1	1	1	f
60	3	1	1	4	f
61	3	1	1	4	f
62	1	1	1	3	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: data_admin
--

COPY public.users (id, username, email, hashed_password, use_case_difficulty, score, is_admin) FROM stdin;
1	Luca Vehbiu	lucavehbiu96@gmail.com	scrypt:32768:8:1$ELcHhcrtvUvxrZ69$2736ccc3a4222a6ed38cc2ce10b4e60dabf29b03a1b53b4c393657c95e63f6e831a32b3ce8c2bad0ee8753559302973b6c0cb79ce1755720ffd4e587ef7b1a77	\N	\N	f
2	Bojken Gjoleka	bgjoleka@gmail.com	scrypt:32768:8:1$ysYoOKSsrxIt4jn8$7d22dce86fa34252db91f1070239b21f171c49c1374877dede3a9b7db54970990968f586f22b8de54bfcbea394d2e35572903719fbcd3aba06f01e03d834344f	\N	\N	f
3	Mandi Nishtulles	lucavehbiu96+test1@gmail.com	scrypt:32768:8:1$S4AWfoCEW1pKVh99$cadae8c040bf8fa886066d7ef32cea72920558f57c043865e472226bc43dfd3825521ae57ac8769c707daef45b5c5583f12b5d7758fd7411393ee3c9e5441e7e	\N	\N	f
4	Llahu	Rikes@gmail.com	scrypt:32768:8:1$u5XFrZbiWBiTLqbG$716f00c84b55d74f82469d4d2c284c91246bb53fc4c73cc4f2907d58fcc1ec67187d447f76a457fbbb1ac246eff57a31e6bf38dc73c614d7aea9a5c66290ab38	\N	\N	f
5	Tafil Hafizi	lucavehbiu96+test2@gmail.com	scrypt:32768:8:1$97fe7W6jWVvmT31V$2ed4774fc11a8e6169679271e60356243914a635823ed98eb64bc4bf42a93ef857ea9e907c1676f9db9eea6efdbf9f1296d8d182096b488965e9d88030217ded	\N	\N	f
6	Noed Dutch	lucavehbiu96+test3@gmail.com	scrypt:32768:8:1$OaLVu78YgHaDcPgF$9dafe11659cbaac2fe4de462c9747a7e3e4ac8fd15b3969067dc88b6ab0414ca3c858f65d0758bf253ff7b139ef4cbbf9be0579ef341f34e7604067c4be7ed4a	\N	\N	t
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
-- Name: lesson_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.lesson_id_seq', 1, false);


--
-- Name: lessons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.lessons_id_seq', 1, false);


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

SELECT pg_catalog.setval('public.use_cases_id_seq', 10, true);


--
-- Name: user_answers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.user_answers_id_seq', 62, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: data_admin
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


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
-- Name: lesson lesson_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_pkey PRIMARY KEY (id);


--
-- Name: lessons lessons_pkey; Type: CONSTRAINT; Schema: public; Owner: data_admin
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT lessons_pkey PRIMARY KEY (id);


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
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: data_admin
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

