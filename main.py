class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):

    uncovered = set(subjects)
    # Скидаємо попередні призначення (на випадок повторного виклику)
    for teacher in teachers:
        teacher.assigned_subjects = set()

    schedule = []

    while uncovered:
        # Найкращий кандидат: максимум покритих предметів, за рівності — молодший
        best_teacher = max(
            teachers,
            key=lambda t: (len(t.can_teach_subjects & uncovered), -t.age),
        )
        coverage = best_teacher.can_teach_subjects & uncovered

        # Якщо навіть найкращий нікого не покриває — покрити неможливо
        if not coverage:
            return None

        best_teacher.assigned_subjects = coverage
        schedule.append(best_teacher)
        uncovered -= coverage

    return schedule


if __name__ == '__main__':
    
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com',
                {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com',
                {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com',
                {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com',
                {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com',
                {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com',
                {'Біологія'}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
