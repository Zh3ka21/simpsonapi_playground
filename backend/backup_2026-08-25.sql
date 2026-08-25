--
-- PostgreSQL database dump
--

\restrict PBVPvRGahG0qutJEQ71azDgUJXMUJgFrCVr4xcgfK1l7H5kMzGNLC29AUxXvsdU

-- Dumped from database version 16.13 (Debian 16.13-1.pgdg13+1)
-- Dumped by pg_dump version 16.13 (Debian 16.13-1.pgdg13+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.actors (
    id bigint NOT NULL,
    first_name text,
    last_name text,
    "cast" text
);


ALTER TABLE public.actors OWNER TO admin;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.actors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.actors_id_seq OWNER TO admin;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO admin;

--
-- Name: ar_internal_metadata; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.ar_internal_metadata (
    key text NOT NULL,
    value text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);


ALTER TABLE public.ar_internal_metadata OWNER TO admin;

--
-- Name: catchphrases; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.catchphrases (
    id bigint NOT NULL,
    phrase text,
    character_id bigint
);


ALTER TABLE public.catchphrases OWNER TO admin;

--
-- Name: catchphrases_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.catchphrases_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.catchphrases_id_seq OWNER TO admin;

--
-- Name: catchphrases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.catchphrases_id_seq OWNED BY public.catchphrases.id;


--
-- Name: characters; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.characters (
    id bigint NOT NULL,
    name text,
    actor_id bigint
);


ALTER TABLE public.characters OWNER TO admin;

--
-- Name: characters_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.characters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.characters_id_seq OWNER TO admin;

--
-- Name: characters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.characters_id_seq OWNED BY public.characters.id;


--
-- Name: episodes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.episodes (
    id bigint NOT NULL,
    number bigint,
    title text,
    season_id bigint
);


ALTER TABLE public.episodes OWNER TO admin;

--
-- Name: episodes_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.episodes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.episodes_id_seq OWNER TO admin;

--
-- Name: episodes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.episodes_id_seq OWNED BY public.episodes.id;


--
-- Name: quotes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.quotes (
    id bigint NOT NULL,
    quote text,
    date date,
    character_id bigint,
    episode_id bigint
);


ALTER TABLE public.quotes OWNER TO admin;

--
-- Name: quotes_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.quotes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.quotes_id_seq OWNER TO admin;

--
-- Name: quotes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.quotes_id_seq OWNED BY public.quotes.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.schema_migrations (
    version text NOT NULL
);


ALTER TABLE public.schema_migrations OWNER TO admin;

--
-- Name: seasons; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.seasons (
    id bigint NOT NULL,
    number bigint,
    year_start bigint,
    year_end bigint,
    season_premiere date,
    season_finale date,
    average_viewers bigint,
    most_watched_episode_id bigint,
    most_watched_episode_viewers bigint
);


ALTER TABLE public.seasons OWNER TO admin;

--
-- Name: seasons_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.seasons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.seasons_id_seq OWNER TO admin;

--
-- Name: seasons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.seasons_id_seq OWNED BY public.seasons.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: catchphrases id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.catchphrases ALTER COLUMN id SET DEFAULT nextval('public.catchphrases_id_seq'::regclass);


--
-- Name: characters id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.characters ALTER COLUMN id SET DEFAULT nextval('public.characters_id_seq'::regclass);


--
-- Name: episodes id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.episodes ALTER COLUMN id SET DEFAULT nextval('public.episodes_id_seq'::regclass);


--
-- Name: quotes id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.quotes ALTER COLUMN id SET DEFAULT nextval('public.quotes_id_seq'::regclass);


--
-- Name: seasons id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.seasons ALTER COLUMN id SET DEFAULT nextval('public.seasons_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.actors (id, first_name, last_name, "cast") FROM stdin;
1	Dan	Castellaneta	Main
2	Nancy	Cartwright	Main
3	Julie	Kavner	Main
4	Yeardley	Smith	Main
5	Hank	Azaria	Main
6	Harry	Shearer	Main
7	Pamela	Hayden	Secondary
8	Tress	MacNeille	Secondary
9	Maggie	Roswell	Secondary
10	Russi	Taylor	Secondary
11	Marcia	Wallace	Guest
12	Phil	Hartman	Guest
13	Joe	Mantegna	Guest
14	Frank	Welker	Guest
15	Kelsey	Grammer	Guest
16	Jon	Lovitz	Guest
17	Albert	Brooks	Guest
18	Glenn	Close	Guest
19	Stephen	Hawking	Guest
21	Alex	Makbusson	Main
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: ar_internal_metadata; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.ar_internal_metadata (key, value, created_at, updated_at) FROM stdin;
environment	development	2018-01-29 16:37:38.175363+00	2018-01-29 16:37:38.175363+00
\.


--
-- Data for Name: catchphrases; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.catchphrases (id, phrase, character_id) FROM stdin;
1	D'oh!	1
2	Woo Hoo!	1
3	Why you little!	1
4	Mmm, donuts.	1
5	Aaargh!	1
6	Stupid Flanders.	1
7	BART!	1
8	Boring!	1
9	Whatever, I'll be at Moe's.	1
10	Let's All Go Out For Some Frosty Chocolate Milkshakes	1
11	Mmm~mmmmm	16
12	You have no idea what it's like, being married to you.	16
13	I don't think that's a very good idea.	16
14	Oh, Homie.	16
15	So man	16
16	Eat My Shorts!	12
17	Don't Have a Cow, Man!	12
18	¡Ay, caramba!	12
19	Get Bent.	12
20	I'm Bart Simpson, Who the Hell are You?	12
21	Cowabunga!	12
22	I Didn't Do It!	12
23	Aw, Man!	12
24	Aw, Geez!	12
25	Whoa, mama!	12
26	Eep!	12
27	If anyone wants me, I'll be in my room.	19
28	Quit it, Bart!	19
29	BAAAAAART!	19
30	Daddy.	71
31	Hi-Diddily-Ho!	38
32	Okily Dokily!	38
33	Toodily-Doo	38
34	What can I ding-dong-diddily-do for you?	38
35	Yay!!!	48
36	Ah, geez!!!	20
37	Aww, what's a matter, Homer?	20
38	WhaaaaAAAAAT?!	20
39	Moe's Tavern, Moe speaking.	20
40	Wors	24
41	Excellent!	36
42	Release the Hounds!	36
43	Smithers!	36
44	Ahoy-hoy?	36
45	Smithers, who's tha	36
46	Simpson, eh?	36
47	Yes, sir?	37
48	I never thought you'd ask!	37
49	Gumble	72
50	Hey, Hey Kids!	3
51	I didn't do it!	3
52	Ng Hey!	73
53	Glavin!	73
54	With th	73
55	Mmya	73
56	Ha Ha!	13
57	I wouldn't put it past him.	74
58	Ha Ha!	74
59	Hi, Everybody!	75
60	Ha!	61
61	Think of the Children!	55
62	Would someone Please think of the Children?	55
63	Dude!	76
64	Bye!	76
65	SIIIIIMMMMMPSOOOOOONNNNNNN!	77
66	Attention students...	77
67	SKINNER!	78
68	SEEEEYYYMOOUURRR!	78
69	SEYMOUR!	50
70	Yes.	79
71	Yargh!	30
72	Hi, I'm Troy McClure!	63
73	You may remember me from such ...	63
74	Thank You, Come Again!	22
75	Yee Haw!!	80
76	Cuff 'em, Lou,	21
77	Ay Ay Ay!	33
78	Hello, Bart.	66
79	Shut up.	81
80	Damn Flanders.	42
81	Listen up, you little FREAKS!	82
82	May God have mercy on us all.	83
83	CLANCY!	84
84	Oh, Yeah!	85
\.


--
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.characters (id, name, actor_id) FROM stdin;
1	Homer Simpson	1
2	Abe Simpson	1
3	Krusty the Clown	1
4	Barney Gumble	1
5	Groundskeeper Willie	1
6	Mayor Quimby	1
7	Hans Moleman	1
8	Sideshow Mel	1
9	Squeaky Voiced Teen	1
10	Gil	1
11	Rich Texan	1
12	Bart Simpson	2
13	Nelson Muntz	2
14	Ralph Wiggum	2
15	Kearny	2
16	Marge Simpson	3
17	Patty Bouvier	3
18	Selma Bouvier	3
19	Lisa Simpson	4
20	Moe Szyslak	5
21	Chief Wiggum	5
22	Apu Nahasapeemapetilon	5
23	Carl	5
24	Comic Book Guy	5
25	Lou	5
26	Prof. Frink	5
27	Cletus	5
28	Superintendent Chalmers	5
29	Snake	5
30	Sea Captain	5
31	Kirk Van Houten	5
32	Wiseguy	5
33	Bumblebee Man	5
34	Disco Stu	5
35	Dr. Nick	5
36	Mr. Burns	6
37	Waylon Smithers	6
38	Ned Flanders	6
39	Seymour Skinner	6
40	Lenny	6
41	Kent Brockman	6
42	Reverend Lovejoy	6
43	Dr. Hibbert	6
44	Otto	6
45	Jasper	6
46	Milhouse Van Houten	7
47	Jimbo	7
48	Rod Flanders	7
49	Todd Flanders	7
50	Agnes Skinner	8
51	Crazy Cat Lady	8
52	Lindsey Naegle	8
53	Manjula Nahasapeemapetilon	8
54	Maude Flanders	9
55	Helen Lovejoy	9
56	Ms. Hoover	9
57	Luann Van Houten	9
58	Martin Prince	10
59	Sherri Uter	10
60	Terry Uter	10
61	Edna Krabappel	11
62	Lionel Hutz	12
63	Troy McClure	12
64	Fat Tony	13
65	Santa's Little Helper	14
66	Sideshow Bob	15
67	Artie Ziff	16
68	Hank Scorpio	17
69	Mona Simpson	18
70	Stephen Hawking	19
71	Maggie Simpson	\N
72	Barney	\N
73	Professor Frink	\N
74	Mrs. Muntz	\N
75	Nick Riviera	\N
76	Snake Jailbird	\N
77	Principal Skinner	\N
78	Gary Chalmers	\N
79	The Yes Guy	\N
80	The Rich Texan	\N
81	Kearney	\N
82	Leopold	\N
83	Dr. Foster	\N
84	Sarah Wiggum	\N
85	Duffman	\N
\.


--
-- Data for Name: episodes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.episodes (id, number, title, season_id) FROM stdin;
1	1	Roasting on an Open Fire	1
2	2	Bart The Genius 1.03] Homer's Odyssey	1
3	4	There's No Disgrace Like Home	1
4	5	Bart the General	1
5	6	Moaning Lisa	1
6	7	The Call of the Simpsons	1
7	8	The Telltale Head	1
8	9	Life on the Fast Lane	1
9	10	Homer's Night Out	1
10	11	The Crepes of Wrath	1
11	12	Krusty Gets Busted	1
12	13	Some Enchanted Evening	1
13	1	Bart Gets an F	2
14	2	Simpson and Delilah	2
15	3	Treehouse of Horror	2
16	4	Two Cars in Every Garage and Three Eyes on Every Fish	2
17	5	Dancin' Homer	2
18	6	Dead Putting Society	2
19	7	Bart vs. Thanksgiving	2
20	8	Bart the Daredevil	2
21	9	Itchy & Scratchy & Marge	2
22	10	Bart Gets Hit by a Car	2
23	11	One Fish, Two Fish, Blowfish, Blue Fish	2
24	12	The Way We Was	2
25	13	Homer vs. Lisa and the 8th Commandment	2
26	14	Principal Charming	2
27	15	Oh Brother, Where Art Thou?	2
28	16	Bart's Dog Gets an F	2
29	17	Old Money	2
30	18	Brush with Greatness	2
31	19	Lisa's Substitute	2
32	20	The War of the Simpsons	2
33	21	Three Men and a Comic Book	2
34	22	Blood Feud	2
35	1	Stark Raving Dad	3
36	2	Mr. Lisa Goes to Washington	3
37	3	When Flanders Failed	3
38	4	Bart the Murderer	3
39	5	Homer Defined	3
40	6	Like Father, Like Clown	3
41	7	Treehouse of Horror II	3
42	8	Lisa's Pony	3
43	9	Saturdays of Thunder	3
44	10	Flaming Moe's	3
45	11	Burns Verkaufen der Kraftwerk	3
46	12	I Married Marge	3
47	13	Radio Bart	3
48	14	Lisa the Greek	3
49	15	Homer Alone	3
50	16	Bart the Lover	3
51	17	Homer at the Bat	3
52	18	Separate Vocations	3
53	19	Dog of Death	3
54	20	Colonel Homer	3
55	21	Black Widower	3
56	22	The Otto Show	3
57	23	Bart's Friend Falls in Love	3
58	24	Brother Can You Spare Two Dimes?	3
59	1	Kamp Krusty	4
60	2	A Streetcar Named Marge	4
61	3	Homer the Heretic	4
62	4	Lisa the Beauty Queen	4
63	5	Treehouse of Horror III	4
64	6	Itchy & Scratchy: The Movie	4
65	7	Marge Gets a Job	4
66	8	New Kid on the Block	4
67	9	Mr. Plow	4
68	10	Lisa's First Word	4
69	11	Homer's Triple Bypass	4
70	12	Marge vs. the Monorail	4
71	13	Selma's Choice	4
72	14	Brother from the Same Planet	4
73	15	I Love Lisa	4
74	16	Duffless	4
75	17	Last Exit to Springfield	4
76	18	So It's Come to This: A Simpsons Clip Show	4
77	19	The Front	4
78	20	Whacking Day	4
79	21	Marge in Chains	4
80	22	Krusty Gets Kancelled	4
81	1	Homer's Barbershop Quartet	5
82	2	Cape Feare	5
83	3	Homer Goes to College	5
84	4	Rosebud	5
85	5	Treehouse of Horror IV	5
86	6	Marge on the Lam	5
87	7	Bart's Inner Child	5
88	8	Boy-Scoutz N the Hood	5
89	9	The Last Temptation of Homer	5
90	10	$pringfield (Or, How I Learned to Stop Worrying and Love Legalized Gambling)	5
91	11	Homer the Vigilante	5
92	12	Bart Gets Famous	5
93	13	Homer and Apu	5
94	14	Lisa vs. Malibu Stacy	5
95	15	Deep Space Homer	5
96	16	Homer Loves Flanders	5
97	17	Bart Gets an Elephant	5
98	18	Burns' Heir	5
99	19	Sweet Seymour Skinner's Badasssss Song	5
100	20	The Boy Who Knew Too Much	5
101	21	Lady Bouvier's Lover	5
102	22	Secrets of a Successful Marriage	5
103	1	Bart of Darkness	6
104	2	Lisa's Rival	6
105	3	Another Simpsons Clip Show	6
106	4	Itchy & Scratchy Land	6
107	5	Sideshow Bob Roberts	6
108	6	Bart's Girlfriend	6
109	7	Treehouse of Horror V	6
110	8	Lisa on Ice	6
111	9	Homer: Bad Man	6
112	10	Grampa vs. Sexual Inadequacy	6
113	11	Fear of Flying	6
114	12	Homer the Great	6
115	13	And Maggie Makes Three	6
116	14	Bart's Comet	6
117	15	Homie the Clown	6
118	16	Bart vs. Australia	6
119	17	Homer vs. Patty & Selma	6
120	18	A Star is Burns	6
121	19	Lisa's Wedding	6
122	20	Two Dozen and One Greyhounds	6
123	21	The PTA Disbands!	6
124	22	'Round Springfield	6
125	23	The Springfield Connection	6
126	24	Lemon of Troy	6
127	25	Who Shot Mr. Burns? (Part 1)	6
128	21	Who Shot Mr. Burns? (Part 2)	6
129	2	Radioactive Man	7
130	3	Home Sweet Home-Dum-Diddly-Doodily	7
131	4	Bart Sells His Soul	7
132	5	Lisa the Vegetarian	7
133	6	Treehouse of Horror VI	7
134	7	King-Size Homer	7
135	8	Mother Simpson	7
136	9	Sideshow Bob's Last Gleaming	7
137	10	The Simpsons 138th Episode Spectacular	7
138	11	Marge Be Not Proud	7
139	12	Team Homer	7
140	13	Two Bad Neighbors	7
141	14	Scenes from the Class Struggle in Springfield	7
142	15	Bart the Fink	7
143	16	Lisa the Iconoclast	7
144	17	Homer the Smithers	7
145	18	The Day the Violence Died	7
146	19	A Fish Called Selma	7
147	20	Bart on the Road	7
148	21	22 Short Films About Springfield	7
149	22	Raging Abe Simpson and His Grumbling Grandson in "The Curse of the Flying Hellfish"	7
150	23	Much Apu About Nothing	7
151	24	Homerpalooza	7
152	25	Summer of 4 Ft. 2	7
153	1	Treehouse of Horror VII	8
154	2	You Only Move Twice	8
155	3	The Homer They Fall	8
156	4	Burns, Baby Burns	8
157	5	Bart After Dark	8
158	6	A Milhouse Divided	8
159	7	Lisa's Date with Density	8
160	8	Hurricane Neddy	8
161	9	El Viaje Misterioso de Nuestro Jomer	8
162	10	The Springfield Files	8
163	11	The Twisted World of Marge Simpson	8
164	12	Mountain of Madness	8
165	13	Simpsoncalifragilisticexpiala(Annoyed Grunt)cious	8
166	14	The Itchy & Scratchy & Poochie Show Episode 15.Homer's Phobia	8
167	16	Brother from Another Series	8
168	17	My Sister, My Sitter	8
169	18	Homer vs. The Eighteenth Amendment	8
170	19	Grade School Confidential	8
171	20	The Canine Mutiny	8
172	21	The Old Man and the Lisa	8
173	22	In Marge We Trust	8
174	23	Homer's Enemy	8
175	24	The Simpsons Spin-Off Showcase	8
176	25	The Secret War of Lisa Simpson	8
177	1	The City of New York vs. Homer Simpson	9
178	2	The Principal and the Pauper	9
179	3	Lisa's Sax	9
180	4	Treehouse of Horror VIII	9
181	5	The Cartridge Family Episode 6.Bart Star	9
182	7	The Two Mrs. Nahasapeemapetilons	9
183	8	Lisa the Skeptic	9
184	9	Realty Bites	9
185	10	Miracle on Evergreen Terrace	9
186	11	All Singing, All Dancing	9
187	12	Bart Carny	9
188	13	The Joy of Sect	9
189	14	Das Bus	9
190	15	The Last Temptation of Krust	9
191	16	Dumbbell Indemnity	9
192	17	Lisa the Simpson	9
193	18	This Little Wiggy	9
194	19	Simpson Tide	9
195	20	The Trouble with Trillions	9
196	21	Girly Edition	9
197	22	Trash of the Titans	9
198	23	King of the Hill	9
199	24	Lost Our Lisa	9
200	25	Natural Born Kissers	9
201	1	Lard of the Dance	10
202	2	The Wizard of Evergreen Terrace	10
203	3	Bart the Mother	10
204	4	Treehouse of Horror IX	10
205	5	When You Dish Upon a Star	10
206	6	D'oh-in in the Wind	10
207	7	Lisa Gets an "A"	10
208	8	Homer Simpson in: "Kidney Trouble"	10
209	9	Mayored to the Mob	10
210	10	Viva Ned Flanders	10
211	11	Wild Barts Can't Be Broken	10
212	12	Sunday, Cruddy Sunday	10
213	13	Homer to the Max	10
214	14	I'm With Cupid	10
215	15	Marge Simpson in: "Screaming Yellow Honkers"	10
216	16	Make Room for Lisa	10
217	17	Maximum Homerdrive	10
218	18	Simpsons Bible Stories	10
219	19	Mom and Pop Art	10
220	20	The Old Man and The "C" Student	10
221	21	Monty Can't Buy Me Love	10
222	22	They Saved Lisa's Brain	10
223	23	Thirty Minutes Over Tokyo	10
224	1	Beyond Blunderdome	10
225	2	Brother's Little Helper	11
226	3	Guess Who's Coming to Criticize Dinner?	11
227	4	Treehouse of Horror X	11
228	5	E-I-E-I-(Annoyed Grunt)	11
229	6	Hello Gutter, Hello Fadder	11
230	7	Eight Misbehavin'	11
231	8	Take My Wife, Sleaze	11
232	9	Grift of the Magi	11
233	10	Little Big Mom	11
234	11	Faith Off	11
235	12	The Mansion Family	11
236	13	Saddlesore Galactica	11
237	14	Alone Again, Natura-Diddily	11
238	15	Missionary: Impossible	11
239	16	Pygmoelian	11
240	17	Bart to the Future	11
241	18	Days of Wine and D'oh'ses	11
242	19	Kill the Alligator and Run	11
243	20	Last Tap Dance in Springfield	11
244	21	It's A Mad, Mad, Mad, Mad Marge	11
245	22	Behind the Laughter	11
246	1	Treehouse of Horror XI	12
247	2	A Tale of Two Springfields	12
248	3	Insane Clown Poppy	12
249	4	Lisa the Tree Hugger	12
250	5	Homer vs. Dignity	12
251	6	The Computer Wore Menace Shoes	12
252	7	The Great Money Caper	12
253	8	Skinner's Sense of Snow	12
254	9	HOMЯ	12
255	10	Pokey Mom	12
256	11	Worst Episode Ever	12
257	12	Tennis the Menace	12
258	13	Day of the Jackanapes	12
259	14	New Kids on the Blecch	12
260	15	Hungry, Hungry Homer	12
261	16	Bye Bye Nerdie	12
262	17	Simpson Safari	12
263	18	Trilogy of Error	12
264	19	I'm Goin' to Praiseland	12
265	20	Children of a Lesser Clod	12
266	21	Simpsons Tall Tales	12
267	1	Treehouse of Horror 12	21
268	2	The Parent Rap	13
269	3	Homer the Moe	13
270	4	A Hunka Hunka Burns in Love	13
271	5	The Blunder Years	13
272	6	She of Little Faith	13
273	7	Brawl in the Family	13
274	8	Sweets and Sour Marge	13
275	9	Jaws Wired Shut	13
276	10	Half-Decent Proposal	13
277	11	The Bart Wants What It Wants	13
278	12	The Lastest Gun in the West	13
279	13	The Old Man and the Key	13
280	14	Tales from the Public Domain	13
281	15	Blame it on Lisa	13
282	16	Weekend at Burnsie's	13
283	17	Gump Roast	13
284	18	I am Furious Yellow	13
285	19	The Sweetest Apu	13
286	20	Little Girl in the Big Ten	13
287	21	The Frying Game	13
288	22	Papa's Got a Brand New Badge	13
289	1	Treehouse of Horror 13	13
290	2	How I Spent My Strummer Vacation	14
291	3	Bart vs. Lisa vs. The Third Grade	14
292	4	Large Marge	14
293	5	Helter Shelter	14
294	6	The Great Louse Detective Episode 7.Special Edna	14
295	8	The Dad Who Knew Too Little	14
296	9	Strong Arms of The Ma	14
297	10	Pray Anything Episode 11.Barting Over	14
298	12	I'm Spelling as Fast as I Can	14
299	13	A Star is Born-Again	14
300	14	Mr. Spritz Goes to Washington Episode 15.C.E. D'oh	14
301	16	'Scuse Me While I Miss the Sky	14
302	17	Three Gays of the Condo	14
303	18	Dude, Where's My Ranch?	14
304	19	Old Yeller Belly	14
305	20	Brake My Wife, Please	14
306	21	Bart of War	14
307	22	Moe Baby Blues	14
308	1	Treehouse of Horror 14	14
309	2	My Mother the Carjacker	15
310	3	The President Wore Pearls	15
311	4	The Regina Monologues	15
312	5	The Fat and the Furriest	15
313	6	Today I am A Clown	15
314	7	'Tis the Fifteenth Season	15
315	8	Marge vs. Singles, Seniors, Childless Couples and Teens, and Gays	15
316	9	I, (Annoyed Grunt)-Bot	15
317	10	Diatribe of a Mad Housewife	15
318	11	Margical History Tour	15
319	12	Milhouse Doesn't Live Here Anymore	15
320	13	Smart and Smarter	15
321	14	The Ziff Who Came to Dinner	15
322	15	Co-Dependent's Day	15
323	16	The Wandering Juvie	15
324	17	My Big Fat Geek Wedding	15
325	18	Catch 'em If You Can	15
326	19	Simple Simpson	15
327	20	The Way We Weren't	15
328	21	Bart-Mangled Banner	15
329	22	Fraudcast News	15
330	1	Treehouse of Horror 15	15
331	2	All's Fair in Oven War	16
332	3	Sleeping With the Enemy	16
333	4	She Used to Be My Girl	16
334	5	Fat Man and Little Boy	16
335	7	Mommie Beerest	16
336	8	Homer and Ned's Hail Mary Pass	16
337	9	Pranksta Rap	16
338	10	There's Something About Marrying	16
339	11	On a Clear Day I Can't See My Sister	16
340	12	Goo Goo Gai Pan	16
341	13	Mobile Homer	16
342	14	The Seven-Beer Snitch Episode 15.Future-Drama	16
343	16	Don't Fear the Roofer	16
344	17	The Heartbroke Kid	16
345	18	A Star is Torn	16
346	19	Thank God It's Doomsday	16
347	20	Home Away From Homer	16
348	21	The Father, The Son, and The Holy Guest Star	16
349	1	Bonfire of the Manatees	16
350	2	The Girl Who Slept Too Little	17
351	3	Milhouse of Sand and Fog	17
352	4	Treehouse of Horror XVI	17
353	5	Marge's Son Poisoning	17
354	6	See Homer Run	17
355	7	The Last of the Red Hat Mamas	17
356	8	The Italian Bob	17
357	9	Simpsons Christmas Stories	17
358	10	Homer's Paternity Coot	17
359	11	We're on the Road to D'ohwhere	17
360	12	My Fair Laddy	17
361	13	The Seemingly Never-Ending Story	17
362	14	Bart Has Two Mommies	17
363	15	Homer Simpson, This Is Your Wife	17
364	16	Million Dollar Abie	17
365	17	Kiss Kiss, Bang Bangalore	17
366	18	The Wettest Stories Ever Told	17
367	19	Girls Just Want To Have Sums	17
368	20	Regarding Margie	17
369	21	The Monkey Suit	17
370	22	Marge and Homer Turn a Couple Play	17
371	1	The Mook, The Chef, The Wife And Her Homer	18
372	2	Jazzy and the Pussycats	18
373	3	Please Homer, Don't Hammer 'Em...	18
374	4	Treehouse of Horror XVII	18
375	5	G.I. (Annoyed Grunt)	18
376	6	Moe'N'a Lisa	18
377	7	Ice Cream of Margie (With the Light Blue Hair)	18
378	8	The Haw-Hawed Couple	18
379	9	Kill Gil: Vols. 1 & 2	18
380	10	The Wife Aquatic	18
381	11	Revenge is a Dish Best Served Three Times	18
382	12	Little Big Girl	18
383	13	Springfield Up	18
384	14	Yokel Chords	18
385	15	Rome-old and Juli-eh	18
386	16	Homerazzi	18
387	17	Marge Gamer	18
388	18	The Boys of Bummer	18
389	19	Crook and Ladder	18
390	20	Stop, or My Dog Will Shoot!	18
391	21	24 Minutes	18
392	22	You Kent Always Say What You Want	18
393	1	He Loves to Fly and He D'ohs	18
394	2	The Homer of Seville	19
395	3	Midnight Towboy	19
396	4	I Don't Wanna Know Why the Caged Bird Sings	19
397	5	Treehouse of Horror 18	19
398	6	Little Orphan Millie	19
399	7	Husbands and Knives	19
400	8	Funeral for a Fiend	19
401	9	Eternal Moonshine of the Simpson Mind	19
402	10	E. Pluribus Wiggum	19
403	11	That 90's Show	19
404	12	Love, Springfieldian Style	19
405	13	The Debarted	19
406	14	Dial 'N' for Nerder	19
407	15	Smoke on the Daughter	19
408	16	Papa Don't Leech	19
409	17	Apocalypse Cow	19
410	18	Any Given Sundance	19
411	19	Mona Leaves-a	19
412	20	All About Lisa	19
413	1	Sex, Pies and Idiot Scrapes	20
414	2	Lost Verizon	20
415	3	Double, Double, Boy in Trouble	20
416	4	Treehouse of Horror XIX	20
417	5	Dangerous Curves	20
418	6	Homer and Lisa Exchange Cross Words	20
419	7	Mypods and Boomsticks	20
420	8	The Burns and the Bees	20
421	9	Lisa the Drama Queen	20
422	10	Take My Life, Please	20
423	11	How the Test Was Won	20
424	12	No Loan Again, Naturally	20
425	13	Gone Maggie Gone	20
426	14	In the Name of the Grandfather	20
427	15	Wedding for Disaster	20
428	16	Eeny Teeny Maya Moe	20
429	17	The Good, the Sad and the Drugly	20
430	18	Father Knows Worst	20
431	19	Waverly Hills 9021-D'oh	20
432	20	Four Great Women and a Manicure	20
433	21	Coming to Homerica	20
434	1	Homer the Whopper	21
435	2	Bart Gets a 'Z'	21
436	3	The Great Wife Hope	21
437	4	Treehouse of Horror XX	21
438	5	The Devil Wears Nada	21
439	6	Pranks and Greens	21
440	7	Rednecks and Broomsticks	21
441	8	O Brother, Where Bart Thou?	21
442	9	Thursdays with Abie	21
443	10	Once Upon a Time in Springfield	21
444	11	Million Dollar Maybe	21
445	12	Boy Meets Curl	21
446	13	The Color Yellow	21
447	14	Postcards from the Wedge	21
448	15	Stealing First Base	21
449	16	The Greatest Story Ever D'ohed	21
450	17	American History X-cellent	21
451	18	Chief of Hearts	21
452	19	The Squirt and the Whale	21
453	20	To Surveil With Love	21
454	21	Moe Letter Blues	21
455	22	The Bob Next Door	21
456	23	Judge Me Tender	21
457	1	Elementary School Musical	22
458	2	Loan-a Lisa	22
459	3	MoneyBART	22
460	4	Treehouse of Horror XXI	22
461	5	Lisa Simpson, This Isn't Your Life	22
462	6	The Fool Monty	22
463	7	How Munched is That Birdie in the Window?	22
464	8	The Fight Before Christmas	22
465	9	Donnie Fatso	22
466	10	Moms I'd Like to Forget	22
467	11	Flaming Moe	22
468	12	Homer the Father	22
469	13	The Blue and the Gray	22
470	14	Angry Dad: The Movie	22
471	15	The Scorpion's Tale	22
472	16	A Midsummer's Nice Dream	22
473	17	Love Is a Many Strangled Thing	22
474	18	The Great Simpsina	22
475	19	The Real Housewives of Fat Tony	22
476	20	Homer Scissorhands	22
477	21	500 Keys	22
478	22	The Ned-Liest Catch	22
479	1	The Falcon and the D'ohman	23
480	2	Bart Stops to Smell the Roosevelts	23
481	3	Treehouse of Horror XXII	23
482	4	Replaceable You	23
483	5	The Food Wife	23
484	6	The Book Job	23
485	7	The Man in the Blue Flannel Pants	23
486	8	The Ten-Per-Cent Solution	23
487	9	Holidays of Future Passed	23
488	10	Politically Inept, with Homer Simpson	23
489	11	The D'oh-cial Network	23
490	12	Moe Goes from Rags to Riches	23
491	13	The Daughter Also Rises	23
492	14	At Long Last Leave	23
493	15	Exit Through the Kwik-E-Mart	23
494	16	How I Wet Your Mother	23
495	17	Them, Robot	23
496	18	Beware My Cheating Bart	23
497	19	A Totally Fun Thing That Bart Will Never Do Again	23
498	20	The Spy Who Learned Me	23
499	21	Ned 'N Edna's Blend	23
500	22	Lisa Goes Gaga	23
501	1	Moonshine River	24
502	2	Treehouse of Horror XXIII	24
503	3	Adventures in Baby-Getting	24
504	4	Gone Abie Gone	24
505	5	Penny-Wiseguys	24
506	6	A Tree Grows in Springfield	24
507	7	The Day the Earth Stood Cool	24
508	8	To Cur With Love	24
509	9	Homer Goes to Prep School	24
510	10	A Test Before Trying	24
511	11	The Changing of the Guardian	24
512	12	Love is a Many-Splintered Thing	24
513	13	Hardly Kirk-ing	24
514	14	Gorgeous Grampa	24
515	15	Black Eyed, Please	24
516	16	Dark Knight Court	24
517	17	What Animated Women Want	24
518	18	Pulpit Friction	24
519	19	Whiskey Business	24
520	20	The Fabulous Faker Boy	24
521	21	The Saga of Carl	24
522	22	Dangers on a Train	24
523	1	Homerland	25
524	2	Treehouse of Horror XXIV	25
525	3	Four Regrettings and a Funeral	25
526	4	YOLO	25
527	5	Labor Pains	25
528	6	The Kid is All Right	25
529	7	Yellow Subterfuge	25
530	8	White Christmas Blues	25
531	9	Steal This Episode	25
532	10	Married to the Blob	25
533	11	Specs and the City	25
534	12	Diggs	25
535	13	The Man Who Grew Too Much	25
536	14	The Winter of His Content	25
537	15	The War of Art	25
538	16	You Don't Have to Live Like a Referee	25
539	17	Luca$	25
540	18	Days of Future Future	25
541	19	What to Expect When Bart's Expecting	25
542	20	Brick Like Me	25
543	21	Pay Pal	25
544	22	The Yellow Badge of Cowardge	25
545	1	Clown in the Dumps	26
546	2	The Wreck of the Relationship	26
547	3	Super Franchise Me	26
548	4	Treehouse of Horror XXV	26
549	5	Opposites A-Frack	26
550	6	Simpsorama	26
551	7	Blazed and Confused	26
552	8	Covercraft	26
553	9	I Won't Be Home for Christmas	26
554	10	The Man Who Came to Be Dinner	26
555	11	Bart's New Friend	26
556	12	The Musk Who Fell To Earth	26
557	13	Walking Big & Tall	26
558	14	My Fare Lady	26
559	15	The Princess Guide	26
560	16	Sky Police	26
561	17	Waiting for Duffman	26
562	18	Peeping Mom	26
563	19	The Kids Are All Fight	26
564	20	Let's Go Fly a Coot	26
565	21	Bull-E	26
566	22	Mathlete's Feat	26
567	1	Every Man's Dream	27
568	2	Cue Detective	27
569	3	Puffless	27
570	4	Halloween of Horror	27
571	5	Treehouse of Horror XXVI	27
572	6	Friend with Benefit	27
573	7	Lisa with a 'S'	27
574	8	Paths of Glory	27
575	9	Barthood	27
576	10	The Girl Code	27
577	11	Teenage Mutant Milk-Caused Hurdles	27
578	12	Much Apu About Something	27
579	13	Love Is in the N2-O2-Ar-CO2-Ne-He-CH4	27
580	14	Gal of Constant Sorrow	27
581	15	Lisa the Veterinarian	27
582	16	The Marge-ian Chronicles	27
583	17	The Burns Cage	27
584	18	How Lisa Got Her Marge Back	27
585	19	Fland Canyon	27
586	20	To Courier with Love	27
587	21	Simprovised	27
588	22	Orange Is the New Yellow	27
589	1	Monty Burns' Fleeing Circus	28
590	2	Friends and Family	28
591	3	The Town	28
592	4	Treehouse of Horror XXVII	28
593	5	Trust but Clarify	28
594	6	There Will Be Buds	28
595	7	Havana Wild Weekend	28
596	8	Dad Behavior	28
597	9	The Last Traction Hero	28
598	10	The Nightmare After Krustmas	28
599	11	Pork and Burns	28
600	12	The Great Phatsby, Part 1	28
601	13	The Great Phatsby, Part 2	28
602	14	Fatzcarraldo	28
603	15	The Cad and the Hat	28
604	16	Kamp Krustier	28
605	17	22 for 30	28
606	18	A Father's Watch	28
607	19	Caper Chase	28
608	20	Looking for Mr. Goodbart	28
609	21	Moho House	28
610	22	Dogtown	28
611	1	The Serfsons	29
612	2	Springfield Splendor	29
613	3	Whistler's Father	29
614	4	Treehouse of Horror XXVIII	29
615	5	Grampy Can Ya Hear Me	29
616	6	The Old Blue Mayor She Ain't What She Used to Be	29
617	7	Singin' in the Lane	29
618	8	Mr. Lisa's	29
\.


--
-- Data for Name: quotes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.quotes (id, quote, date, character_id, episode_id) FROM stdin;
1	There's only one thing to do at a moment like this: strut!	1994-11-06	12	108
2	Your ideas are intriguing to me, and I wish to subscribe to your newsletter.	1997-02-02	1	164
3	Everything's coming up Milhouse.	1999-04-11	46	219
4	I used to be with it, but then they changed what ‘it' was, and now what I'm with isn't it. And what's ‘it' seems weird and scary to me.	1996-05-19	2	151
5	I, for one, welcome our new insect overlords.	1994-02-24	41	95
6	It takes two to lie: one to lie and one to listen.	1992-03-26	1	54
7	I would kill everyone in this room for a drop of sweet beer.	1993-02-18	1	74
8	They taste like burning.	1998-02-15	14	189
9	Marriage is like a coffin and each kid is another nail.	2002-11-10	1	290
10	I've said it before and I'll say it again: democracy simply doesn't work.	1995-02-05	41	116
11	What's the point of going out? We're just gonna wind up back here anyway.	1996-02-04	1	141
12	I didn't think it was physically possible, but this both sucks and blows.	1999-02-21	12	215
13	Loneliness and cheeseburgers are a dangerous mix.	1997-03-02	24	168
14	You tried your best and you failed miserably. The lesson is: Never try.	1994-04-14	1	98
15	There's a 4:30 in the morning now?	1995-02-05	12	116
16	Don't blame me, I voted for Kodos.	1996-10-27	1	153
17	I can't promise I'll try, but I'll try to try.	1997-04-13	12	171
18	My cat's breath smells like cat food.	1994-09-11	14	104
\.


--
-- Data for Name: schema_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.schema_migrations (version) FROM stdin;
20171231201726
20171231200717
20171231200933
20171231200659
20171231200826
20171231200845
\.


--
-- Data for Name: seasons; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.seasons (id, number, year_start, year_end, season_premiere, season_finale, average_viewers, most_watched_episode_id, most_watched_episode_viewers) FROM stdin;
1	1	1989	1990	1989-12-17	1990-05-13	27000000	8	33000000
2	2	1990	1991	1990-10-11	1991-07-11	24000000	13	33000000
3	3	1991	1992	1991-09-19	1992-08-27	21000000	54	25000000
4	4	1992	1993	1992-09-24	1993-05-13	22000000	68	28000000
5	5	1993	1994	1993-09-30	1994-05-19	18000000	85	24000000
6	6	1994	1995	1994-09-04	1995-05-21	15000000	109	22000000
7	7	1995	1996	1995-09-17	1996-05-19	15000000	133	19000000
8	8	1996	1997	1996-10-27	1997-05-18	14000000	162	20000000
9	9	1997	1998	1997-09-21	1998-05-17	16000000	182	19000000
10	10	1998	1999	1998-08-23	1999-05-16	13000000	217	15000000
11	11	1999	2000	1999-09-26	2000-05-21	8000000	235	18000000
12	12	2000	2001	2000-11-01	2001-05-20	15000000	256	18000000
13	13	2001	2002	2001-11-06	2002-05-22	12000000	268	14000000
14	14	2002	2003	2002-11-03	2003-05-18	14000000	298	22000000
15	15	2003	2004	2003-11-02	2004-05-23	11000000	316	16000000
16	16	2004	2005	2004-11-07	2005-05-15	10000000	336	23000000
17	17	2005	2006	2005-09-11	2006-05-21	9000000	352	11000000
18	18	2006	2007	2006-09-10	2007-05-20	9000000	380	13000000
19	19	2007	2008	2007-09-23	2008-05-18	8000000	\N	11000000
20	20	2008	2009	2008-09-28	2009-05-17	7000000	416	12000000
21	21	2009	2010	2009-09-27	2010-05-23	7000000	443	14000000
22	22	2010	2011	2010-09-26	2011-05-22	7000000	466	12000000
23	23	2011	2012	2011-09-25	2012-05-20	6000000	489	11000000
24	24	2012	2013	2012-09-30	2013-05-19	5000000	509	8000000
25	25	2013	2014	2013-09-29	2014-05-18	5000000	531	12000000
26	26	2014	2015	2014-09-28	2015-05-17	5000000	554	10000000
27	27	2015	2016	2015-09-27	2016-05-22	4000000	577	8000000
28	28	2016	2017	2016-09-25	2017-05-21	4000000	599	8000000
29	29	2017	2018	2017-10-01	\N	\N	\N	\N
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.actors_id_seq', 21, true);


--
-- Name: catchphrases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.catchphrases_id_seq', 84, true);


--
-- Name: characters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.characters_id_seq', 86, true);


--
-- Name: episodes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.episodes_id_seq', 618, true);


--
-- Name: quotes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.quotes_id_seq', 18, true);


--
-- Name: seasons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.seasons_id_seq', 29, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: actors idx_16467_actors_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT idx_16467_actors_pkey PRIMARY KEY (id);


--
-- Name: catchphrases idx_16474_catchphrases_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.catchphrases
    ADD CONSTRAINT idx_16474_catchphrases_pkey PRIMARY KEY (id);


--
-- Name: characters idx_16481_characters_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT idx_16481_characters_pkey PRIMARY KEY (id);


--
-- Name: episodes idx_16488_episodes_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.episodes
    ADD CONSTRAINT idx_16488_episodes_pkey PRIMARY KEY (id);


--
-- Name: quotes idx_16495_quotes_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.quotes
    ADD CONSTRAINT idx_16495_quotes_pkey PRIMARY KEY (id);


--
-- Name: seasons idx_16502_seasons_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.seasons
    ADD CONSTRAINT idx_16502_seasons_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations idx_16506_sqlite_autoindex_schema_migrations_1; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT idx_16506_sqlite_autoindex_schema_migrations_1 PRIMARY KEY (version);


--
-- Name: ar_internal_metadata idx_16511_sqlite_autoindex_ar_internal_metadata_1; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.ar_internal_metadata
    ADD CONSTRAINT idx_16511_sqlite_autoindex_ar_internal_metadata_1 PRIMARY KEY (key);


--
-- Name: idx_16474_index_catchphrases_on_character_id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_16474_index_catchphrases_on_character_id ON public.catchphrases USING btree (character_id);


--
-- Name: idx_16481_index_characters_on_actor_id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_16481_index_characters_on_actor_id ON public.characters USING btree (actor_id);


--
-- Name: idx_16488_index_episodes_on_season_id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_16488_index_episodes_on_season_id ON public.episodes USING btree (season_id);


--
-- Name: idx_16495_index_quotes_on_character_id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_16495_index_quotes_on_character_id ON public.quotes USING btree (character_id);


--
-- Name: idx_16495_index_quotes_on_episode_id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_16495_index_quotes_on_episode_id ON public.quotes USING btree (episode_id);


--
-- PostgreSQL database dump complete
--

\unrestrict PBVPvRGahG0qutJEQ71azDgUJXMUJgFrCVr4xcgfK1l7H5kMzGNLC29AUxXvsdU

