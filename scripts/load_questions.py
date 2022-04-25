from datetime import datetime
from polls.models import Question


questions = [
    "মানুষের রক্তে লোহিত রক্তকণিকা কোথায় সঞ্চিত হয় ?",
    "আন্তর্জাতিক এভারেস্ট দিবস কবে পালন করা হয় ?",
    "নিন্মের কোন অংশে সর্বাপেক্ষা ভালো প্রতিবিম্ব গঠিত হয় ?",
    "ডাবের জলে কোন হরমোন থাকে ?",
    "বিজয়নগর রাজ্যের সবচেয়ে প্রতিভাশালী রাজা কে ছিলেন ?",
    "‘দেশের স্টিলফ্রেম’ কাদের বলে ?",
    "কুইতো কোন দেশের রাজধানী ?",
]

def run():
    for question in questions:
        Question.objects.create(
            question_text=question,
            pub_date=datetime.now()
        )
