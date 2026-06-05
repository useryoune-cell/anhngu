# -*- coding: utf-8 -*-
"""Seed real learning content for the Lingo Flask app.

Run:
    python seed_real_data.py
"""

from datetime import datetime, timedelta
import json
from pathlib import Path

from werkzeug.security import generate_password_hash

from app import (
    BASE_DIR,
    COURSE_FILE_DIR,
    DB_PATH,
    MATERIAL_DIR,
    SKILL_FILE_DIR,
    app,
    get_db,
    init_db,
)


SEED_PASSWORD = "123456"
TEACHER_USERNAME = "giaovien01"
MAIN_STUDENT_USERNAME = "hocsinh01"

MATERIAL_TITLES = [
    "B1 Reading: Study Habits That Actually Work",
    "A2 Vocabulary: Daily Routines and Time",
    "Pronunciation Mini Lesson: Word Stress",
]

COURSE_TITLES = [
    "Present Perfect for Real Life",
    "Giving Opinions in Speaking Part 2",
    "Reading for Main Idea and Detail",
]

QUIZ_PACKAGE_TITLES = [
    "Quiz B1 - Grammar and Vocabulary",
    "Quiz A2 - Everyday English",
]

LISTENING_TITLES = [
    "Listening A2: Planning a Weekend",
    "Listening B1: A Study Group Conversation",
]

GRAMMAR_TITLES = [
    "Grammar A2: Past Simple vs Present Perfect",
    "Grammar B1: First Conditional",
]

WRITING_TITLES = [
    "Writing Task: Email to a Teacher",
    "Writing Task: Opinion Paragraph about Online Learning",
]

SPEAKING_TITLES = [
    "Speaking Shadowing: My Daily Study Routine",
    "Speaking Shadowing: Describing a Favorite Place",
]

EXAM_SPEAKING_TITLES = [
    "Speaking AI Test: Hobbies and Free Time",
    "Speaking AI Test: Learning English Online",
]

EXAM_ROOM_TITLES = [
    "B1 Mock Test - Reading and Use of English",
    "A2 Quick Test - Vocabulary and Grammar",
]


STUDENTS = [
    ("hocsinh01", "hocsinh01@lingo.vn", "Nguyễn Minh Anh", "10A1", "0912000001"),
    ("linhtran", "linhtran@lingo.vn", "Trần Khánh Linh", "10A1", "0912000002"),
    ("baongoc", "baongoc@lingo.vn", "Phạm Bảo Ngọc", "10A2", "0912000003"),
    ("tuananh", "tuananh@lingo.vn", "Hoàng Tuấn Anh", "10A2", "0912000004"),
    ("phuongvy", "phuongvy@lingo.vn", "Đỗ Phương Vy", "11A1", "0912000005"),
    ("haidang", "haidang@lingo.vn", "Ngô Hải Đăng", "11A1", "0912000006"),
    ("anhnhi", "anhnhi@lingo.vn", "Huỳnh An Nhi", "11A2", "0912000007"),
    ("quocbao", "quocbao@lingo.vn", "Mai Quốc Bảo", "11A2", "0912000008"),
    ("thanhtruc", "thanhtruc@lingo.vn", "Bùi Thanh Trúc", "12A1", "0912000009"),
    ("minhkhang", "minhkhang@lingo.vn", "Lê Minh Khang", "12A1", "0912000010"),
    ("nhatminh", "nhatminh@lingo.vn", "Đặng Nhật Minh", "12A2", "0912000011"),
    ("giahuy", "giahuy@lingo.vn", "Võ Gia Huy", "12A2", "0912000012"),
]


def write_seed_file(directory, filename, title, body):
    directory.mkdir(parents=True, exist_ok=True)
    file_path = directory / filename
    html = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.65;
      margin: 0;
      padding: 28px;
      color: #17202a;
      background: #fffaf0;
    }}
    h1 {{ color: #0f8f73; margin-top: 0; }}
    h2 {{ color: #f05a28; margin-top: 24px; }}
    .note {{
      border-left: 5px solid #f7c948;
      background: #fff4c2;
      padding: 12px 16px;
      margin: 18px 0;
      border-radius: 8px;
    }}
    table {{ width: 100%; border-collapse: collapse; background: #fff; }}
    th, td {{ border: 1px solid #eadfcb; padding: 10px; text-align: left; }}
    th {{ background: #ffe8a3; }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  {body}
</body>
</html>
"""
    file_path.write_text(html, encoding="utf-8")
    return file_path


def prepare_seed_files():
    material_1 = write_seed_file(
        MATERIAL_DIR,
        "seed_b1_study_habits.html",
        "B1 Reading: Study Habits That Actually Work",
        """
        <p>Many students spend hours reading notes again and again, but research-based study habits are more active. A useful routine is to learn a small amount, close the book, and explain the idea in your own words.</p>
        <div class="note">Key idea: active recall and spaced review help learners remember vocabulary and grammar longer.</div>
        <h2>Vocabulary</h2>
        <table><tr><th>Word</th><th>Meaning</th><th>Example</th></tr>
        <tr><td>routine</td><td>thói quen lặp lại</td><td>I follow a short study routine every evening.</td></tr>
        <tr><td>review</td><td>ôn lại</td><td>Review new words after one day, one week, and one month.</td></tr>
        <tr><td>explain</td><td>giải thích</td><td>Try to explain the grammar point without looking.</td></tr></table>
        """,
    )
    material_2 = write_seed_file(
        MATERIAL_DIR,
        "seed_a2_daily_routines.html",
        "A2 Vocabulary: Daily Routines and Time",
        """
        <h2>Useful phrases</h2>
        <p>wake up, get dressed, have breakfast, go to school, do homework, have dinner, go to bed.</p>
        <h2>Time expressions</h2>
        <p>in the morning, at noon, in the afternoon, in the evening, at night, on weekdays, at the weekend.</p>
        <div class="note">Practice: I usually wake up at six thirty, but I wake up later at the weekend.</div>
        """,
    )
    course_notes = write_seed_file(
        COURSE_FILE_DIR,
        "seed_present_perfect_notes.html",
        "Present Perfect for Real Life",
        """
        <h2>Form</h2>
        <p>Subject + have/has + past participle.</p>
        <h2>Use</h2>
        <p>Use the present perfect for life experience, unfinished time, and recent results.</p>
        <table><tr><th>Situation</th><th>Example</th></tr>
        <tr><td>Experience</td><td>I have visited Da Nang twice.</td></tr>
        <tr><td>Unfinished time</td><td>She has studied three lessons this week.</td></tr>
        <tr><td>Recent result</td><td>They have finished the project.</td></tr></table>
        """,
    )
    grammar_notes = write_seed_file(
        SKILL_FILE_DIR,
        "seed_first_conditional.html",
        "Grammar B1: First Conditional",
        """
        <p>The first conditional describes a real possible result in the future.</p>
        <p><strong>Form:</strong> If + present simple, will + verb.</p>
        <div class="note">If I review vocabulary tonight, I will remember more words tomorrow.</div>
        """,
    )
    return {
        "material_1": f"uploads/materials/{material_1.name}",
        "material_2": f"uploads/materials/{material_2.name}",
        "course_notes": f"uploads/courses/files/{course_notes.name}",
        "grammar_notes": f"uploads/skills/files/{grammar_notes.name}",
    }


def fetch_ids(db, table, titles):
    if not titles:
        return []
    placeholders = ",".join("?" for _ in titles)
    return [
        row["id"]
        for row in db.execute(f"SELECT id FROM {table} WHERE title IN ({placeholders})", titles).fetchall()
    ]


def delete_by_ids(db, table, column, ids):
    if not ids:
        return
    placeholders = ",".join("?" for _ in ids)
    db.execute(f"DELETE FROM {table} WHERE {column} IN ({placeholders})", ids)


def cleanup_seed_data(db):
    course_ids = fetch_ids(db, "courses", COURSE_TITLES)
    delete_by_ids(db, "course_progress", "course_id", course_ids)
    delete_by_ids(db, "courses", "id", course_ids)

    package_ids = fetch_ids(db, "quiz_packages", QUIZ_PACKAGE_TITLES)
    delete_by_ids(db, "quiz_attempts", "package_id", package_ids)
    delete_by_ids(db, "quiz_questions", "package_id", package_ids)
    delete_by_ids(db, "quiz_packages", "id", package_ids)

    listening_ids = fetch_ids(db, "listening_lessons", LISTENING_TITLES)
    delete_by_ids(db, "listening_attempts", "lesson_id", listening_ids)
    delete_by_ids(db, "listening_lessons", "id", listening_ids)

    grammar_ids = fetch_ids(db, "grammar_lessons", GRAMMAR_TITLES)
    delete_by_ids(db, "grammar_attempts", "lesson_id", grammar_ids)
    delete_by_ids(db, "grammar_lessons", "id", grammar_ids)

    writing_ids = fetch_ids(db, "writing_tasks", WRITING_TITLES)
    delete_by_ids(db, "writing_submissions", "task_id", writing_ids)
    delete_by_ids(db, "writing_tasks", "id", writing_ids)

    speaking_ids = fetch_ids(db, "speaking_lessons", SPEAKING_TITLES)
    delete_by_ids(db, "speaking_attempts", "lesson_id", speaking_ids)
    delete_by_ids(db, "speaking_lessons", "id", speaking_ids)

    topic_ids = fetch_ids(db, "exam_speaking_topics", EXAM_SPEAKING_TITLES)
    delete_by_ids(db, "exam_speaking_sessions", "topic_id", topic_ids)
    delete_by_ids(db, "exam_speaking_topics", "id", topic_ids)

    room_ids = fetch_ids(db, "exam_rooms", EXAM_ROOM_TITLES)
    delete_by_ids(db, "exam_room_submissions", "room_id", room_ids)
    delete_by_ids(db, "exam_room_registrations", "room_id", room_ids)
    delete_by_ids(db, "exam_room_questions", "room_id", room_ids)
    delete_by_ids(db, "exam_rooms", "id", room_ids)

    delete_by_ids(db, "materials", "id", fetch_ids(db, "materials", MATERIAL_TITLES))
    placeholders = ",".join("?" for _ in EXAM_ROOM_TITLES)
    db.execute(f"DELETE FROM exam_results WHERE room_name IN ({placeholders})", EXAM_ROOM_TITLES)
    db.commit()


def upsert_user(db, username, email, fullname, role, class_name=None, phone=None):
    row = db.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email)).fetchone()
    if row:
        db.execute(
            """
            UPDATE users
            SET fullname = ?, username = ?, email = ?, role = ?, class = ?, phone = ?
            WHERE id = ?
            """,
            (fullname, username, email, role, class_name, phone, row["id"]),
        )
        return row["id"]
    cursor = db.execute(
        """
        INSERT INTO users (fullname, username, email, password_hash, role, class, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (fullname, username, email, generate_password_hash(SEED_PASSWORD), role, class_name, phone),
    )
    return cursor.lastrowid


def seed_users(db):
    teacher_id = upsert_user(
        db,
        TEACHER_USERNAME,
        "giaovien@lingo.vn",
        "Cô Nguyễn Khánh Linh",
        "teacher",
        None,
        "0909000001",
    )
    student_ids = []
    for username, email, fullname, class_name, phone in STUDENTS:
        student_ids.append(upsert_user(db, username, email, fullname, "student", class_name, phone))
    db.commit()
    return teacher_id, student_ids


def seed_materials(db, teacher_id, files):
    materials = [
        (
            "B1 Reading: Study Habits That Actually Work",
            "Bài đọc B1 có từ vựng, ví dụ và bảng ghi chú để học sinh luyện đọc trong web.",
            "file",
            None,
            None,
            files["material_1"],
            "seed_b1_study_habits.html",
        ),
        (
            "A2 Vocabulary: Daily Routines and Time",
            "Từ vựng A2 về thói quen hằng ngày, thời gian và câu mẫu dùng trong giao tiếp.",
            "file",
            None,
            None,
            files["material_2"],
            "seed_a2_daily_routines.html",
        ),
        (
            "Pronunciation Mini Lesson: Word Stress",
            "Video luyện nghe trọng âm từ, học sinh mở trực tiếp trong khung tài liệu.",
            "youtube",
            None,
            "eIho2S0ZahI",
            None,
            None,
        ),
    ]
    for item in materials:
        db.execute(
            """
            INSERT INTO materials
                (teacher_id, title, description, source_type, external_url, youtube_id, file_path, file_name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (teacher_id, *item),
        )


def seed_courses(db, teacher_id, files):
    courses = [
        {
            "title": "Present Perfect for Real Life",
            "content": "Học sinh phân biệt present perfect với past simple qua tình huống thật: trải nghiệm, khoảng thời gian chưa kết thúc và kết quả mới xảy ra.",
            "youtube_id": "eIho2S0ZahI",
            "material_path": files["course_notes"],
            "material_name": "seed_present_perfect_notes.html",
            "quiz": (
                "Choose the correct present perfect sentence.",
                "I have finished my homework.",
                "I finished my homework yesterday.",
                "I am finish my homework.",
                "I has finished my homework.",
                "A",
            ),
        },
        {
            "title": "Giving Opinions in Speaking Part 2",
            "content": "Bài học hướng dẫn mở ý kiến, đưa lý do, ví dụ và câu kết khi nói về một chủ đề quen thuộc.",
            "youtube_id": "Ks-_Mh1QhMc",
            "material_path": files["material_1"],
            "material_name": "seed_b1_study_habits.html",
            "quiz": (
                "Which phrase is best for giving an opinion politely?",
                "In my opinion, online learning is useful.",
                "You are wrong.",
                "I no like this.",
                "Because yes.",
                "A",
            ),
        },
        {
            "title": "Reading for Main Idea and Detail",
            "content": "Học sinh luyện đọc nhanh để tìm ý chính, sau đó đọc kỹ để chọn đáp án dựa trên bằng chứng trong bài.",
            "youtube_id": "8S0FDjFBj8o",
            "material_path": files["material_2"],
            "material_name": "seed_a2_daily_routines.html",
            "quiz": (
                "What should you read first when finding the main idea?",
                "The title and the first sentence of each paragraph.",
                "Only the final word.",
                "Only the answer options.",
                "Nothing, just guess.",
                "A",
            ),
        },
    ]
    ids = []
    for course in courses:
        q = course["quiz"]
        cursor = db.execute(
            """
            INSERT INTO courses
                (teacher_id, title, content, video_type, video_url, youtube_id, video_path, video_name,
                 material_type, material_url, material_path, material_name, quiz_question,
                 option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, 'youtube', ?, ?, NULL, NULL, 'file', NULL, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                teacher_id,
                course["title"],
                course["content"],
                f"https://www.youtube.com/watch?v={course['youtube_id']}",
                course["youtube_id"],
                course["material_path"],
                course["material_name"],
                *q,
            ),
        )
        ids.append(cursor.lastrowid)
    return ids


def insert_questions(db, package_id, questions):
    for position, q in enumerate(questions, start=1):
        db.execute(
            """
            INSERT INTO quiz_questions
                (package_id, position, question_text, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (package_id, position, *q),
        )


def seed_quizzes(db, teacher_id):
    quiz_1 = [
        ("She ___ English for three years.", "has studied", "studied yesterday", "is study", "have study", "A"),
        ("I am interested ___ learning new words.", "at", "in", "on", "for", "B"),
        ("Choose the synonym of 'improve'.", "make better", "forget", "delay", "remove", "A"),
        ("If it rains tomorrow, we ___ at home.", "stay", "will stay", "stayed", "staying", "B"),
        ("The opposite of 'cheap' is ___.", "expensive", "small", "quiet", "early", "A"),
        ("He speaks more clearly ___ his brother.", "than", "as", "to", "from", "A"),
        ("We need to ___ a decision today.", "make", "do", "take off", "put", "A"),
        ("Which sentence is correct?", "There are many students.", "There is many students.", "There be many students.", "There many students.", "A"),
        ("A person who teaches is a ___.", "teacher", "driver", "doctor", "farmer", "A"),
        ("I have never ___ sushi before.", "eat", "ate", "eaten", "eating", "C"),
    ]
    quiz_2 = [
        ("What do you say when you meet someone for the first time?", "Nice to meet you.", "See you yesterday.", "Good night at noon.", "I am rain.", "A"),
        ("Choose the correct question.", "Where do you live?", "Where you live?", "Where are live?", "Where living you?", "A"),
        ("I usually have breakfast ___ 6:30.", "in", "on", "at", "to", "C"),
        ("The plural of 'child' is ___.", "childs", "children", "childes", "childrens", "B"),
        ("Can I ___ a glass of water, please?", "have", "has", "having", "had", "A"),
        ("Which word is a place?", "library", "quickly", "beautiful", "sometimes", "A"),
        ("She ___ to school by bus.", "go", "goes", "going", "gone", "B"),
        ("What is the past simple of 'buy'?", "buyed", "bought", "buys", "buying", "B"),
        ("I am tired, so I want to ___.", "rest", "run fast forever", "eat a book", "open music", "A"),
        ("Choose the correct sentence.", "This is my notebook.", "This my notebook is.", "Notebook this my is.", "My is notebook this.", "A"),
    ]
    package_ids = []
    for title, difficulty, questions in [
        ("Quiz B1 - Grammar and Vocabulary", "B1", quiz_1),
        ("Quiz A2 - Everyday English", "A2", quiz_2),
    ]:
        cursor = db.execute(
            "INSERT INTO quiz_packages (teacher_id, title, difficulty) VALUES (?, ?, ?)",
            (teacher_id, title, difficulty),
        )
        insert_questions(db, cursor.lastrowid, questions)
        package_ids.append(cursor.lastrowid)
    return package_ids


def seed_skills(db, teacher_id, files):
    listening_rows = [
        (
            "Listening A2: Planning a Weekend",
            "Hi Mai, are you free this Saturday? I want to visit the city museum in the morning. After that, we can have lunch near the river. The weather forecast says it will be sunny.",
            "What will the speakers do on Saturday morning?",
            "Visit the city museum",
            "Watch a movie at home",
            "Study at the library",
            "Go shopping for clothes",
            "A",
        ),
        (
            "Listening B1: A Study Group Conversation",
            "Our English group meets every Wednesday after school. This week, we will review conditionals and prepare a short speaking task. Please bring your notebook and two questions for discussion.",
            "What should students bring to the study group?",
            "A notebook and two questions",
            "A sports uniform",
            "A dictionary only",
            "A lunch box",
            "A",
        ),
    ]
    for row in listening_rows:
        db.execute(
            """
            INSERT INTO listening_lessons
                (teacher_id, title, passage, quiz_question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (teacher_id, *row),
        )

    grammar_rows = [
        (
            "Grammar A2: Past Simple vs Present Perfect",
            "Use past simple for a finished time: I visited Hue last year. Use present perfect when the exact time is not important or the time period continues: I have visited Hue twice.",
            "file",
            None,
            files["course_notes"],
            "seed_present_perfect_notes.html",
            "Which sentence uses present perfect correctly?",
            "I have seen that film before.",
            "I have see that film before.",
            "I seen that film yesterday.",
            "I seeing that film now.",
            "A",
        ),
        (
            "Grammar B1: First Conditional",
            "The first conditional talks about a real future possibility. Form: If + present simple, will + verb.",
            "file",
            None,
            files["grammar_notes"],
            "seed_first_conditional.html",
            "Choose the correct first conditional sentence.",
            "If I study tonight, I will pass the quiz.",
            "If I studied tonight, I pass the quiz.",
            "If I will study tonight, I pass the quiz.",
            "If I studying tonight, I will passed.",
            "A",
        ),
    ]
    for row in grammar_rows:
        db.execute(
            """
            INSERT INTO grammar_lessons
                (teacher_id, title, content, material_type, material_url, material_path, material_name,
                 quiz_question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (teacher_id, *row),
        )

    writing_rows = [
        (
            "Writing Task: Email to a Teacher",
            "Write an email to your English teacher. Ask for advice about improving your speaking skill. Include your problem, one thing you have tried, and one question.",
            20,
        ),
        (
            "Writing Task: Opinion Paragraph about Online Learning",
            "Write one paragraph about this topic: Online learning is useful for high school students. Do you agree or disagree? Give reasons and examples.",
            25,
        ),
    ]
    writing_ids = []
    for row in writing_rows:
        cursor = db.execute(
            "INSERT INTO writing_tasks (teacher_id, title, prompt, time_limit_minutes) VALUES (?, ?, ?, ?)",
            (teacher_id, *row),
        )
        writing_ids.append(cursor.lastrowid)

    speaking_rows = [
        (
            "Speaking Shadowing: My Daily Study Routine",
            "I study English for thirty minutes every evening. First, I review new words. Then I listen to a short conversation and repeat it aloud.",
        ),
        (
            "Speaking Shadowing: Describing a Favorite Place",
            "My favorite place is a quiet bookstore near my school. I like it because I can read, relax, and learn new ideas there.",
        ),
    ]
    speaking_ids = []
    for title, passage in speaking_rows:
        notes = [
            {"word": word.lower().strip(".,!?"), "pronunciation": f"/{word.lower().strip('.,!?')}/", "meaning": "Từ luyện phát âm trong câu mẫu"}
            for word in passage.split()
        ]
        cursor = db.execute(
            "INSERT INTO speaking_lessons (teacher_id, title, passage, word_notes_json) VALUES (?, ?, ?, ?)",
            (teacher_id, title, passage, json.dumps(notes, ensure_ascii=False)),
        )
        speaking_ids.append(cursor.lastrowid)
    return writing_ids, speaking_ids


def seed_exam_speaking(db, teacher_id):
    topics = [
        (
            "Speaking AI Test: Hobbies and Free Time",
            "Ask the student about hobbies, why they enjoy them, how often they do them, and whether hobbies can help students reduce stress.",
            "A2-B1",
            "Hello, nice to meet you. What is your name and what do you like doing in your free time?",
        ),
        (
            "Speaking AI Test: Learning English Online",
            "Discuss online English learning, useful tools, difficulties, and a realistic plan for improving speaking and vocabulary.",
            "B1",
            "Hello. Can you tell me how you usually learn English online?",
        ),
    ]
    ids = []
    for row in topics:
        cursor = db.execute(
            """
            INSERT INTO exam_speaking_topics (teacher_id, title, topic_prompt, level, opening_question)
            VALUES (?, ?, ?, ?, ?)
            """,
            (teacher_id, *row),
        )
        ids.append(cursor.lastrowid)
    return ids


def seed_exam_rooms(db, teacher_id):
    now = datetime.now()
    rooms = [
        (
            "B1 Mock Test - Reading and Use of English",
            "Đề thi B1 gồm câu đơn LN1 và bài đọc LN2, thang điểm 10.",
            (now - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M"),
            60,
            "b1-mock-reading-use-of-english.docx",
        ),
        (
            "A2 Quick Test - Vocabulary and Grammar",
            "Đề nhanh A2 để luyện trước khi vào phòng thi chính thức.",
            (now + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M"),
            30,
            "a2-quick-test-vocabulary-grammar.docx",
        ),
    ]
    room_ids = []
    for room in rooms:
        cursor = db.execute(
            """
            INSERT INTO exam_rooms
                (teacher_id, title, description, start_at, duration_minutes, source_file_name, total_questions)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (teacher_id, *room, 10),
        )
        room_ids.append(cursor.lastrowid)

    b1_questions = [
        ("LN1", "", "Choose the best word: The teacher asked us to ___ the new vocabulary before Friday.", "review", "repair", "replace", "refuse", "A"),
        ("LN1", "", "Which sentence is correct?", "She has lived here since 2022.", "She lived here since 2022.", "She has live here since 2022.", "She lives here yesterday.", "A"),
        ("LN1", "", "The word 'confident' is closest in meaning to ___.", "sure of yourself", "very tired", "late", "expensive", "A"),
        ("LN1", "", "If students practise every day, they ___ faster.", "will improve", "improved", "improves", "are improved yesterday", "A"),
        ("LN1", "", "Choose the correct preposition: She is good ___ explaining ideas.", "at", "on", "for", "with", "A"),
        ("LN2", "Many teenagers use short videos to learn English. Short videos are easy to watch, but they are not enough by themselves. Learners need to take notes, repeat useful phrases, and use the language in speaking or writing. A balanced routine can include videos, reading, vocabulary review, and real conversation.", "What is the main idea of the passage?", "Short videos can help, but learners need an active routine.", "Teenagers should never watch videos.", "Reading is not useful for English learners.", "Conversation is impossible online.", "A"),
        ("LN2", "Many teenagers use short videos to learn English. Short videos are easy to watch, but they are not enough by themselves. Learners need to take notes, repeat useful phrases, and use the language in speaking or writing. A balanced routine can include videos, reading, vocabulary review, and real conversation.", "According to the passage, what should learners do with useful phrases?", "Repeat them and use them.", "Delete them.", "Only translate them once.", "Avoid saying them aloud.", "A"),
        ("LN2", "A school club started an English reading challenge. Students choose one short article each week and write a five-sentence summary. At the end of the month, they share the most useful words they learned. The club wants students to read regularly, not perfectly.", "How often do students choose an article?", "Once a week", "Every day", "Once a year", "Twice a day", "A"),
        ("LN2", "A school club started an English reading challenge. Students choose one short article each week and write a five-sentence summary. At the end of the month, they share the most useful words they learned. The club wants students to read regularly, not perfectly.", "What do students share at the end of the month?", "Useful words they learned", "Their phone passwords", "Only grammar mistakes", "A list of movies", "A"),
        ("LN1", "", "Choose the best answer: I look forward to ___ from you.", "hearing", "hear", "heard", "hears", "A"),
    ]
    a2_questions = [
        ("LN1", "", "She ___ breakfast at seven o'clock.", "has", "have", "having", "had yesterday now", "A"),
        ("LN1", "", "What is the opposite of 'hot'?", "cold", "fast", "young", "clean", "A"),
        ("LN1", "", "Choose the correct sentence.", "There is a book on the table.", "There are a book on the table.", "There be a book on table.", "There a book is table.", "A"),
        ("LN1", "", "I go to school ___ bus.", "by", "on", "at", "in", "A"),
        ("LN1", "", "The past simple of 'go' is ___.", "went", "goed", "goes", "going", "A"),
        ("LN2", "Lan wakes up at six thirty on weekdays. She has breakfast with her family and goes to school by bike. After school, she does homework and listens to English songs for ten minutes.", "How does Lan go to school?", "By bike", "By train", "By plane", "By taxi", "A"),
        ("LN2", "Lan wakes up at six thirty on weekdays. She has breakfast with her family and goes to school by bike. After school, she does homework and listens to English songs for ten minutes.", "What does Lan do after school?", "Does homework and listens to English songs", "Goes swimming every day", "Buys a new bike", "Sleeps all afternoon", "A"),
        ("LN1", "", "Can you help me, ___?", "please", "yesterday", "because", "never", "A"),
        ("LN1", "", "Which word is food?", "bread", "window", "pencil", "cloud", "A"),
        ("LN1", "", "We ___ English on Monday.", "study", "studies", "studying", "studied tomorrow", "A"),
    ]
    for room_id, questions in zip(room_ids, [b1_questions, a2_questions]):
        for position, q in enumerate(questions, start=1):
            db.execute(
                """
                INSERT INTO exam_room_questions
                    (room_id, position, question_type, passage, question_text,
                     option_a, option_b, option_c, option_d, correct_answer)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (room_id, position, *q),
            )
    return room_ids


def seed_student_activity(db, student_ids, course_ids, package_ids, writing_ids, speaking_ids, topic_ids, room_ids):
    main_student_id = student_ids[0]
    for course_id in course_ids[:2]:
        db.execute(
            """
            INSERT INTO course_progress (user_id, course_id, selected_answer, score)
            VALUES (?, ?, 'A', 100)
            """,
            (main_student_id, course_id),
        )

    scores = [940, 910, 890, 870, 855, 830, 805, 780, 760, 735, 710, 690]
    for student_id, score in zip(student_ids, scores):
        db.execute(
            "INSERT INTO exam_results (user_id, room_name, score, taken_at) VALUES (?, ?, ?, ?)",
            (student_id, EXAM_ROOM_TITLES[0], score, datetime.now().isoformat(timespec="seconds")),
        )

    for index, student_id in enumerate(student_ids):
        percentage = max(50, 95 - index * 4)
        bonus = 10 if percentage > 80 else 0
        db.execute(
            """
            INSERT INTO quiz_attempts
                (user_id, package_id, correct_count, total_questions, percentage, bonus_points)
            VALUES (?, ?, ?, 10, ?, ?)
            """,
            (student_id, package_ids[index % len(package_ids)], round(percentage / 10), percentage, bonus),
        )

    db.execute(
        """
        INSERT INTO writing_submissions
            (task_id, user_id, content, ai_score, ai_feedback, teacher_score, teacher_feedback, status, graded_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'graded', CURRENT_TIMESTAMP)
        """,
        (
            writing_ids[0],
            main_student_id,
            "Dear teacher, I want to improve my speaking because I feel nervous when I answer questions. I have tried listening to short conversations and repeating them. Could you please tell me how to practise pronunciation at home?",
            82,
            "Bài viết rõ yêu cầu, có lý do và câu hỏi phù hợp. Nên thêm một câu kết lịch sự hơn.",
            85,
            "Nội dung tốt, dùng câu hỏi lịch sự. Cần chú ý viết dài hơn và kiểm tra mạo từ.",
        ),
    )

    missed_words = [
        {"word": "routine", "pronunciation": "/ruːˈtiːn/", "meaning": "thói quen"},
        {"word": "conversation", "pronunciation": "/ˌkɒnvəˈseɪʃn/", "meaning": "cuộc hội thoại"},
    ]
    db.execute(
        """
        INSERT INTO speaking_attempts (user_id, lesson_id, transcript, score, missed_words_json)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            main_student_id,
            speaking_ids[0],
            "I study English for thirty minutes every evening first I review new words then I listen to a short conversation",
            86,
            json.dumps(missed_words, ensure_ascii=False),
        ),
    )

    conversation = [
        {"ai": "Hello. What is your name and what do you like doing in your free time?", "student": "My name is Minh Anh. I like reading books and listening to music."},
        {"ai": "How often do you read books?", "student": "I read three or four times a week, usually before bedtime."},
    ]
    db.execute(
        """
        INSERT INTO exam_speaking_sessions
            (topic_id, user_id, conversation_json, score, feedback, pronunciation_feedback, unclear_words_json)
        VALUES (?, ?, ?, 84, ?, ?, ?)
        """,
        (
            topic_ids[0],
            main_student_id,
            json.dumps(conversation, ensure_ascii=False),
            "Trả lời đúng chủ đề, có ví dụ cá nhân. Nên mở rộng câu trả lời bằng lý do rõ hơn.",
            "Phát âm khá rõ. Cần chú ý âm cuối trong words như books và times.",
            json.dumps([{"word": "books", "issue_vi": "âm cuối /s/ chưa rõ", "suggestion_vi": "đọc bật nhẹ âm /s/ cuối từ"}], ensure_ascii=False),
        ),
    )

    answers = {str(i): "A" for i in range(1, 11)}
    db.execute(
        """
        INSERT INTO exam_room_registrations (room_id, user_id)
        VALUES (?, ?)
        """,
        (room_ids[0], main_student_id),
    )
    db.execute(
        """
        INSERT INTO exam_room_submissions
            (room_id, user_id, answers_json, correct_count, total_questions, score)
        VALUES (?, ?, ?, 9, 10, 9.0)
        """,
        (room_ids[0], main_student_id, json.dumps(answers, ensure_ascii=False)),
    )


def count_table(db, table):
    return db.execute(f"SELECT COUNT(*) AS total FROM {table}").fetchone()["total"]


def main():
    with app.app_context():
        init_db()
        db = get_db()
        cleanup_seed_data(db)
        files = prepare_seed_files()
        teacher_id, student_ids = seed_users(db)
        seed_materials(db, teacher_id, files)
        course_ids = seed_courses(db, teacher_id, files)
        package_ids = seed_quizzes(db, teacher_id)
        writing_ids, speaking_ids = seed_skills(db, teacher_id, files)
        topic_ids = seed_exam_speaking(db, teacher_id)
        room_ids = seed_exam_rooms(db, teacher_id)
        seed_student_activity(db, student_ids, course_ids, package_ids, writing_ids, speaking_ids, topic_ids, room_ids)
        db.commit()

        print(f"Seed data loaded into: {DB_PATH}")
        print(f"Users: {count_table(db, 'users')}")
        print(f"Materials: {count_table(db, 'materials')}")
        print(f"Courses: {count_table(db, 'courses')}")
        print(f"Quiz packages: {count_table(db, 'quiz_packages')}")
        print(f"Listening lessons: {count_table(db, 'listening_lessons')}")
        print(f"Grammar lessons: {count_table(db, 'grammar_lessons')}")
        print(f"Writing tasks: {count_table(db, 'writing_tasks')}")
        print(f"Speaking lessons: {count_table(db, 'speaking_lessons')}")
        print(f"Speaking AI topics: {count_table(db, 'exam_speaking_topics')}")
        print(f"Exam rooms: {count_table(db, 'exam_rooms')}")
        print(f"Login student: {MAIN_STUDENT_USERNAME} / {SEED_PASSWORD}")
        print(f"Login teacher: {TEACHER_USERNAME} / {SEED_PASSWORD}")


if __name__ == "__main__":
    main()
